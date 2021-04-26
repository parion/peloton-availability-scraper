import os
import discord
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Env Variables
URL = os.environ['URL']
TIMEOUT = os.environ['TIMEOUT']
TOKEN = os.environ['DISCORD_TOKEN']
USER_ID = os.environ['DISCORD_USER_ID']
CHROME_BIN = os.environ.get('GOOGLE_CHROME_SHIM', None)

# Set up Selenium WebDriver using Chrome executable and point to URL
CHROMEDRIVER_PATH = './chromedriver'
chrome_options = Options()
chrome_options.binary_location = CHROME_BIN
driver = webdriver.Chrome(
    executable_path='./chromedriver', options=chrome_options)
driver.get(URL)
print('💻\tConnecting with Selenium...')

# Wait until either app is loaded or timeout is reached (exception)
try:
    WebDriverWait(driver, float(TIMEOUT)).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
except TimeoutException:
    print('🤨\tNo h1 tag found. App may have not loaded correctly in the alotted time.')
    driver.quit()
print('🕵️\tConnected. Scraping...')

availableDates = []
try:
  # Get dates container element
    datesContainer = driver.find_elements_by_xpath(
        '//*[@data-test-id="datesContainer"]')
    # For each button in dates container, get the text of the button and retrieve digits
    for button in datesContainer:
        dateString = button.find_element_by_tag_name(
            'button').text.split(', ')[1]
        # If date exists, add to available dates array
        if dateString:
            date = datetime.strptime(f'{dateString} 2021', '%b %d %Y')
            availableDates.append(date)
except NoSuchElementException:
    print('🤨\tNo buttons found.')
    driver.quit()
# No need for webdriver to stick around
driver.quit()
print('📆\tDates found. Looking up earlier dates...')

# For each date in availableDates, check if value is less than current date
for date in availableDates:
    if datetime.now() < date:
        print('🎉\tEarlier date found! Sending Discord message...')
        client = discord.Client()

        @client.event
        async def on_ready():
            print(f'🔌\t{client.user} has connected to Discord!')
            user = await client.fetch_user(USER_ID)
            await user.send(f'🚨 An earlier delivery date on **{date.strftime("%B %d, %Y")}** is available! Go, go go!🚨\n' + URL)
            # Close Discord client after sending listings
            await client.close()

        # Start Discord client
        client.run(TOKEN)
        break

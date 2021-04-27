# Peloton Availability Scraper

A simple Python web scraper that watches the available delivery dates for a Peloton product and notifies through Discord when an earlier date than the current delivery date is available.

## Running Locally

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/). Clone this repository to your desired local location.

For this program, a Discord bot is required. You can learn how to set one up on the [Discord Developer Portal](https://discord.com/developers/docs/intro). You'll also likely want to send the availability message to your Discord profile and you can find your Discord user ID on [Discord's support page](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-).

This script uses Selenium to load the React application and wait for content to scrape. To use Selenium, you'll need a Web Driver for your browser of choice. Since Chrome is used here, visit [Chrome WebDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) and download the latest version.

Create an `.env` file in root directory and provide definitions for each environment variable listed.

```
# Sets the Selenium timeout to load the Peloton availability page
TIMEOUT = 30
# Your custom Peloton rescheduling page
URL=https://www.onepeloton.com/delivery/UUID/reschedule
# Discord bot token
DISCORD_TOKEN=TOKEN_ID
# Discord User ID to send message to (likely, yourself)
DISCORD_USER_ID=UUID
# Path to Chrome Web Driver (needed for Selenium)
CHROMEDRIVER_PATH=./chromedriver
```

Finally, provide your current delivery date to the DELIVERY_DATE variable defined in `peloton.py` (hopefully future onboarding is made easier).

And that should be all the setup! Find your delivery dates by running

```sh
$ pip install -r requirements.txt
$ python3 peloton.py
```

## Deploying to Heroku

**TODO**

For now, I'll tell you you'll need the python buildpack, [heroku-buildpack-google-chrome](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-google-chrome), and [heroku-buildpack-chromedriver](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-chromedriver).

```sh
$ heroku create
$ git push heroku main
```

or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Contributions

Contributions are welcome and encouraged. Currently the onboarding process and code break-ups could use some work. Refactorings, ehancements, and bug fixes are all appreciated. 🙏

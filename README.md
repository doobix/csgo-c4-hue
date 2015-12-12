# csgo-c4-hue
These scripts let will change the colors of your Philips Hue lights based on the C4 bomb status in Counter-Strike: Global Offensive.

## Features

* Each light blinks red 1-by-1 when bomb has been planted.
* All lights blink red when bomb has been planted for at least 35 seconds.
* All lights turn orange when bomb has exploded.
* All lights turn blue when bomb has been defused.
* All lights turn white when there is no bomb status.

## Installation

1. Install Python 2.7 if your machine doesn't have it.
2. Install Flask via pip.

  OS X: `pip install flask`

  Windows: `C:\Python27\Scripts\pip.exe install flask`

3. Edit `csgo-c4-hue.py` and fill in the values for your hue bridge IP and hue user.

  Example:

  ```
  HUE_BRIDGE_IP = '192.168.1.100'
  HUE_USER = '1a2a3a4a5a6a7a8a9a0a'
  ```

## How to get hue bridge IP

To get your hue bridge IP, visit: http://www.meethue.com/api/nupnp

## How to make a hue user

You can make a new user by going to the API Debug Tool: http://<your hue bridge ip>/debug/clip.html

For the url input box, enter `/api`.

For the message body, enter `{"devicetype":"csgo_c4#user"}`

Now you can press the link button on the bridge and then click the POST button in the API Debug Tool.

You should see a success message along with `"username": "<long random character string>"` in the command response area.

The long random character string is what needs to be copy/pasted into `csgo-c4-hue.py`.

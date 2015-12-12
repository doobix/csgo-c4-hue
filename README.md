# csgo-c4-hue
These scripts will change the colors of your Philips Hue lights based on the C4 bomb status in Counter-Strike: Global Offensive.

## Features

* Each light blinks red 1-by-1 when bomb has been planted.
* All lights blink red when bomb has been planted for at least 35 seconds.
* All lights turn orange when bomb has exploded.
* All lights turn blue when bomb has been defused.
* All lights turn white when there is no bomb status.

## Installation

1. Copy `gamestate_integration_c4_hue.cfg` to your CS:GO cfg directory.

  OS X: `/Users/<username>/Library/Application Support/Steam/SteamApps/common/Counter-Strike Global Offensive/csgo/cfg`

  Windows: `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg`

2. Install Python 2.7 if your machine doesn't have it.
3. Install Flask via pip.

  OS X: `pip install flask`

  Windows: `C:\Python27\Scripts\pip.exe install flask`

4. Edit `csgo-c4-hue.py` and fill in the values for your [hue bridge IP](#how-to-get-hue-bridge-ip) and [hue user](#how-to-make-a-hue-user).

  Example:

  ```
  HUE_BRIDGE_IP = '192.168.1.100'
  HUE_USER = '1a2a3a4a5a6a7a8a9a0a'
  ```

## Usage

Run both `csgo-c4-hue.py` and `csgo-c4-hue-server.py` scripts while playing CS:GO.

The `csgo-c4-hue-server.py` script will be receiving the gamestate data from CS:GO and it will write the bomb status to the file named `bomb_status`.

The `csgo-c4-hue.py` script will be reading the `bomb_status` file every 250 ms and will change the hue lights depending on what is in that file.

## Appendix

### How to get hue bridge IP

To get your hue bridge IP, visit: http://www.meethue.com/api/nupnp

### How to make a hue user

You can make a new user by going to the API Debug Tool: `http://<your hue bridge ip>/debug/clip.html`

For the url input box, enter `/api`.

For the message body, enter `{"devicetype":"csgo_c4#user"}`

Now you can press the link button on the bridge and then click the POST button in the API Debug Tool.

You should see a success message along with `"username": "<long random character string>"` in the command response area.

The long random character string is what needs to be copy/pasted into `csgo-c4-hue.py`.

import json
import requests
import time

HUE_BRIDGE_IP = ''
HUE_USER = ''
HUE_API = 'http://{}/api/{}/'.format(HUE_BRIDGE_IP, HUE_USER)

def main():
    lights = []
    bomb_time = None
    current_status = ''
    r = requests.get('{}groups/0'.format(HUE_API))
    json_data = r.json()
    lights = json_data['lights']
    last_blink_time = None
    blink_on = True
    last_strobe_time = None
    current_strobe_light = 1
    previous_strobe_light = None

    while True:
        f = open('bomb_status', 'r')
        bomb_status = f.read()
        if bomb_status == 'planted':
            print 'bomb planted!'
            if current_status != 'planted':
                change_all_lights(no_lights())
                blink_on = True
                current_status = 'planted'
            if bomb_time is None:
                bomb_time = time.time()
            total_bomb_time = time.time() - bomb_time
            print 'bomb planted for {} seconds'.format(total_bomb_time)
            if total_bomb_time >= 30:
                if last_blink_time is None:
                    last_blink_time = time.time() - 2
                elapsed_blink_time = time.time() - last_blink_time
                if elapsed_blink_time >= 1:
                    last_blink_time = time.time()
                    blink_on = blink_lights(blink_on)
            else:
                if last_strobe_time is None:
                    last_strobe_time = time.time() - 2
                elapsed_strobe_time = time.time() - last_strobe_time
                if elapsed_strobe_time >= 1:
                    last_strobe_time = time.time()
                    current_strobe_light, previous_strobe_light = strobe_lights(lights, current_strobe_light, previous_strobe_light)
        elif bomb_status == 'exploded' and current_status != 'exploded':
            print 'bomb exploded!'
            current_status = 'exploded'
            change_all_lights(explode_lights())
        elif bomb_status == 'defused' and current_status != 'defused':
            print 'bomb defused!'
            current_status = 'defused'
            change_all_lights(blue_lights())
        elif bomb_status == '' and current_status != '':
            print 'no bomb status!'
            current_status = ''
            bomb_time = None
            last_blink_time = None
            last_strobe_time = None
            change_all_lights(white_lights())
        f.close()
        time.sleep(.250)

def blink_lights(blink_on):
    if blink_on:
        change_all_lights(red_lights())
        return False
    else:
        change_all_lights(no_lights())
        return True

def strobe_lights(lights, current_strobe_light, previous_strobe_light):
    # Turn off previous light
    if previous_strobe_light and current_strobe_light != previous_strobe_light:
        change_light(previous_strobe_light, no_lights())
        print 'off {}'.format(previous_strobe_light)
    # Turn on current light
    previous_strobe_light = current_strobe_light
    change_light(current_strobe_light, red_lights())
    if current_strobe_light < len(lights):
        current_strobe_light += 1
    else:
        current_strobe_light = 1
    print 'on {}'.format(previous_strobe_light)
    return current_strobe_light, previous_strobe_light

def change_light(light, light_type):
    r = requests.put(
        '{}lights/{}/state'.format(HUE_API, light),
        json=light_type
    )

def change_all_lights(light_type):
    r = requests.put(
        '{}groups/0/action'.format(HUE_API),
        json=light_type
    )

def red_lights():
    return {
        'on': True,
        'sat': 254,
        'bri': 254,
        'hue': 0,
        'transitiontime': 0
    }

def blue_lights():
    return {
        'on': True,
        'sat': 254,
        'bri': 254,
        'hue': 45000,
        'transitiontime': 0
    }

def explode_lights():
    return {
        'on': True,
        'sat': 254,
        'bri': 254,
        'hue': 10000,
        'transitiontime': 0
    }

def white_lights():
    return {
        'on': True,
        'sat': 0,
        'bri': 254,
        'hue': 10000
    }

def no_lights():
    return {
        'on': False,
        'transitiontime': 0
    }

if __name__ == "__main__":
    main()

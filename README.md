# post_to_homeassistant
This is a python script to post to the Home Assistant REST API using Long Lived Tokens.  This will allow you to control lights, switches and input_booleans using command line arguments.

Usage example:
`post_to_homeassistant.py input_boolean.front_door_camera_motion on`

The requests module is required.  Install requests with pip:
```pip install requests```

You will need to edit the script and assign the URL to your Home Assistant instance, as well as the token.  You can create a token from your profile page in Home Assistant.  More information found here: [https://www.home-assistant.io/docs/authentication/](https://www.home-assistant.io/docs/authentication/)

The goal of this repo is to intergrate Blue Iris into Home Assistant.  I've included an example Home Assistant package, see ```blueiris.yaml```.  This script is open ended and could be used with any project which is able to execute a python script to trigger a state change.

Home Assistant configuration for Blue Iris intergration example:
```
camera:
  - platform: mjpeg
    mjpeg_url: http://<blueiris server ip>:81/mjpg/FrontDoor  # This needs to be the URL of your Blue Iris web server
    name: Front Door 
    # If you've configured the BI Web Server to not require authentication from
    # LAN connections, remove the the following three lines
    username: !secret bi_username
    password: !secret bi_password
    authentication: basic

binary_sensor:
  - platform: template
    sensors:
      front_door_motion:
        device_class: motion
        value_template: "{{ is_state('input_boolean.front_door_motion', 'on') }}"

input_boolean:
  front_door_motion:
    name: Front Door Motion
```


This will create a binary sensor (front_door_motion) based on the state of the input_boolean (front_door_camera_motion) which can be controlled using the post_to_homeassistant script.

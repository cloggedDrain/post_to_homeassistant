# post_to_homeassistant
This is a python script to post to the Home Assistant REST API using Long Lived Tokens.  This will allow you to control lights, switches and input_booleans using command line arguments.

Usage example:
`post_to_homeassistant.py input_boolean.front_door_camera_motion on`

The requests module is required.  Install requests with pip:
```pip install requests```


The goal of this repo is to intergrate Blue Iris into Home Assistant.  I've included an example Home Assistant package, see ```blueiris.yaml```

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

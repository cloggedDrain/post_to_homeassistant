# post_to_homeassistant

Python script to post to Home Assistant REST API.  Useful for intergration other systems, for example Blue Iris.

The requests module is required.  Install requests with pip:
```pip install requests```

Usage example:
`post_to_homeassistant.py input_boolean.front_door_camera_motion on`


Home Assistant configuration for Blue Iris intergration:
```
camera:
  - platform: mjpeg
    mjpeg_url: http://<blue iris ip address/hostname>:81/mjpg/FrontDoor
    name: Front Door
    #username: [redacted]  # authentication is supported, or can be bypassed through blue iris configuration for lan-only connections
    #password: [redacted]
    #authentication: basic

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

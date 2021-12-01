!! NOTE this sensor is still in development !!

# P2000 Sensor

This is a simple p2000 sensor for home assistant

### Installation

Copy this folder to `<config_dir>/custom_components/p2000/`.

Add the following to your `configuration.yaml` file:


```yaml
# Example configuration.yaml entry
sensor:
  - platform: p2000
    name: p2000_Zwolle
    gemeenten:
      - zwolle
    capcodes:
      - 1234567
```

** Either or 'gemeenten' or 'capcodes' should be filled. **

Be aware that if you use `gemeenten` and `capcodes` in the same config entry both one of the `gemeenten` and one of the `capcodes` should be in the `melding`


You should get a sensor like te following with a lot of attributes.

The id is unique and changes with every new p2000 message.


![Tux, the Linux mascot](./assets/screenshot01.png)

Extracting data can be done with a template like:

`{{ state_attr('sensor.p2000_zwolle', 'melding') }}`
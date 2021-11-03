!! NOTE this sensor is still in development !!

# Example Sensor

This is a simple p2000 sensor for home assistant

### Installation

Copy this folder to `<config_dir>/custom_components/p2000/`.

Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: p2000
    gemeenten:
      - zwolle
    capcodes:
      - 1234567
```

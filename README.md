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

More information on your dashboard.<br> tekst in Dutch.<br>
![afbeelding](https://user-images.githubusercontent.com/62996429/144426649-70ec4732-14e1-4856-aa40-d8b81e99f3c3.png)

```
type: markdown
content: >
  Datum : {{ state_attr('sensor.p2000', 'datum' ) }}   Tijd: {{
  state_attr('sensor.p2000', 'tijd') }}


  Melding : {{ state_attr('sensor.p2000', 'melding') }}<br>


  {{ state_attr('sensor.p2000', 'tekstmelding') }}<br>

  -

  Plaats: {{ state_attr('sensor.p2000', 'plaats') }}

  Straat : {{ state_attr('sensor.p2000', 'straat') }} 

  Regio : {{ state_attr('sensor.p2000', 'regio') }}

  capcode : {{ state_attr('sensor.p2000', 'capstring') }}

  lat : {{ state_attr('sensor.p2000', 'latitude') }}  long: {{
  state_attr('sensor.p2000', 'longitude') }}

  <br>

  Dienst: {{ state_attr('sensor.p2000', 'dienst') }}

  info :  {{ state_attr('sensor.p2000', 'brandinfo') }}<br>

  Regio id : {{ state_attr('sensor.p2000', 'regioid') }}       Dienst id : {{
  state_attr('sensor.p2000', 'dienstid') }}

  Prio : {{ state_attr('sensor.p2000', 'prio1') }}

  Grip : {{ state_attr('sensor.p2000', 'grip') }}


  Id nr : {{ state_attr('sensor.p2000', 'id') }}<br>
```
Also <br>
![afbeelding](https://user-images.githubusercontent.com/62996429/144427222-1118abfa-4710-4f48-962f-b9f89cd523bc.png)

```
type: logbook
entities:
  - sensor.p2000
hours_to_show: 24
title: '112'
```

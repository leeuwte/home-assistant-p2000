import logging


import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.const import (CONF_NAME, CONF_ICON)
import homeassistant.helpers.config_validation as cv
from .api import P2000Api

"""Start the logger"""
_LOGGER = logging.getLogger(__name__)
 
DEFAULT_NAME = "p2000"

CONF_GEMEENTEN = "gemeenten"
CONF_CAPCODES = "capcodes"
CONF_DIENSTEN = "diensten"
CONF_WOONPLAATSEN = "woonplaatsen"
CONF_REGIOS = "regios"
CONF_PRIO1 = "prio1"
CONF_LIFE = "lifeliners"


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_ICON, default="mdi:fire-truck"): cv.icon,
    vol.Optional(CONF_WOONPLAATSEN): vol.All(cv.ensure_list, [cv.string]),
    vol.Optional(CONF_GEMEENTEN): vol.All(cv.ensure_list, [cv.string]),
    vol.Optional(CONF_CAPCODES): vol.All(cv.ensure_list, [cv.string]),
    vol.Optional(CONF_REGIOS): vol.All(cv.ensure_list, [cv.string]),
    vol.Optional(CONF_DIENSTEN): vol.All(cv.ensure_list, [cv.string]),
    vol.Optional(CONF_PRIO1, default=False): cv.boolean,
    vol.Optional(CONF_LIFE, default=False): cv.boolean,
    
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the sensor platform."""

    name = config.get(CONF_NAME)
    icon = config.get(CONF_ICON)
    
    apiFilter = {}
        
    # Add string / string array properties
    for prop in [CONF_WOONPLAATSEN, CONF_GEMEENTEN, CONF_CAPCODES, CONF_DIENSTEN, CONF_REGIOS]:
        if prop in config:
            apiFilter[prop] = config[prop]

    # Add boolean properties
    for prop in [CONF_PRIO1, CONF_LIFE]:
        if prop in config and config[prop] == True:
            apiFilter[prop] = "1"
     
    api = P2000Api()

    add_entities([P2000Sensor(api, name, icon, apiFilter)])


class P2000Sensor(SensorEntity):
    """Representation of a Sensor."""

    def __init__(self, api, name, icon, apiFilter):
        """Initialize the sensor."""
        self.api = api
        self.attributes = {}
        self.apiFilter = apiFilter
        self._name = name
        self.icon = icon
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the monitored installation."""
        attributes = self.attributes
        attributes['icon'] = self.icon
        return attributes

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        data = self.api.get_data(self.apiFilter)

        if (data == None):
            return

        self.attributes = data
        self._state = data["melding"]


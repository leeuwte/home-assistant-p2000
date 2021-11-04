"""Constants for the P2000 integration."""
import logging
from typing import Final

DOMAIN: Final = "p2000"
LOGGER = logging.getLogger(__package__)

CONF_PROVINCE: Final = "province"

PROVINCES: Final = (
    "Drenthe",
    "Flevoland",
    "Friesland",
    "Gelderland",
    "Groningen",
    "Limburg",
    "Noord-Brabant",
    "Noord-Holland",
    "Overijssel",
    "Utrecht",
    "Zeeland",
    "Zuid-Holland",
)

ENTRY_TYPE_SERVICE: Final = "service"
#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search1.py

from googlemaps import GoogleMaps
address = '12642 Medford Road, Philadelphia, PA'
print GoogleMaps().address_to_latlng(address)

#!/usr/bin/python
# -*- coding: utf-8 -*-

#########################################################
#
# Alejandro German
# 
# https://github.com/seralexger/selenium-capturetraffic
#
#########################################################

from capturetraffic import CaptureTraffic


sniffer = CaptureTraffic()
data = sniffer.capture_traffic('https://www.airbnb.es/s/Mil%C3%A1n--Italia/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJ53USP0nBhkcRjQ50xhPN_zw&query=Mil%C3%A1n%2C%20Italia&map_toggle=true&allow_override%5B%5D=&s_tag=KmFXqfK_', save=True)
print(data)

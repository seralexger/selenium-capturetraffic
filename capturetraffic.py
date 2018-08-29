#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import time

from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class CaptureTraffic:

	'''
	Simple class to capture xhr requests of webpages and its responses, it's configure to capture http and https requests.
	'''

	server = None
	proxy = None
	proxy_port = None
	proxy_ip = None
	driver = None
	headers = { 
		    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
		}

	def __init__(self):

		self.start_session()

	

	def start_server(self):

		self.server = Server('browsermob-proxy-2.1.4/bin/browsermob-proxy')
		self.server.start()


	def start_driver(self):

		
		profile = webdriver.FirefoxProfile()
		profile.set_preference('network.proxy.ssl_port', int(self.proxy_port))
		profile.set_preference('network.proxy.ssl', self.proxy_ip)
		profile.set_preference('network.proxy.http_port', int(self.proxy_port))
		profile.set_preference('network.proxy.http', self.proxy_ip)
		profile.set_preference('network.proxy.type', 1)
		profile.set_preference('general.useragent.override', self.headers['User-Agent'])
		options = Options()
		options.add_argument('--headless')

		self.driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='utils/geckodriver')


	def start_session(self):

		self.start_server()
		self.proxy = self.server.create_proxy()
		self.proxy.new_har(options={'captureHeaders': True, 'captureContent': True, 'captureBinaryContent': True})
		self.proxy_port = self.proxy.proxy.split(':')[-1]
		self.proxy_ip = self.proxy.proxy.split(':')[0]
		self.start_driver()


	def stop_session(self):
		
		server.stop()
		driver.quit() 



	def capture_traffic(self, url, wait_time = 30, save = False, save_path = 'data/xhr_re.json'):
		'''
		time.sleep() can be replace for a wait function of Selenium webdriver.
		'''

		self.driver.get(url)
		time.sleep(wait_time)

		if save:
			if not os.path.exists('data'):
				os.makedirs('data')
			with open(save_path, 'w') as fp:
				json.dump(self.proxy.har, fp, indent = 4)

		return self.proxy.har



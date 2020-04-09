# -*- coding: utf-8 -*-
import sys
import importlib
import time

sys.path.append('plugins/')
PCRC = None
PREFIX = '!!PCRC'


def load_PCRC():
	global PCRC
	PCRC = importlib.import_module('PCRC-MCDR.PCRC')


def on_info(server, info):
	if info.is_user and info.content == '!!PCRC start':
		server.reply(info, 'Starting PCRC')
		if PCRC.is_working():
			server.reply(info, 'PCRC is already running!')
		else:
			PCRC.start()
	if info.source == 1 and info.content == '!!PCRC stop':
		if PCRC.is_working():
			PCRC.stop()
		else:
			server.reply(info, 'PCRC is not running!')


def on_load(server, old):
	global PCRC
	try:
		if old is not None and old.PCRC is not None and old.PCRC.is_working():
			PCRC = old.PCRC
		else:
			load_PCRC()
	except:
		load_PCRC()


def on_mcdr_stop(server):
	global PCRC
	if PCRC is None:
		return
	if PCRC.is_working():
		PCRC.stop()
	else:
		for i in range(600):
			if not PCRC.is_stopped():
				server.logger.info('Waiting for PCRC to stop')
				for i in range(10):
					if not PCRC.is_stopped():
						time.sleep(0.1)
		if not PCRC.is_stopped():
			server.logger.info('PCRC took too long to stop (more than 10min)! Exit anyway')

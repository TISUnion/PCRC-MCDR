# -*- coding: utf-8 -*-
import importlib
import time

from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'pcrc_mcdr',
    'version': '1.0.0',
    'name': 'PCRC MCDR',
    'description': 'a MCDR plugin wrapper for PCRC',
    'author': 'Fallen_Breath',
    'link': 'https://github.com/TISUnion/PCRC-MCDR'
}

PCRC = None
PREFIX = '!!PCRC'

# 0=guest 1=user 2=helper 3=admin
Permission = 1


def permission_check(server, info, perm):
    if info.is_user:
        if info.source == 1:
            return True
        elif server.get_permission_level(info) >= perm:
            return True
    return False


def load_PCRC():
    global PCRC
    PCRC = importlib.import_module('PCRC-MCDR.PCRC')


@new_thread('PCRC-MCDR')
def on_user_info(server, info):
    if PCRC is not None:
        if permission_check(server, info, Permission) and info.content == '!!PCRC start':
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


def stopping(server):
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


def on_mcdr_stop(server):
    stopping(server)


@new_thread('PCRC-MCDR')
def on_remove(server):
    stopping(server)

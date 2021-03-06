#! /usr/bin/python3
# -*- coding:utf-8 -*-
import csv
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

filename = 'data'

def filename_check(filename=None):
    """
    :type filename: str
    :rtype: bool
    """
    if filename is None:
        logger.debug("None file")
        return False
    return True

def open_csv(filename=None, opentype='r'):
    """
    :type filename: str
    :type opentype: str
        read    -> 'r'
        write   -> 'w'
        append  -> 'a'
    :rtype: fileobject
    """
    if not filename_check(filename=filename):
        return
    return open(filename+'.csv', opentype)


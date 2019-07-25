# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

APY_KEY = '95b4b2df9c92207e52d472b1b66db8c8'
APP_ID = "VCOJEYD2PO"
INDEX = 'products'

def update(request):
    logging.debug("method: update: " + str(request))

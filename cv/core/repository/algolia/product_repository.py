# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def update(request):
    logging.debug("method: update: " + str(request))

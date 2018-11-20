# -*- coding: utf-8 -*-
import os

# Constantes.

ORACLE_USER = "delivery"
ORACLE_PASS = "Farmat0d0"
ORACLE_DSN = "10.232.8.3/delivery"

# oracle client
os.chdir(os.path.dirname(__file__))
ORACLE_CLIENT = str("C:\Oracle\instantclient_12_2")

# QUERIES ORACLE
SQL_GET_PAYMENT_METHODS = """SELECT ID, DESCRIPTION, IMAGE_URL, POSITION_INDEX, CREDIT_CARD, STATUS FROM BDOM.PAYMENT_MEANS"""
SQL_GET_CONFIGURATION_PROPERTIES = """SELECT KEYY, VALUE2, DESCRIPTION, ACTIVE FROM DELIVERY_PROPERTY"""
SQL_GET_STORE_STOCK = """SELECT I.ID, SS.STORE_ID, SS.FULL_PRICE, SS.STOCK
                        FROM BDOS.ITEM I
                        INNER JOIN BDOS.STORE_STOCK SS ON (I.ID = SS.ITEM)
                        WHERE I.STATUS<>'E'
                          AND I.STATUS<>'X'
                          AND I.ID IN (1051510)
                          AND SS.STORE_ID IN (26, 53, 83, 1000, 1001) """

# APIS
# CV API 3.0...
URL_BASE = 'https://sandbox-dot-services-dot-integracion-retail-colombia.appspot.com/_ah/api/'
URL_API_CREATE_CONFIGURATION_PROPERTY = str(URL_BASE) + str('configuration/v1/property')
URL_API_CREATE_PAYMENT_METHOD = str(URL_BASE) + str('datafoundation/v1/paymentmethod')
URL_API_SAVE_STORE_STOCK = 'https://stock-update-endpoint-dot-sandbox-domicilios-farmatodo.appspot.com/_ah/api/stockEndpoint/v1/item/stock/price/update'

# Algolia API
APY_KEY = '95b4b2df9c92207e52d472b1b66db8c8'
APP_ID = "VCOJEYD2PO"
INDEX = 'products'

# TELEGRAM API
ID_CHANNEL_TELEGRAM = "-1001125408652"
TOKEN_TELEGRAM_BOT = "555831688:AAEKbvH8i87QAmdn-51VwcEEYhDKeqOimZo"
URL_TELEGRAM = "https://api.telegram.org/bot"
API_TELEGRAM_SEND_MSG = str(URL_TELEGRAM) + str(TOKEN_TELEGRAM_BOT) + "/sendMessage"

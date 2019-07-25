# -*- coding: utf-8 -*-
import os

import cx_Oracle

os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
os.chdir(os.path.dirname(__file__))
ORACLE_CLIENT = str("C:\Oracle\instantclient_12_2")

ORACLE_USER = "delivery"
ORACLE_PASS = "Farmat0d0"
ORACLE_DSN = "10.232.8.3/delivery"

# QUERIES ORACLE
SQL_GET_ORDERS_TO_SEND_TO_SIM = """ SELECT DISTINCT (ORDER_ID) 
                                    FROM BDOM.ORDER_SIM_LOG 
                                    WHERE 0=0 
                                        --AND STATUS IN ('ERROR') 
                                        AND ORDER_ID IN (5101527)"""
SQL_GET_ORDERS_TO_SEND_TO_RMS = """ SELECT DISTINCT (ORDER_ID) 
                                    FROM BDOM.ORDER_RMS_LOG 
                                    WHERE 0=0 
                                        --AND STATUS IN ('ERROR') 
                                        AND ORDER_ID IN (5101527)"""
SQL_GET_PAYMENT_METHODS = """SELECT ID, DESCRIPTION, IMAGE_URL, POSITION_INDEX, CREDIT_CARD, STATUS FROM BDOM.PAYMENT_MEANS"""
SQL_GET_CONFIGURATION_PROPERTIES = """SELECT KEYY, VALUE2, DESCRIPTION, ACTIVE FROM DELIVERY_PROPERTY"""
SQL_GET_STORE_STOCK = """SELECT I.ID, SS.STORE_ID, SS.FULL_PRICE, SS.STOCK
                        FROM BDOS.ITEM I
                        INNER JOIN BDOS.STORE_STOCK SS ON (I.ID = SS.ITEM)
                        WHERE I.STATUS<>'E'
                          AND I.STATUS<>'X'
                          AND I.ID IN (1051510)
                          AND SS.STORE_ID IN (26, 53, 83, 1000, 1001) """

# examples in https://github.com/oracle/python-cx_Oracle

def connect():
    os.chdir(ORACLE_CLIENT)
    conn = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASS, dsn=ORACLE_DSN)
    return conn


def executeQuery(sql):
    con = connect()
    cursor = con.cursor()
    res = cursor.execute(sql).fetchall()
    con.close()
    return res


def exe_update_new_item_status(item, status):
    con = connect()
    cur = con.cursor()
    statement = 'update BDOS.LOG_NEW_ITEM set UPLOADED = :1 where ITEM = :2'
    cur.execute(statement, (status, item))
    con.commit()
    con.close()


def exe_update_updated_item_status(item, status):
    con = connect()
    cur = con.cursor()
    statement = 'update BDOS.log_updated_item set UPLOADED = :1 where ITEM = :2'
    cur.execute(statement, (status, item))
    con.commit()
    con.close()

# -*- coding: utf-8 -*-
import os

import cx_Oracle
# examples in https://github.com/oracle/python-cx_Oracle

os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
os.chdir(os.path.dirname(__file__))
ORACLE_CLIENT = str("C:\Oracle\instantclient_12_2")

ORACLE_USER = "delivery"
ORACLE_PASS = "Farmat0d0"
ORACLE_DSN = "10.232.8.3/delivery"


def connect():
    os.chdir(ORACLE_CLIENT)
    conn = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASS, dsn=ORACLE_DSN)
    return conn


def get_orders_to_send_to_rms():
    query = """ SELECT DISTINCT (ORDER_ID) 
                FROM BDOM.ORDER_RMS_LOG 
                WHERE 0=0 
                    --AND STATUS IN ('ERROR') 
                    AND ORDER_ID IN (5101527)"""
    con = connect()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res


def get_orders_to_send_to_sim():
    query = """ SELECT DISTINCT (ORDER_ID) 
                FROM BDOM.ORDER_SIM_LOG 
                WHERE 0=0 
                    --AND STATUS IN ('ERROR') 
                    AND ORDER_ID IN (5101527)"""
    con = connect()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res


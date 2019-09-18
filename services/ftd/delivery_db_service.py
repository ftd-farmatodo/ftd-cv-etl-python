# -*- coding: utf-8 -*-
import os

import cx_Oracle

# examples in https://github.com/oracle/python-cx_Oracle

os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
os.chdir(os.path.dirname(__file__))

ORACLE_CLIENT = str('C:\Oracle\instantclient_12_2')
ORACLE_USER = "delivery"
ORACLE_PASS = "Farmat0d0"
# ORACLE_DSN = "10.193.0.10/delivery"
# ORACLE_DSN = "10.232.8.3/delivery"
ORACLE_DSN = "10.193.0.3/delivery"


def connect():
    os.chdir(ORACLE_CLIENT)
    conn = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASS, dsn=ORACLE_DSN)
    return conn


def get_orders_to_send_to_rms():
    # return [[6608825]]
    query = """ SELECT DISTINCT ( ORL.order_id ) ,ORL.STATUS
                FROM   bdom.ORDER_RMS_LOG ORL
                       INNER JOIN (
                                    SELECT
                                      ROW_NUMBER() OVER ( partition BY ORL_T.order_id ORDER BY ORL_T.id DESC) I,
                                      ORL_T.order_id,
                                      ORL_T.status
                                    FROM   bdom.ORDER_RMS_LOG ORL_T
                                    ORDER  BY ORL_T.order_id
                                  ) LAST_STATUS
                         ON ORL.order_id = LAST_STATUS.order_id
                            AND LAST_STATUS.i = 1
                            AND LAST_STATUS.status IN ( 'ERROR', 'EXHAUSTED_ATTEMPSTS', 'DISABLED' )
                            AND ORL.status = LAST_STATUS.status
                ORDER  BY ORL.order_id"""
    con = connect()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res


def get_orders_to_send_to_sim():
    # return [[6608825]]
    query = """ SELECT DISTINCT ( OSL.order_id ) ,OSL.STATUS
                FROM   bdom.ORDER_SIM_LOG OSL
                       INNER JOIN (
                                    SELECT
                                      ROW_NUMBER() OVER ( partition BY OSL_T.order_id ORDER BY OSL_T.id DESC) I,
                                      OSL_T.order_id,
                                      OSL_T.status
                                    FROM   bdom.ORDER_SIM_LOG OSL_T
                                    ORDER  BY OSL_T.order_id
                                  ) LAST_STATUS
                         ON OSL.order_id = LAST_STATUS.order_id
                            AND LAST_STATUS.i = 1
                            AND LAST_STATUS.status IN ( 'ERROR', 'EXHAUSTED_ATTEMPSTS', 'DISABLED' )
                            AND OSL.status = LAST_STATUS.status
                ORDER  BY OSL.order_id"""
    con = connect()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res

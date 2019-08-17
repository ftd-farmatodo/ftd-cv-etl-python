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
    return [[6608825]]
    # query = """ SELECT DISTINCT (ORDER_ID)
    #             FROM BDOM.ORDER_RMS_LOG
    #             WHERE 0=0
    #                 --AND STATUS IN ('ERROR')
    #                 AND ORDER_ID IN (5101527)"""
    # con = connect()
    # cursor = con.cursor()
    # res = cursor.execute(query).fetchall()
    # con.close()
    # return res


def get_orders_to_send_to_sim():
    # return [[6608825],[6628250],[6721144],[6558629],[6552674],[6656303],[6538171],[6591795],[6726869],[6623239],[6572228],[6603300],[6570760],[6625779],[6538171],[6561210],[6715689],[6520081],[6721633],[6609608],[6682530],[6522244],[6604912],[6601962],[6565727],[6562113],[6613387],[6494695],[6618333],[6726816],[6726866],[6453862],[6608672],[6542380],[6624867],[6560374],[6567923],[6556086],[6632317],[6526741],[6643233],[6570582],[6627992],[6607526],[6613438],[6597145],[6427901],[6624091],[6427972],[6719316],[6726829],[6478587],[6608225],[6419248],[6561210],[6556086],[6602445],[6726848],[6458898],[6498300],[6726894]]
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
                            AND LAST_STATUS.status IN ( 'ERROR', 'EXHAUSTED_ATTEMPSTS' )
                            AND OSL.status = LAST_STATUS.status
                ORDER  BY OSL.order_id"""
    con = connect()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res

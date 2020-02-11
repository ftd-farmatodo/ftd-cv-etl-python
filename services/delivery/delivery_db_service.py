# -*- coding: utf-8 -*-
import os

import cx_Oracle

# examples in https://github.com/oracle/python-cx_Oracle

os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
os.chdir(os.path.dirname(__file__))

ORACLE_CLIENT = str('C:\Oracle\instantclient_12_2')
ORACLE_USER = "delivery"
ORACLE_PASS = "Farmat0d0"
# ORACLE_DSN = "10.193.0.10/delivery"  # develop
ORACLE_DSN = "10.232.8.3/delivery"  # sandbox
# ORACLE_DSN = "10.193.0.3/delivery"  # production


def connect():
    os.chdir(ORACLE_CLIENT)
    conn = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASS, dsn=ORACLE_DSN)
    return conn


def get_orders_to_send_to_rms():
    # return [[6783292]]
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
    # return [[6783292]]
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


def get_customers_20_to_send_to_atom():
    # return [[24030]]
    query = """ SELECT ID FROM BDUCD.CUSTOMER WHERE ATOM_ID IS NULL AND ROWNUM <= 10000 """
    con = connect()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res


def get_stores():
    # return [[24030]]
    query = """ SELECT ID, OR_ID FROM BDOS.STORE WHERE OR_ID IS NOT NULL ORDER BY ID ASC """
    con = connect()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res


def update_store_stock_full_price(store_id, item_id, full_price):
    try:
        statement = """UPDATE BDOS.STORE_STOCK SET FULL_PRICE = :fullPrice WHERE STORE_ID = :store_id AND ITEM = :item_id"""
        con = connect()
        cur = con.cursor()
        cur.execute(statement, (full_price, store_id, item_id))
        con.commit()
        con.close()
        return True
    except Exception as e:
        print("Error al ejecutar insert con parametros -> " + e)
        return False


def update_store_stock_stock(store_id, item_id, stock):
    try:
        statement = """UPDATE BDOS.STORE_STOCK SET STOCK = :stock WHERE STORE_ID = :store_id AND ITEM = :item_id"""
        con = connect()
        cur = con.cursor()
        cur.execute(statement, (stock, store_id, item_id))
        con.commit()
        con.close()
        return True
    except Exception as e:
        print("Error al ejecutar insert con parametros -> " + e)
        return False


def update_store_stock(store_id, item_id, stock, full_price):
    try:
        statement = """UPDATE BDOS.STORE_STOCK SET FULL_PRICE = :full_price, STOCK = :stock WHERE STORE_ID = :store_id AND ITEM = :item_id"""
        con = connect()
        cur = con.cursor()
        cur.execute(statement, (full_price, stock, store_id, item_id))
        con.commit()
        con.close()
        return True
    except Exception as e:
        print("Error al ejecutar insert con parametros -> " + e)
        return False

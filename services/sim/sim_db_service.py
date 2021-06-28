# -*- coding: utf-8 -*-
import os

import cx_Oracle

# examples in https://github.com/oracle/python-cx_Oracle
os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
os.chdir(os.path.dirname(__file__))

ORACLE_USER_COL = "sim"
ORACLE_PASS_COL = "retail16FTD"
ORACLE_DSN_COL = "sim-scan0-co.farmatodo.com:1521/SIM_SERVICE"

ORACLE_USER_Vzl = "sim"
ORACLE_PASS_Vzl = "retail16FTD"
ORACLE_DSN_Vzl = "sim-scan0-co.farmatodo.com:1521/SIM_SERVICE"



def connect_col():
    conn = cx_Oracle.connect(user=ORACLE_USER_COL, password=ORACLE_PASS_COL, dsn=ORACLE_DSN_COL)
    return conn

def connect_vzl():
    conn = cx_Oracle.connect(user=ORACLE_USER_Vzl, password=ORACLE_PASS_Vzl, dsn=ORACLE_DSN_Vzl)
    return conn


def get_orders_to_send_to_sim_col():
    #return [[10746021],[10729839],[10760348]]
    query = """select distinct cust_order_id, external_id, TRANSACTION_EXTENDED_ID, transaction_date_time
                from pos_Transaction pt, pos_transaction_log l
                where processing_status = 2
                 and not exists (select 1 from ful_ord fo where fo.cust_order_id = pt.cust_order_id)
                  -- and trunc(transaction_Date_time)<> trunc(sysdate) -- todas las ordenes desde el inicio
                  -- and transaction_Date_time between TRUNC(SYSDATE-1) and TRUNC(SYSDATE) -- ordenes del dia anterior
                 and trunc(transaction_Date_time) >= TRUNC(SYSDATE-2) -- ordenes del dia
                  --and transaction_Date_time between to_date('01/11/2020', 'dd/mm/yyyy') and to_date('03/11/2020' ,'dd/mm/yyyy') -- ordenes para un rango de fecha especifico
                  and pt.id = l.transaction_id
                  and l.MESSAGE like 'Invalid customer order ID or invalid customer order state for intended action.'"""
    con = connect_col()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res

def get_orders_to_send_to_sim_vzl():
    #return [[10746021],[10729839],[10760348]]
    query = """ select distinct cust_order_id, external_id, TRANSACTION_EXTENDED_ID, transaction_date_time
                from sim.pos_transaction pt, sim.pos_transaction_log l
                where processing_status = 2
                  and not exists (select 1 from sim.ful_ord fo where fo.cust_order_id = pt.cust_order_id)
                  -- and trunc(transaction_Date_time)<> trunc(sysdate) -- todas las ordenes desde el inicio
                  -- and transaction_Date_time between to_date('23/03/2020', 'dd/mm/yyyy') and to_date('06/04/2020' ,'dd/mm/yyyy') -- ordenes para un rango de fecha especifico
                  -- and transaction_Date_time between TRUNC(SYSDATE-7) and TRUNC(SYSDATE) -- ordenes del dia anterior
                  and transaction_Date_time > TRUNC(SYSDATE-7) -- desde x dias atras, hasha hoy
                  and pt.id = l.transaction_id
                  and l.MESSAGE like 'Invalid customer order ID or invalid customer order state for intended action.' """

    con = connect_vzl()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res

# -*- coding: utf-8 -*-
import os

import cx_Oracle

# examples in https://github.com/oracle/python-cx_Oracle

os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
os.chdir(os.path.dirname(__file__))

#ORACLE_CLIENT = str('C:\Oracle\instantclient_12_2')
ORACLE_CLIENT = str("E:\gcloud_repository\CronsPython\datasources\instantclient_12_2") #En el servidor de ETL
#ORACLE_CLIENT = str("H:\Intraron\Proyectos\Py\Tareas\CronsPython\datasources\instantclient_12_2") #En mi maquina
ORACLE_USER = "sim"
ORACLE_PASS = "retail16FTD"
ORACLE_DSN = "sim-scan0-co.farmatodo.com:1521/SIM_SERVICE"


def connect():
    os.chdir(ORACLE_CLIENT)
    conn = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASS, dsn=ORACLE_DSN)
    return conn


def get_orders_to_send_to_sim():
    # return [[7072305]]
    query = """ select distinct cust_order_id, external_id, TRANSACTION_EXTENDED_ID, transaction_date_time
                from pos_Transaction pt, pos_transaction_log l
                where processing_status = 2
                  and not exists (select 1 from ful_ord fo where fo.cust_order_id = pt.cust_order_id)
                  -- and trunc(transaction_Date_time)<> trunc(sysdate) -- todas las ordenes desde el inicio
                  and transaction_Date_time between TRUNC(SYSDATE-2) and TRUNC(SYSDATE-1) -- ordenes del dia anterior
                  -- and transaction_Date_time between to_date('23/03/2020', 'dd/mm/yyyy') and to_date('06/04/2020' ,'dd/mm/yyyy') -- ordenes para un rango de fecha especifico
                  and pt.id = l.transaction_id
                  and l.MESSAGE like 'Invalid customer order ID or invalid customer order state for intended action.' """
    con = connect()
    cursor = con.cursor()
    res = cursor.execute(query).fetchall()
    con.close()
    return res

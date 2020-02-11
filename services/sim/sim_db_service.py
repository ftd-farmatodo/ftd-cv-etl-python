# -*- coding: utf-8 -*-
import os

import cx_Oracle

# examples in https://github.com/oracle/python-cx_Oracle

os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
os.chdir(os.path.dirname(__file__))

ORACLE_CLIENT = str('C:\Oracle\instantclient_12_2')
ORACLE_USER = "sim"
ORACLE_PASS = "retail16FTD"
ORACLE_DSN = "sim-scan0-co.farmatodo.com:1521/SIM_SERVICE"


def connect():
    os.chdir(ORACLE_CLIENT)
    conn = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASS, dsn=ORACLE_DSN)
    return conn


def get_orders_to_send_to_sim():
    return [[7072305], [7096703], [6453862], [6526741], [6556086], [6561210], [6618333], [6682530], [6835323],
            [6880346], [6943199], [6983061], [6983007], [6982948], [6983046], [6992182], [7002920], [7004578],
            [7072287], [7072210], [7096450], [7096632], [7096545], [7096555], [7096614], [7096538], [7096741],
            [7096666], [7096768], [7096795], [7096679], [7096615], [7096695], [7096693], [7096669], [7096518],
            [7096697], [7096516], [7096647], [7096652], [7104458], [7194841], [7230524], [7230699], [7230602],
            [7230694], [7230636], [7235997], [7236130], [7096760], [6427972], [6520081], [6560374], [6608672],
            [6624867], [6753014], [6882930], [6911435], [6927278], [6977560], [6983042], [6983036], [7065195],
            [7068055], [7072178], [7072258], [7072233], [7077031], [7077057], [7077129], [7096718], [7096690],
            [7096786], [7096581], [7096619], [7096734], [7096844], [7096839], [7096727], [7096633], [7096254],
            [7096491], [7096775], [7096685], [7096311], [7096635], [7096504], [7096772], [7096755], [7096461],
            [7096618], [7096740], [7096616], [7230726], [7230504], [7230739], [7230647], [7230703], [7230675],
            [7230753]]
    # query = """ select distinct cust_order_id, external_id, TRANSACTION_EXTENDED_ID, transaction_date_time
    #             from pos_Transaction pt, pos_transaction_log l
    #             where processing_status = 2
    #               and not exists
    #                 (select 1 from ful_ord fo where fo.cust_order_id = pt.cust_order_id)
    #               and trunc(transaction_Date_time)<> trunc(sysdate)
    #               and pt.id = l.transaction_id
    #               and l.MESSAGE like 'Invalid customer order ID or invalid customer order state for intended action.' """
    # con = connect()
    # cursor = con.cursor()
    # res = cursor.execute(query).fetchall()
    # con.close()
    # return res

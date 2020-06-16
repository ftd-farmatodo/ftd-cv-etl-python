# -*- coding: utf-8 -*-
import os

import cx_Oracle

# examples in https://github.com/oracle/python-cx_Oracle
os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
os.chdir(os.path.dirname(__file__))

ORACLE_CLIENT = str('C:\Oracle\instantclient_12_2')

# QA Enviroment
ORACLE_USER = "UTILITY"
ORACLE_PASS = "FTDts16r"
ORACLE_DSN = "fts-scan3.farmatodo.com:1521/ftsqaco"


def get_connection():
    os.chdir(ORACLE_CLIENT)
    conn = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASS, dsn=ORACLE_DSN)
    return conn


def get_location_mapping(connection):
    query = """ SELECT * FROM UTILITY.STORE_ZONE_DIGITAL_MEDIA """
    cursor = connection.cursor()
    res = cursor.execute(query).fetchall()
    connection.close()
    return res


def insert_location_mapping(connection, source, target):
    statement = """INSERT INTO UTILITY.STORE_ZONE_DIGITAL_MEDIA (SOURCE, TARGET) VALUES  (:source, :target) """
    cur = connection.cursor()
    cur.execute(statement, (source, target))
    return True

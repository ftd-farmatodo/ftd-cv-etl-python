# -*- coding: utf-8 -*-
import os

import cx_Oracle

os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
from cv.core.common import constants


# constants = importlib.machinery.SourceFileLoader('constants', 'E:\gcloud_repository\CronsPython\common/constants.py').load_module()

# examples in https://github.com/oracle/python-cx_Oracle

def connOracle():
    os.chdir(constants.ORACLE_CLIENT)
    conn = cx_Oracle.connect(user=constants.ORACLE_USER, password=constants.ORACLE_PASS, dsn=constants.ORACLE_DSN)
    return conn


def exeQuery(sql):
    con = connOracle()
    cursor = con.cursor()
    res = cursor.execute(sql).fetchall()
    con.close()
    return res


def exe_update_new_item_status(item, status):
    con = connOracle()
    cur = con.cursor()
    statement = 'update BDOS.LOG_NEW_ITEM set UPLOADED = :1 where ITEM = :2'
    cur.execute(statement, (status, item))
    con.commit()
    con.close()


def exe_update_updated_item_status(item, status):
    con = connOracle()
    cur = con.cursor()
    statement = 'update BDOS.log_updated_item set UPLOADED = :1 where ITEM = :2'
    cur.execute(statement, (status, item))
    con.commit()
    con.close()

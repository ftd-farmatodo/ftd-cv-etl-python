# -*- coding: utf-8 -*-
import json
import logging
import os
import requests
import cx_Oracle


logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

os.environ["NLS_LANG"] = "SPANISH_COLOMBIA.AL32UTF8"
os.chdir(os.path.dirname(__file__))

#ORACLE_CLIENT = str('C:\Oracle\instantclient_12_2')
ORACLE_CLIENT = str("E:\gcloud_repository\CronsPython\datasources\instantclient_12_2") #En el Servidor
#ORACLE_CLIENT = str("H:\Intraron\Proyectos\Py\Tareas\CronsPython\datasources\instantclient_12_2") #En mi maquina
ORACLE_USER = "delivery"
ORACLE_PASS = "Farmat0d0"
# ORACLE_DSN = "10.193.0.10/delivery"
# ORACLE_DSN = "10.232.8.3/delivery"
ORACLE_DSN = "10.193.0.3/delivery"

# CORE2_DELIVERY_BASE_URL = 'http://localhost:7001/DeliveryWS'
# CORE2_DELIVERY_BASE_URL = 'http://10.193.0.9:11103/DeliveryWS'
# CORE2_DELIVERY_BASE_URL = 'http://10.232.8.2:11103/DeliveryWS'
CORE2_DELIVERY_BASE_URL = 'http://10.193.0.2:11103/DeliveryWS'


def connect():
    os.chdir(ORACLE_CLIENT)
    conn = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASS, dsn=ORACLE_DSN)
    return conn


def send_order_to_sim(request):
    logging.debug("method: send_order_to_sim() -> Request: " + str(request))
    try:
        url = CORE2_DELIVERY_BASE_URL + '/v1/order/sendOrderToSIM'
        logging.debug("method: send_order_to_sim() -> URL Service: " + url)
        response = requests.post(url, data=json.dumps(request), headers={'content-type': 'application/json'})
        logging.debug("method: sen_order_to_sim() -> Response: " + json.dumps(response.json()))
        return response.json()
    except Exception as ex:
        logging.exception(ex)
        return json.dumps({
            "code": "Exception",
            "message": ex.message
        })


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


tracing = []

# consultar las ordenes que se deben reimpulsar a SIM
rows = get_orders_to_send_to_sim()
logging.info("# de ordenes: " + str(len(rows)))

for count, row in enumerate(rows):
    try:
        request = {
            "orderId": row[0],
            "skipAttemptsValidation":  True
        }
        response = send_order_to_sim(request)
        record = {
            "orderId": row[0],
            "code":  response['code'],
            "message": response['message']
        }
        logging.info(json.dumps(record))
        tracing.append(record)
    except Exception as ex:
        logging.exception(ex)

# logging.info(tracing)

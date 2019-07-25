# -*- coding: utf-8 -*-
import logging
from multiprocessing import Pool

from services.deliverydb import delivery_db_service as ds
from services.datastore import datastore_builder
from services.datastore.datafoundation import store_stock_repository

# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log')
# create logger
logger = logging.getLogger('upload_stock_task')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

if __name__ == '__main__':

    algolia_pool = Pool(5)
    datastore_pool = Pool(5)

    # file = [[1, 1, 6], [1, 2, 3], [1, 3, 0], [1, 4, 1], [1, 5, 2], [2, 5, 2]]
    file = ds.executeQuery(ds.SQL_GET_STORE_STOCK)

    items = {}

    # logging.info("construir diccionario donde la llave es el id del item y el valor es un listado de store_stock")

    for row in file:
        store_stock = []
        item = row[0]
        json = {
            "item_id": row[0],
            "store_id": row[1],
            "full_price": row[2],
            "stock": row[3]
        }
        if items.get(item) is not None:
            store_stock = items.get(item)
        items[item] = store_stock
        store_stock.append(json)
        # logging.info(items)

    # list1 = algolia_util.build_algolia_request(items)
    # logging.info(list1)
    list2 = datastore_builder.build_datastore_request(items)
    # logging.info(list2)
    # algolia_pool.map(product_repository.update, list1)
    datastore_pool.map(store_stock_repository.update, list2)

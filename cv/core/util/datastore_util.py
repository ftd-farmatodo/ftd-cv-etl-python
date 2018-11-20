# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def build_datastore_request(dictionary):
    count = 0
    records = []
    # logging.debug("key in etl.iterkeys()")
    for key in dictionary:
        # logging.debug(key)
        children = []
        values = dictionary[key]
        # logging.debug(values)
        for value in values:
            # logging.debug(value)
            # logging.info("contruir request para datastore")
            store_stock = {
                'storeGroupId': value["store_id"],
                'fullPrice': value["full_price"],
                "stock": value["stock"]
            }
            # logging.debug(store_stock)
            children.append(store_stock)
        record = {
            "item": key,
            "storeInformation": children
        }
        # logging.debug(record)
        records.append(record)
        count = count + 1
    logging.debug("# de registros a actualizar en el datastore: [%s]", count)
    return records

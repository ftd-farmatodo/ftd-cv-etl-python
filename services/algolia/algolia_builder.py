# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def build_algolia_request(dictionary):
    count = 0
    records = []
    # logging.debug("value in etl.itervalues()")
    for value in dictionary.itervalues():
        # logging.debug(value)
        for record in value:
            # logging.info("contruir request para algolia")
            request = {
                "objectID": str(record["item_id"]) + str(record["store_id"]),
                "fullPrice": record["full_price"],
                "stock": record["stock"],
                "offerText": record["offer_text"],
                "offerDescription": record["offer_description"],
                "offerPrice": record["offer_price"]
            }
            # logging.debug(request)
            records.append(request)
            count = count + 1
    logging.debug("# de registros a actualizar en algolia: [%s]", count)
    return records

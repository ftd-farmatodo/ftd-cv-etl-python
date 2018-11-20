# -*- coding: utf-8 -*-
import logging
from multiprocessing import Pool

from cv.core.common import constants
from cv.core.datasources import connectionBD as ds
from cv.core.repository.datastore.datafoundation import payment_method_repository

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

if __name__ == '__main__':

    pool = Pool(5)

    rows = ds.exeQuery(constants.SQL_GET_PAYMENT_METHODS)

    records = []

    for count, row in enumerate(rows):
        payment_method = {
            "id": row[0],
            "description": row[1],
            "imageURL": row[2],
            "index": int(row[3]),
            "creditCard": bool(row[4]),
            "status": bool(row[5])
        }
        logging.info(payment_method)
        records.append(payment_method)

    logging.info(records)
    pool.map(payment_method_repository.save, records)

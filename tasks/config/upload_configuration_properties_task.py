# -*- coding: utf-8 -*-
import logging
from multiprocessing import Pool

from services.deliverydb import delivery_db_service as ds
from services.datastore.config import configuration_property_repository

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

if __name__ == '__main__':

    pool = Pool(5)

    rows = ds.executeQuery(ds.SQL_GET_CONFIGURATION_PROPERTIES)

    records = []

    for count, row in enumerate(rows):
        configuration_property = {
            "id": str(row[0]),
            "value": str(row[1]),
            "description": str(row[2]),
            "active": bool(row[3])
        }

        logging.info(configuration_property)
        records.append(configuration_property)

    logging.info(records)
    pool.map(configuration_property_repository.save, records)
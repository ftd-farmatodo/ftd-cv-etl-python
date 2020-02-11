# -*- coding: utf-8 -*-
import logging

from services.delivery import delivery_db_service
from services.fts import fts_utility_service_db, fts_ftretail_service_db

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# consultar la configuracion actual
# mapping = fts_utility_service_db.get_location_mapping()
# logging.info("# of records: " + str(len(mapping)))
#
# for count, row in enumerate(mapping):
#     try:
#         logging.info(row)
#     except Exception as ex:
#         logging.exception(ex)


# consultar la configuracion actual
locations = delivery_db_service.get_stores()
logging.info("# of stores: " + str(len(locations)))

for count, row in enumerate(locations):
    try:
        logging.info(row)
        fts_utility_service_db.insert_location_mapping(1965, row[1])
    except Exception as ex:
        logging.exception(ex)

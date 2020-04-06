# -*- coding: utf-8 -*-
import logging

import xlrd

from services.delivery import delivery_db_service

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# Give the location of the file
loc = ("C:\Google\Drive\diego.poveda@farmatodo.com\DOMICILIOS\OR\ICO\STORE_STOCK_PRICE_MD.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
# For sheet 0
sheet = wb.sheet_by_index(0)
# For row 0 and column 0
sheet.cell_value(0, 0)
# logging.info(sheet.nrows)
# logging.info(sheet.ncols)

delivery_db_connection = delivery_db_service.get_connection()

for i in range(sheet.nrows):
    try:
        # logging.info(sheet.row_values(1))
        item = int(sheet.cell_value(i, 0))
        store = int(sheet.cell_value(i, 2))
        full_price = float(sheet.cell_value(i, 4))
        delivery_db_service.update_store_stock(delivery_db_connection, store, item, 100, full_price)
        logging.info("Row [" + str(i + 1) + "]: item: " + str(item) + ", store: " + str(store) + ", full_price: " + str(
            full_price) + ", stock: " + str(100))
        delivery_db_connection.commit()
    except Exception as ex:
        logging.exception(
            "Row [" + str(i + 1) + "]: item: " + str(item) + ", store: " + str(store) + ", full_price: " + str(
                full_price) + ", stock: " + str(100))
        delivery_db_connection.rollback()

delivery_db_connection.close()

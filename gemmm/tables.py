# -*- coding: utf-8 -*-

import pandas as pd
from importlib import resources as impresources
from . import data

table_path = impresources.files(data) / 'msoa_table.parquet'
msoa_lookup = pd.read_parquet(table_path)

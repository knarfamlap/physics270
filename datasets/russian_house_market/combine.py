#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

filenames = ['test.csv', 'train.csv']

combines_csv = pd.concat([pd.read_csv(f) for f in filenames]) 

combines_csv.to_csv('house.csv', index=False)

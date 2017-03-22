#!/usr/bin/env python
# -*- coding: utf_8 -*-

import xlrd
data = xlrd.open_workbook('D:\GitHub\python-Demo\卢虎.xlsx')
table = data.sheets()[0]
print table.cell_value(1, 0)

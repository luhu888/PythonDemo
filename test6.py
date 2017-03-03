#!/usr/bin/env python
# -*- coding: utf_8 -*-
import xlrd
data = xlrd.open_workbook('D:\GitHub\python-Demo\Â¬»¢.xlsx')
table = data.sheets()[0]
print table.cell_value(1, 0)
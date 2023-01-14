# -*- coding: utf-8 -*-
# @Time    : 1/14/2023 8:55 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Load.py
# @Software: PyCharm

import pandas as pd


class Load:

    def __init__(self, name, bus1, p, v):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v

        self.r = v ** 2 / p

        self.buses = [self.bus1]

    def calc_g(self):
        g = 1 / self.r
        g_df = pd.DataFrame()

        g_df.loc[self.bus1, self.bus1] = g

        self.g = g_df
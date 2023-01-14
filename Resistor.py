# -*- coding: utf-8 -*-
# @Time    : 1/14/2023 8:55 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Resistor.py
# @Software: PyCharm

import pandas as pd


class Resistor:

    def __init__(self, name, bus1, bus2, r):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r

        self.buses = [self.bus1, self.bus2]

    def calc_g(self):
        g = 1 / self.r

        g_df = pd.DataFrame()

        g_df.loc[self.bus1, self.bus1] = g
        g_df.loc[self.bus2, self.bus2] = g
        g_df.loc[self.bus1, self.bus2] = - g
        g_df.loc[self.bus2, self.bus1] = - g

        self.g = g_df

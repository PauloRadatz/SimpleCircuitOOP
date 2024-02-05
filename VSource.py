# -*- coding: utf-8 -*-
# @Time    : 1/14/2023 9:08 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : VSource.py
# @Software: PyCharm


class VSource:

    def __init__(self, name: str, bus1: str, v: float):
        self.name = name
        self.bus1 = bus1
        self.v = v
        self.buses = [self.bus1]
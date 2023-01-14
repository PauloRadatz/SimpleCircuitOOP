# -*- coding: utf-8 -*-
# @Time    : 1/14/2023 8:54 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Bus.py
# @Software: PyCharm


class Bus:

    counter = 0

    def __init__(self, name):
        self.name = name
        self.index = Bus.counter

        self.v = None

        Bus.counter = Bus.counter + 1

    def set_bus_v(self, bus_v):
        self.v = bus_v
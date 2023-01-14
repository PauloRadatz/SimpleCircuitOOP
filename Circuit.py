# -*- coding: utf-8 -*-
# @Time    : 1/14/2023 8:52 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Circuit.py
# @Software: PyCharm

from typing import Dict, List, Optional
from Bus import Bus
from Resistor import Resistor
from Load import Load
from VSource import VSource


class Circuit:

    def __init__(self, name: str):

        self.name: str = name

        self.buses_order: List[str] = list()
        self.buses: Dict[str, Bus] = dict()
        self.g_elements: Dict = dict()

        self.resistors: Dict[str, Resistor] = dict()
        self.loads: Dict[str, Load] = dict()
        self.vsource: Optional[VSource] = None

    def __add_bus(self, bus):
        if bus not in self.buses.keys():
            self.buses[bus] = Bus(bus)
            self.buses_order.append(bus)

    def set_bus_type(self, bus, bus_type):
        self.buses[bus].set_bus_type(bus_type)

    def add_resistor_element(self, name, bus1, bus2, r):

        self.resistors[name] = Resistor(name, bus1, bus2, r)
        self.resistors[name].calc_g()
        self.__add_bus(bus1)
        self.__add_bus(bus2)

        self.g_elements[name] = self.resistors[name]

    def add_load_element(self, name, bus1, p, v):

        self.loads[name] = Load(name, bus1, p, v)
        self.loads[name].calc_g()
        self.__add_bus(bus1)

        self.g_elements[name] = self.loads[name]

    def add_vsource_element(self, name, bus1, v):

        self.vsource = VSource(name, bus1, v)
        self.__add_bus(bus1)
        self.buses[bus1].set_bus_v(v)

    def print_nodal_voltage(self):
        for bus in self.buses_order:
            print(f"Bus = {bus} : voltage = {self.buses[bus].v}")
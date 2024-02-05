# -*- coding: utf-8 -*-
# @Time    : 1/14/2023 8:56 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Solution.py
# @Software: PyCharm

from Circuit import Circuit
import numpy as np


class Solution:

    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def build_g_matrix(self):
        self.g_matrix = np.zeros((len(self.circuit.buses), len(self.circuit.buses)))
        self.bus_order = list()

        for element_name, element in self.circuit.g_elements.items():

            for row in element.buses:
                for col in element.buses:
                    index_row = self.circuit.buses[row].index
                    index_col = self.circuit.buses[col].index

                    self.g_matrix[index_row, index_col] = self.g_matrix[index_row, index_col] + element.g.loc[row, col]


    def do_power_flow(self):
        self.build_g_matrix()

        # Implemented not a generic solution. It works only for a series circuit with a vsource, resistor, load
        # The implementation is not important as the idea of structure for the tool
        z_matrix = np.linalg.inv(self.g_matrix)
        i = self.circuit.vsource.v / z_matrix[0, 0]
        vb = z_matrix[1, 1] * i

        self.circuit.buses["B"].set_bus_v(vb)
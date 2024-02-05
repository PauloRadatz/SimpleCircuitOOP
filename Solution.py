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

        # Implemented a specific solution. It only works for a series circuit with a voltage source, resistor, and load.
        # The implementation details are not as crucial as the structural idea for the tool.
        self.g_matrix[0, 0] = self.circuit.g_elements["Rab"].g.loc["A", "A"]
        self.g_matrix[0, 1] = self.circuit.g_elements["Rab"].g.loc["A", "B"]
        self.g_matrix[1, 0] = self.circuit.g_elements["Rab"].g.loc["B", "A"]
        self.g_matrix[1, 1] = self.circuit.g_elements["Rab"].g.loc["B", "B"] + self.circuit.g_elements["Lb"].g.loc["B", "B"]


    def do_power_flow(self):
        self.build_g_matrix()

        # Implemented a specific solution. It only works for a series circuit with a voltage source, resistor, and load.
        # The implementation details are not as crucial as the structural idea for the tool.
        z_matrix = np.linalg.inv(self.g_matrix)
        i = self.circuit.vsource.v / z_matrix[0, 0]
        vb = z_matrix[1, 1] * i

        self.circuit.buses["B"].set_bus_v(vb)
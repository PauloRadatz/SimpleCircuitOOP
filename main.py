# -*- coding: utf-8 -*-
# @Time    : 1/14/2023 8:56 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : main.py
# @Software: PyCharm

from Circuit import Circuit
from Solution import Solution

# Defining my circuit
circuit_obj = Circuit("MySimpleCircuit")
circuit_obj.add_vsource_element(name="Va", bus1="A", v=100.0)
circuit_obj.add_resistor_element(name="Rab", bus1="A", bus2="B", r=5)
circuit_obj.add_load_element(name="Lb", bus1="B", p=2000.0, v=100.0)

# Simulating my circuit
solution_obj = Solution(circuit_obj)
solution_obj.do_power_flow()
circuit_obj.print_nodal_voltage()

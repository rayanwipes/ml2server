#!/usr/bin/env python3

from lifelines.datasets import load_waltons
from lifelines.datasets import load_dd
import matplotlib.pyplot as plt
import import_impl
import unittest
import os

from kaplan_meier import *


class kaplan_tests(unittest.TestCase):
    def test_waltons(self):
        df = load_waltons()
        # print("The data being analysed is as follows:")
        # print(df)
        duration_array = df['T']
        death_binary = df['E']
        kmf = kaplan_meier()
        kmf.fit(duration_array, death_binary)
        kmf.save_csv('waltons.csv')
        kmf.save_fig('waltons.png')

    def test_dd(self):
        df = load_dd()
        # print("The data being analysed is as follows:")
        # print(df)
        duration_array = df['duration']
        death_binary = df['observed']
        kmf = kaplan_meier()
        kmf.fit(duration_array, death_binary)
        kmf.save_csv('dd.csv')
        kmf.save_fig('dd.png')

    def test_regimes(self):
        df = load_dd()
        # print("The data being analysed is as follows:")
        # print(df)
        dem = (df["democracy"] == "Democracy")
        kmf = kaplan_meier()
        duration_array = df['duration']
        death_binary = df['observed']
        kmf.add_subplot()
        kmf.fit(duration_array[dem], death_binary[dem])
        kmf.fit(duration_array[~dem], death_binary[~dem])
        kmf.save_csv('combined.csv')
        kmf.save_fig("combined.png")


if __name__ == "__main__":
    unittest.main()

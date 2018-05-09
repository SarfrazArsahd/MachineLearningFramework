#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:48:09 2018

@author: sarfraz
"""

import unittest
from NeuralNetwork import *

class TestNeuralNetwork(unittest.TestCase):
    
    def test_NeuralNetwork(self):
        NN=NeuralNetwork()
        self.assertEqual(str(NN), "Neural Network")
                         


if __name__ == '__main__':
    unittest.main()
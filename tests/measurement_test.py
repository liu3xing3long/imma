#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

import unittest
import numpy as np

import imma.measure

class MeasurementTest(unittest.TestCase):

    def test_neigh_matrix(self):

        data = np.zeros((3, 4), dtype=int)
        data[:3, 1] = 1
        data[2:, 2] = 2
        data[0, 1:] = 3

        import imma.measure
        nbm = imma.measure.neighboor_matrix(data)
        nbm[1][0]
        self.assertEqual(nbm[1][0], nbm[0][1])
        self.assertEqual(nbm[3][0], nbm[0][3])

    def test_neigh_matrix_obj(self):

        data = np.zeros((3, 4), dtype=int)
        data[:3, 1] = 1
        data[2:, 2] = 2
        data[0, 1:] = 3
    #
        nbm = imma.measure.NeighboorMatrix(data)
        ndn = nbm.to_ndarray()
        sum = np.sum(ndn)
        sh = data.shape
        number_of_vertical_edges = 2 * 4
        number_of_horizontal_edges = 3 * 3
        self.assertEqual(sum, (number_of_horizontal_edges + number_of_vertical_edges) * 2)
        keys = nbm.keys()
        self.assertIn(0, keys)
        self.assertIn(1, keys)
        self.assertIn(2, keys)

        # print(nbm)
        # print data_out.shape
        # print data
        # print data_out
        # self.assertEquals(new_shape[0], data_out.shape[0])
        # self.assertEquals(new_shape[1], data_out.shape[1])
        # self.assertEquals(new_shape[2], data_out.shape[2])


if __name__ == "__main__":
    unittest.main()

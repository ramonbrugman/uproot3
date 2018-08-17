#!/usr/bin/env python

# Copyright (c) 2017, DIANA-HEP
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from collections import namedtuple
import unittest

import numpy

import uproot

class Test(unittest.TestCase):
    def runTest(self):
        pass

    def test_vector_of_numbers(self):
        branch = uproot.open("tests/samples/small-evnt-tree-fullsplit.root")["tree"]["StlVecU32"]
        a = branch.array()
        for i in range(100):
            self.assertEqual(a[i], [i] * (i % 10))

        branch = uproot.open("tests/samples/small-evnt-tree-fullsplit.root")["tree"]["StlVecF64"]
        a = branch.array()
        for i in range(100):
            self.assertEqual(a[i], [i] * (i % 10))

    def test_vector_of_vector_of_numbers(self):
        branch = uproot.open("tests/samples/vectorVectorDouble.root")["t"]["x"]
        self.assertEqual(branch.array().tolist(), [[], [[], []], [[10.0], [], [10.0, 20.0]], [[20.0, -21.0, -22.0]], [[200.0], [-201.0], [202.0]]])

    def test_strings1(self):
        tree = uproot.open("tests/samples/small-evnt-tree-fullsplit.root")["tree"]
        self.assertEqual(tree.array("Str").tolist(), [b'evt-000', b'evt-001', b'evt-002', b'evt-003', b'evt-004', b'evt-005', b'evt-006', b'evt-007', b'evt-008', b'evt-009', b'evt-010', b'evt-011', b'evt-012', b'evt-013', b'evt-014', b'evt-015', b'evt-016', b'evt-017', b'evt-018', b'evt-019', b'evt-020', b'evt-021', b'evt-022', b'evt-023', b'evt-024', b'evt-025', b'evt-026', b'evt-027', b'evt-028', b'evt-029', b'evt-030', b'evt-031', b'evt-032', b'evt-033', b'evt-034', b'evt-035', b'evt-036', b'evt-037', b'evt-038', b'evt-039', b'evt-040', b'evt-041', b'evt-042', b'evt-043', b'evt-044', b'evt-045', b'evt-046', b'evt-047', b'evt-048', b'evt-049', b'evt-050', b'evt-051', b'evt-052', b'evt-053', b'evt-054', b'evt-055', b'evt-056', b'evt-057', b'evt-058', b'evt-059', b'evt-060', b'evt-061', b'evt-062', b'evt-063', b'evt-064', b'evt-065', b'evt-066', b'evt-067', b'evt-068', b'evt-069', b'evt-070', b'evt-071', b'evt-072', b'evt-073', b'evt-074', b'evt-075', b'evt-076', b'evt-077', b'evt-078', b'evt-079', b'evt-080', b'evt-081', b'evt-082', b'evt-083', b'evt-084', b'evt-085', b'evt-086', b'evt-087', b'evt-088', b'evt-089', b'evt-090', b'evt-091', b'evt-092', b'evt-093', b'evt-094', b'evt-095', b'evt-096', b'evt-097', b'evt-098', b'evt-099'])

    def test_strings2(self):
        tree = uproot.open("tests/samples/small-evnt-tree-fullsplit.root")["tree"]
        self.assertEqual(tree.array("StdStr").tolist(), [b'std-000', b'std-001', b'std-002', b'std-003', b'std-004', b'std-005', b'std-006', b'std-007', b'std-008', b'std-009', b'std-010', b'std-011', b'std-012', b'std-013', b'std-014', b'std-015', b'std-016', b'std-017', b'std-018', b'std-019', b'std-020', b'std-021', b'std-022', b'std-023', b'std-024', b'std-025', b'std-026', b'std-027', b'std-028', b'std-029', b'std-030', b'std-031', b'std-032', b'std-033', b'std-034', b'std-035', b'std-036', b'std-037', b'std-038', b'std-039', b'std-040', b'std-041', b'std-042', b'std-043', b'std-044', b'std-045', b'std-046', b'std-047', b'std-048', b'std-049', b'std-050', b'std-051', b'std-052', b'std-053', b'std-054', b'std-055', b'std-056', b'std-057', b'std-058', b'std-059', b'std-060', b'std-061', b'std-062', b'std-063', b'std-064', b'std-065', b'std-066', b'std-067', b'std-068', b'std-069', b'std-070', b'std-071', b'std-072', b'std-073', b'std-074', b'std-075', b'std-076', b'std-077', b'std-078', b'std-079', b'std-080', b'std-081', b'std-082', b'std-083', b'std-084', b'std-085', b'std-086', b'std-087', b'std-088', b'std-089', b'std-090', b'std-091', b'std-092', b'std-093', b'std-094', b'std-095', b'std-096', b'std-097', b'std-098', b'std-099'])

    def test_strings3(self):
        tree = uproot.open("tests/samples/small-evnt-tree-fullsplit.root")["tree"]
        self.assertEqual(tree.array("StlVecStr").tolist(), [[], [b'vec-001'], [b'vec-002', b'vec-002'], [b'vec-003', b'vec-003', b'vec-003'], [b'vec-004', b'vec-004', b'vec-004', b'vec-004'], [b'vec-005', b'vec-005', b'vec-005', b'vec-005', b'vec-005'], [b'vec-006', b'vec-006', b'vec-006', b'vec-006', b'vec-006', b'vec-006'], [b'vec-007', b'vec-007', b'vec-007', b'vec-007', b'vec-007', b'vec-007', b'vec-007'], [b'vec-008', b'vec-008', b'vec-008', b'vec-008', b'vec-008', b'vec-008', b'vec-008', b'vec-008'], [b'vec-009', b'vec-009', b'vec-009', b'vec-009', b'vec-009', b'vec-009', b'vec-009', b'vec-009', b'vec-009'], [], [b'vec-011'], [b'vec-012', b'vec-012'], [b'vec-013', b'vec-013', b'vec-013'], [b'vec-014', b'vec-014', b'vec-014', b'vec-014'], [b'vec-015', b'vec-015', b'vec-015', b'vec-015', b'vec-015'], [b'vec-016', b'vec-016', b'vec-016', b'vec-016', b'vec-016', b'vec-016'], [b'vec-017', b'vec-017', b'vec-017', b'vec-017', b'vec-017', b'vec-017', b'vec-017'], [b'vec-018', b'vec-018', b'vec-018', b'vec-018', b'vec-018', b'vec-018', b'vec-018', b'vec-018'], [b'vec-019', b'vec-019', b'vec-019', b'vec-019', b'vec-019', b'vec-019', b'vec-019', b'vec-019', b'vec-019'], [], [b'vec-021'], [b'vec-022', b'vec-022'], [b'vec-023', b'vec-023', b'vec-023'], [b'vec-024', b'vec-024', b'vec-024', b'vec-024'], [b'vec-025', b'vec-025', b'vec-025', b'vec-025', b'vec-025'], [b'vec-026', b'vec-026', b'vec-026', b'vec-026', b'vec-026', b'vec-026'], [b'vec-027', b'vec-027', b'vec-027', b'vec-027', b'vec-027', b'vec-027', b'vec-027'], [b'vec-028', b'vec-028', b'vec-028', b'vec-028', b'vec-028', b'vec-028', b'vec-028', b'vec-028'], [b'vec-029', b'vec-029', b'vec-029', b'vec-029', b'vec-029', b'vec-029', b'vec-029', b'vec-029', b'vec-029'], [], [b'vec-031'], [b'vec-032', b'vec-032'], [b'vec-033', b'vec-033', b'vec-033'], [b'vec-034', b'vec-034', b'vec-034', b'vec-034'], [b'vec-035', b'vec-035', b'vec-035', b'vec-035', b'vec-035'], [b'vec-036', b'vec-036', b'vec-036', b'vec-036', b'vec-036', b'vec-036'], [b'vec-037', b'vec-037', b'vec-037', b'vec-037', b'vec-037', b'vec-037', b'vec-037'], [b'vec-038', b'vec-038', b'vec-038', b'vec-038', b'vec-038', b'vec-038', b'vec-038', b'vec-038'], [b'vec-039', b'vec-039', b'vec-039', b'vec-039', b'vec-039', b'vec-039', b'vec-039', b'vec-039', b'vec-039'], [], [b'vec-041'], [b'vec-042', b'vec-042'], [b'vec-043', b'vec-043', b'vec-043'], [b'vec-044', b'vec-044', b'vec-044', b'vec-044'], [b'vec-045', b'vec-045', b'vec-045', b'vec-045', b'vec-045'], [b'vec-046', b'vec-046', b'vec-046', b'vec-046', b'vec-046', b'vec-046'], [b'vec-047', b'vec-047', b'vec-047', b'vec-047', b'vec-047', b'vec-047', b'vec-047'], [b'vec-048', b'vec-048', b'vec-048', b'vec-048', b'vec-048', b'vec-048', b'vec-048', b'vec-048'], [b'vec-049', b'vec-049', b'vec-049', b'vec-049', b'vec-049', b'vec-049', b'vec-049', b'vec-049', b'vec-049'], [], [b'vec-051'], [b'vec-052', b'vec-052'], [b'vec-053', b'vec-053', b'vec-053'], [b'vec-054', b'vec-054', b'vec-054', b'vec-054'], [b'vec-055', b'vec-055', b'vec-055', b'vec-055', b'vec-055'], [b'vec-056', b'vec-056', b'vec-056', b'vec-056', b'vec-056', b'vec-056'], [b'vec-057', b'vec-057', b'vec-057', b'vec-057', b'vec-057', b'vec-057', b'vec-057'], [b'vec-058', b'vec-058', b'vec-058', b'vec-058', b'vec-058', b'vec-058', b'vec-058', b'vec-058'], [b'vec-059', b'vec-059', b'vec-059', b'vec-059', b'vec-059', b'vec-059', b'vec-059', b'vec-059', b'vec-059'], [], [b'vec-061'], [b'vec-062', b'vec-062'], [b'vec-063', b'vec-063', b'vec-063'], [b'vec-064', b'vec-064', b'vec-064', b'vec-064'], [b'vec-065', b'vec-065', b'vec-065', b'vec-065', b'vec-065'], [b'vec-066', b'vec-066', b'vec-066', b'vec-066', b'vec-066', b'vec-066'], [b'vec-067', b'vec-067', b'vec-067', b'vec-067', b'vec-067', b'vec-067', b'vec-067'], [b'vec-068', b'vec-068', b'vec-068', b'vec-068', b'vec-068', b'vec-068', b'vec-068', b'vec-068'], [b'vec-069', b'vec-069', b'vec-069', b'vec-069', b'vec-069', b'vec-069', b'vec-069', b'vec-069', b'vec-069'], [], [b'vec-071'], [b'vec-072', b'vec-072'], [b'vec-073', b'vec-073', b'vec-073'], [b'vec-074', b'vec-074', b'vec-074', b'vec-074'], [b'vec-075', b'vec-075', b'vec-075', b'vec-075', b'vec-075'], [b'vec-076', b'vec-076', b'vec-076', b'vec-076', b'vec-076', b'vec-076'], [b'vec-077', b'vec-077', b'vec-077', b'vec-077', b'vec-077', b'vec-077', b'vec-077'], [b'vec-078', b'vec-078', b'vec-078', b'vec-078', b'vec-078', b'vec-078', b'vec-078', b'vec-078'], [b'vec-079', b'vec-079', b'vec-079', b'vec-079', b'vec-079', b'vec-079', b'vec-079', b'vec-079', b'vec-079'], [], [b'vec-081'], [b'vec-082', b'vec-082'], [b'vec-083', b'vec-083', b'vec-083'], [b'vec-084', b'vec-084', b'vec-084', b'vec-084'], [b'vec-085', b'vec-085', b'vec-085', b'vec-085', b'vec-085'], [b'vec-086', b'vec-086', b'vec-086', b'vec-086', b'vec-086', b'vec-086'], [b'vec-087', b'vec-087', b'vec-087', b'vec-087', b'vec-087', b'vec-087', b'vec-087'], [b'vec-088', b'vec-088', b'vec-088', b'vec-088', b'vec-088', b'vec-088', b'vec-088', b'vec-088'], [b'vec-089', b'vec-089', b'vec-089', b'vec-089', b'vec-089', b'vec-089', b'vec-089', b'vec-089', b'vec-089'], [], [b'vec-091'], [b'vec-092', b'vec-092'], [b'vec-093', b'vec-093', b'vec-093'], [b'vec-094', b'vec-094', b'vec-094', b'vec-094'], [b'vec-095', b'vec-095', b'vec-095', b'vec-095', b'vec-095'], [b'vec-096', b'vec-096', b'vec-096', b'vec-096', b'vec-096', b'vec-096'], [b'vec-097', b'vec-097', b'vec-097', b'vec-097', b'vec-097', b'vec-097', b'vec-097'], [b'vec-098', b'vec-098', b'vec-098', b'vec-098', b'vec-098', b'vec-098', b'vec-098', b'vec-098'], [b'vec-099', b'vec-099', b'vec-099', b'vec-099', b'vec-099', b'vec-099', b'vec-099', b'vec-099', b'vec-099']])

    def test_array(self):
        tree = uproot.open("tests/samples/small-evnt-tree-fullsplit.root")["tree"]
        self.assertEqual(tree.array("ArrayI16[10]").tolist(), [[i] * 10 for i in range(100)])

    def test_slice(self):
        tree = uproot.open("tests/samples/small-evnt-tree-fullsplit.root")["tree"]
        self.assertEqual(tree.array("SliceI16").tolist(), [[], [1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9], [], [11], [12, 12], [13, 13, 13], [14, 14, 14, 14], [15, 15, 15, 15, 15], [16, 16, 16, 16, 16, 16], [17, 17, 17, 17, 17, 17, 17], [18, 18, 18, 18, 18, 18, 18, 18], [19, 19, 19, 19, 19, 19, 19, 19, 19], [], [21], [22, 22], [23, 23, 23], [24, 24, 24, 24], [25, 25, 25, 25, 25], [26, 26, 26, 26, 26, 26], [27, 27, 27, 27, 27, 27, 27], [28, 28, 28, 28, 28, 28, 28, 28], [29, 29, 29, 29, 29, 29, 29, 29, 29], [], [31], [32, 32], [33, 33, 33], [34, 34, 34, 34], [35, 35, 35, 35, 35], [36, 36, 36, 36, 36, 36], [37, 37, 37, 37, 37, 37, 37], [38, 38, 38, 38, 38, 38, 38, 38], [39, 39, 39, 39, 39, 39, 39, 39, 39], [], [41], [42, 42], [43, 43, 43], [44, 44, 44, 44], [45, 45, 45, 45, 45], [46, 46, 46, 46, 46, 46], [47, 47, 47, 47, 47, 47, 47], [48, 48, 48, 48, 48, 48, 48, 48], [49, 49, 49, 49, 49, 49, 49, 49, 49], [], [51], [52, 52], [53, 53, 53], [54, 54, 54, 54], [55, 55, 55, 55, 55], [56, 56, 56, 56, 56, 56], [57, 57, 57, 57, 57, 57, 57], [58, 58, 58, 58, 58, 58, 58, 58], [59, 59, 59, 59, 59, 59, 59, 59, 59], [], [61], [62, 62], [63, 63, 63], [64, 64, 64, 64], [65, 65, 65, 65, 65], [66, 66, 66, 66, 66, 66], [67, 67, 67, 67, 67, 67, 67], [68, 68, 68, 68, 68, 68, 68, 68], [69, 69, 69, 69, 69, 69, 69, 69, 69], [], [71], [72, 72], [73, 73, 73], [74, 74, 74, 74], [75, 75, 75, 75, 75], [76, 76, 76, 76, 76, 76], [77, 77, 77, 77, 77, 77, 77], [78, 78, 78, 78, 78, 78, 78, 78], [79, 79, 79, 79, 79, 79, 79, 79, 79], [], [81], [82, 82], [83, 83, 83], [84, 84, 84, 84], [85, 85, 85, 85, 85], [86, 86, 86, 86, 86, 86], [87, 87, 87, 87, 87, 87, 87], [88, 88, 88, 88, 88, 88, 88, 88], [89, 89, 89, 89, 89, 89, 89, 89, 89], [], [91], [92, 92], [93, 93, 93], [94, 94, 94, 94], [95, 95, 95, 95, 95], [96, 96, 96, 96, 96, 96], [97, 97, 97, 97, 97, 97, 97], [98, 98, 98, 98, 98, 98, 98, 98], [99, 99, 99, 99, 99, 99, 99, 99, 99]])

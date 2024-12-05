import unittest
from graph import *
import random

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        self.assertEqual(g.get_vertex('not a key'), None)
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_one_subtree(self):
        g = Graph('file_one_subtree.txt')
        self.assertEqual(g.conn_components(), [['a','b','c','d','e','f']])
        self.assertFalse(g.is_bipartite())

    def test_diff_bicol(self):
        g = Graph('file_subtrees_diff_bicol.txt')
        self.assertEqual(g.conn_components(), [['cat','dog','eagle'],['falcon','gorilla']])
        self.assertFalse(g.is_bipartite())

    def test_complex(self):
        g = Graph('file_complex.txt')
        self.assertEqual(g.conn_components(),[['a','b','c','d','e','f','g'],['abc','fij','geh','z'], ['h', 'l']])
        self.assertTrue(g.is_bipartite())

    def test_pentagon(self):
        g = Graph('file_pentagon.txt')
        self.assertEqual(g.conn_components(),[['a','b','c','d','e']])
        self.assertFalse(g.is_bipartite())

    def test_two_lines(self):
        g = Graph('file_2_lines.txt')
        self.assertEqual(g.conn_components(), [['computer','science']])
        self.assertTrue(g.is_bipartite())







if __name__ == '__main__':
   unittest.main()

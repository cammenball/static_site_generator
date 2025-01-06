import unittest

from textnode import TextNode, TextType
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "hello World", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "hello World", None, {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_node1(self):
        node = HTMLNode("p", "hello World", [1,2], {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "hello World", [1,2], {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_node2(self):
        node = HTMLNode("a", "hello World", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "hello World", None, {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_node3(self):
        node = HTMLNode("p", "hello World", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "hello World", None, {"href": "https://www.google.com"})
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
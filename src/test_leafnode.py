import unittest

from textnode import TextNode, TextType
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test 1: Basic tag with text
        node1 = LeafNode("p", "Hello, world!")
        assert node1.to_html() == "<p>Hello, world!</p>"

        # Test 2: Text with no tag
        node2 = LeafNode(None, "Just some text")
        assert node2.to_html() == "Just some text"

    def test_node2(self):
        node2 = LeafNode("a", "Just a link",{"href": "https://www.google.com"})
        assert node2.to_html() == '<a href="https://www.google.com">Just a link</a>'

    def test_text_node_to_html_node(self):
        # Test regular text conversion
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello, world!"
        assert html_node.props == None



if __name__ == "__main__":
    unittest.main()
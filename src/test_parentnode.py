import unittest

from textnode import TextNode, TextType
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_basic_parent(self):
        child = LeafNode("b", "Bold text")
        parent = ParentNode("p", [child])
        assert parent.to_html() == "<p><b>Bold text</b></p>"

        # Test 2: Text with no tag
        node2 = LeafNode(None, "Just some text")
        assert node2.to_html() == "Just some text"

    def test_node2(self):
        node2 = LeafNode("a", "Just a link",{"href": "https://www.google.com"})
        assert node2.to_html() == '<a href="https://www.google.com">Just a link</a>'



if __name__ == "__main__":
    unittest.main()

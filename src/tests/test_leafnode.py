import unittest
from src.htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_initialization(self):
        node = LeafNode(value="Hello, World!", tag="p")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.tag, "p")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html_with_value_and_tag(self):
        node = LeafNode(value="Hello, World!", tag="p")
        expected_html = "<p>Hello, World!</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_tag(self):
        node = LeafNode(value="Hello, World!", tag="")
        expected_html = "Hello, World!"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_value(self):
        node = LeafNode(value="", tag="p")
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Leaf node must contain value")

    def test_to_html_with_props(self):
        props = {"class": "my-class", "id": "my-id"}
        node = LeafNode(value="Hello, World!", tag="p", props=props)
        expected_html = '<p class="my-class" id="my-id">Hello, World!</p>'
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()

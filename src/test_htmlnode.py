import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_initialization_with_no_params(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_initialization_with_params(self):
        props = {"class": "my-class", "id": "my-id"}
        children = [HTMLNode(tag="span", value="Hello")]
        node = HTMLNode(tag="div", value="Content", children=children, props=props)

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Content")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].value, "Hello")
        self.assertEqual(node.props, props)

    def test_props_to_html(self):
        props = {"class": "my-class", "id": "my-id"}
        node = HTMLNode(tag="div", props=props)
        expected_html = ' class="my-class" id="my-id"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_repr(self):
        props = {"class": "my-class", "id": "my-id"}
        node = HTMLNode(tag="div", value="Content", props=props)
        expected_repr = f"HTMLNode(div, Content, None, {props})"
        self.assertEqual(repr(node), expected_repr)

    def test_empty_props_to_html(self):
        node = HTMLNode(tag="div", props={})
        expected_html = ""
        self.assertEqual(node.props_to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()

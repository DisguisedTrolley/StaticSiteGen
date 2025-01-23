from htmlnode import ParentNode, LeafNode
import unittest


class TestParentNode(unittest.TestCase):
    def test_to_html_with_valid_input(self):
        # Test with valid tag and children
        child1 = LeafNode(tag="span", value="Hello")
        child2 = LeafNode(tag="span", value="World")
        parent = ParentNode(tag="div", children=[child1, child2])

        expected_html = "<div><span>Hello</span><span>World</span></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_empty_tag(self):
        # Test with empty tag
        parent = ParentNode(tag="", children=[LeafNode(tag="span", value="Some value")])
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "Tag is required")

    def test_to_html_with_no_children(self):
        # Test with no children
        parent = ParentNode(tag="div", children=None)
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "Children array is required")

    def test_to_html_with_props(self):
        # Test with props
        child = LeafNode(tag="span", value="Hello")
        parent = ParentNode(tag="div", children=[child], props={"class": "my-class"})

        expected_html = '<div class="my-class"><span>Hello</span></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_multiple_children(self):
        # Test with multiple children
        child1 = LeafNode(tag="p", value="Paragraph 1")
        child2 = LeafNode(tag="p", value="Paragraph 2")
        parent = ParentNode(tag="section", children=[child1, child2])

        expected_html = "<section><p>Paragraph 1</p><p>Paragraph 2</p></section>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_nested_parent(self):
        # Test with nested children
        child1 = LeafNode(tag="p", value="Paragraph 1")
        child2 = LeafNode(tag="p", value="Paragraph 2")
        child3 = LeafNode(tag="p", value="Paragraph 3")
        child4 = LeafNode(tag="p", value="Paragraph 4")
        nested_child = ParentNode(tag="div", children=[child1, child2])
        parent = ParentNode(tag="section", children=[child3, nested_child, child4])

        expected_html = "<section><p>Paragraph 3</p><div><p>Paragraph 1</p><p>Paragraph 2</p></div><p>Paragraph 4</p></section>"
        self.assertEqual(parent.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()

import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a image node", TextType.IMAGE, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_invalid_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertIsNotNone(node.url)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextToHTML(unittest.TestCase):
    def test_normal_text(self):
        node = TextNode(text="Normal text", text_type=TextType.TEXT)
        converted = text_node_to_html_node(node)
        self.assertEqual("", converted.tag)
        self.assertEqual("Normal text", converted.value)
        self.assertIsNone(converted.props)

    def test_bold_text(self):
        node = TextNode(text="Bold text", text_type=TextType.BOLD)
        converted = text_node_to_html_node(node)
        self.assertEqual("b", converted.tag)
        self.assertEqual("Bold text", converted.value)
        self.assertIsNone(converted.props)

    def test_link_text(self):
        node = TextNode(
            text="Boot dev", text_type=TextType.LINK, url="https://boot.dev"
        )
        converted = text_node_to_html_node(node)
        self.assertEqual("a", converted.tag)
        self.assertEqual({"href": "https://boot.dev"}, converted.props)
        self.assertEqual("Boot dev", converted.value)
        self.assertIsNone(converted.children)


if __name__ == "__main__":
    unittest.main()

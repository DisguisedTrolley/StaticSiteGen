import unittest
from src.textnode import TextNode, TextType
from src.splitdelimiter import split_nodes_delimiter


class TestSplitNodesDelimiterTextTypes(unittest.TestCase):
    def test_split_text_type_text(self):
        node = TextNode("Hello, world!", TextType.TEXT)
        result = split_nodes_delimiter([node])
        expected = [
            TextNode("Hello, world!", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_text_type_bold(self):
        nodes_with_bold = [
            TextNode("This is **bold** text.", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes_with_bold)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)


"""
    def test_split_text_type_italic(self):
        nodes_with_italic = [
            TextNode("This is *italic* | text.", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes_with_italic, "|", TextType.ITALIC)
        expected = [
            TextNode("This is *italic* ", TextType.TEXT),
            TextNode(" text.", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)

    def test_split_text_type_code(self):
        nodes_with_code = [
            TextNode("This is `code` | text.", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes_with_code, "|", TextType.CODE)
        expected = [
            TextNode("This is `code` ", TextType.TEXT),
            TextNode(" text.", TextType.CODE),
        ]
        self.assertEqual(result, expected)

    def test_split_mixed_text_types(self):
        mixed_nodes = [
            TextNode(
                "This is **bold** | and this is *italic* | and this is `code`.",
                TextType.TEXT,
            ),
        ]
        result = split_nodes_delimiter(mixed_nodes, "|", TextType.TEXT)
        expected = [
            TextNode("This is **bold** ", TextType.TEXT),
            TextNode(" and this is *italic* ", TextType.TEXT),
            TextNode(" and this is `code`.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
"""

if __name__ == "__main__":
    unittest.main()

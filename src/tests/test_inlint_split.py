import unittest
from src.textnode import TextNode, TextType
from src.inline_split import (
    split_links,
    split_nodes_delimiter,
)


class TestSplitNodesDelimiterTextTypes(unittest.TestCase):
    def test_split_text_type_text(self):
        node = TextNode("Hello, world!", TextType.TEXT)
        result = split_nodes_delimiter([node])
        expected = [
            TextNode("Hello, world!", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_text_type_bold(self):
        node = TextNode("This is **bold** text.", TextType.TEXT)

        result = split_nodes_delimiter([node])
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_multiple_types(self):
        node = TextNode("This has **bold** and an *italic* text", TextType.TEXT)

        result = split_nodes_delimiter([node])
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


class TestSplitNodesDelimiterImageAndLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode("this has a [link](https://boot.dev)", TextType.TEXT)

        result = split_links([node])

        expected = [
            TextNode("this has a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(result, expected)

    def test_split_images(self):
        node = TextNode(
            "This has an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )

        result = split_links([node])

        expected = [
            TextNode("This has an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
        ]

        self.assertEqual(result, expected)

    def test_the_entire_flow(self):
        node = TextNode(
            "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
            TextType.TEXT,
        )

        text_nodes = split_nodes_delimiter([node])
        link_nodes = split_links(text_nodes)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(link_nodes, expected)

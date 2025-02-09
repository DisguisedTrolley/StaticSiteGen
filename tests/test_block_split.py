import unittest

from src.block_split import block_to_blocktype, markdown_to_blocks


class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_block_err(self):
        file = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        res = markdown_to_blocks(file)
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]

        self.assertEqual(res, expected)

    def test_empty_string(self):
        file = ""
        res = markdown_to_blocks(file)
        expected = []
        self.assertEqual(res, expected)

    def test_only_newlines(self):
        file = "\n\n\n"
        res = markdown_to_blocks(file)
        expected = []
        self.assertEqual(res, expected)

    def test_single_paragraph(self):
        file = "This is a single paragraph."
        res = markdown_to_blocks(file)
        expected = ["This is a single paragraph."]
        self.assertEqual(res, expected)

    def test_multiple_paragraphs_with_extra_newlines(self):
        file = "First paragraph.\n\n\nSecond paragraph.\n\nThird paragraph."
        res = markdown_to_blocks(file)
        expected = ["First paragraph.", "Second paragraph.", "Third paragraph."]
        self.assertEqual(res, expected)

    def test_paragraphs_with_only_newlines_between(self):
        file = "Paragraph one.\n\n\n\nParagraph two."
        res = markdown_to_blocks(file)
        expected = ["Paragraph one.", "Paragraph two."]
        self.assertEqual(res, expected)


class TestBlockType(unittest.TestCase):
    def test_block_type_heading(self):
        inp = "##  This is a secondary heading"
        res = block_to_blocktype(inp)

        expected = "heading"

        self.assertEqual(res, expected)

    def test_block_type_code(self):
        inp = """```py code type.\n some code here\n```"""
        res = block_to_blocktype(inp)

        expected = "code"

        self.assertEqual(res, expected)

    def test_block_type_wrong_code(self):
        inp = '```py print("hello")'

        res = block_to_blocktype(inp)

        expected = "paragraph"

        self.assertEqual(res, expected)

    def test_block_type_quote(self):
        inp = """> quote of the day\n> Some quote\n> yet another quote"""

        res = block_to_blocktype(inp)
        expected = "quote"

        self.assertEqual(res, expected)

    def test_block_type_wrong_quote(self):
        inp = """> quote of the day\nsomething in between\n> another quote"""

        res = block_to_blocktype(inp)
        expected = "paragraph"

        self.assertEqual(res, expected)

    def test_block_type_uo_list(self):
        inp = """* list item 1\n* list item two"""

        res = block_to_blocktype(inp)

        expected = "unordered_list"

        self.assertEqual(res, expected)

    def test_block_type_paragraph(self):
        inp = """* This was a list\nbut this line ruined it."""

        res = block_to_blocktype(inp)
        expected = "paragraph"

        self.assertEqual(res, expected)

    def test_block_type_ordered_list(self):
        inp = (
            """1. this is supposed to be an ordered list\n2. this is the second item"""
        )

        res = block_to_blocktype(inp)
        expected = "ordered_list"

        self.assertEqual(res, expected)

    def test_block_type_wrong_ordered_list(self):
        inp = """1. this is supposed to be an ordered list\n2. this is the second item\nthis is not a list item so it breaks"""

        res = block_to_blocktype(inp)
        expected = "paragraph"

        self.assertEqual(res, expected)

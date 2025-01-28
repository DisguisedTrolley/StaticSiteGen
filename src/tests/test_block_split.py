import unittest

from src.block_split import markdown_to_blocks


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
            "* This is a list\n* with items"
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
        expected = [
            "First paragraph.",
            "Second paragraph.",
            "Third paragraph."
        ]
        self.assertEqual(res, expected)

    def test_paragraphs_with_only_newlines_between(self):
        file = "Paragraph one.\n\n\n\nParagraph two."
        res = markdown_to_blocks(file)
        expected = [
            "Paragraph one.",
            "Paragraph two."
        ]
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()

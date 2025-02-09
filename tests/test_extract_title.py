import unittest

from src.md_to_html import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_single_heading(self):
        markdown = "# Title\n\nSome content here."
        self.assertEqual(extract_title(markdown), "Title")

    def test_multiple_headings(self):
        markdown = "# First Title\n\nSome content here.\n\n## Second Title"
        self.assertEqual(extract_title(markdown), "First Title")

    def test_no_heading(self):
        markdown = "Some content here without a heading."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Heading not found")

    def test_empty_markdown(self):
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Heading not found")

    def test_heading_with_extra_spaces(self):
        markdown = "#   Title with spaces   \n\nContent here."
        self.assertEqual(extract_title(markdown), "Title with spaces")

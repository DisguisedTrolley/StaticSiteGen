import unittest

from src.md_to_html import markdown_to_html


class TestMdToHTMLNode(unittest.TestCase):
    def test_links(self):
        node = """
# The Unparalleled Majesty of "The Lord of the Rings"

[Back Home](/)

![LOTR image artistmonkeys](/images/rivendell.png)
"""
        res = markdown_to_html(node)
        print(res)
        self.assertEqual("Test", "Test")

    def test_different_headings(self):
        node = """# primary heading\n\n## secondary heading\n\n### This here is h3\n\n#### h4 comes here"""

        res = markdown_to_html(node)
        exp = "<div><h1>primary heading</h1><h2>secondary heading</h2><h3>This here is h3</h3><h4>h4 comes here</h4></div>"

        self.assertEqual(res, exp)

    def test_code_block(self):
        node = """
# Primary heading

```Some code goes in here```

## secondary heading
"""

        res = markdown_to_html(node)
        exp = "<div><h1>Primary heading</h1><pre><code>Some code goes in here</code></pre><h2>secondary heading</h2></div>"

        self.assertEqual(res, exp)

    def test_quote_block(self):
        node = """
# How to code?

This md doc *will* teach **coding**

> This is a
> Code block
"""

        res = markdown_to_html(node)
        exp = "<div><h1>How to code?</h1><p>This md doc <i>will</i> teach <b>coding</b></p><blockquote>This is a Code block</blockquote></div>"

        self.assertEqual(res, exp)

    def test_unordered_list_block(self):
        node = """# List items\n\n* first item\n* second *item*"""

        res = markdown_to_html(node)
        exp = "<div><h1>List items</h1><ul><li>first item</li><li>second <i>item</i></li></ul></div>"

        self.assertEqual(res, exp)

    def test_ordered_list(self):
        node = """## List items\n\n1. First ordered list item.\n2. second ordered list item."""

        res = markdown_to_html(node)
        exp = "<div><h2>List items</h2><ol><li>First ordered list item.</li><li>second ordered list item.</li></ol></div>"

        self.assertEqual(res, exp)

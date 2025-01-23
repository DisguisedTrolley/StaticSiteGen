# NOTE: A "TextNode" is an intermediate representation between Markdown and HTML, and is specific to inline markup.
# The HTMLNode class will represent a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents)
# and is purpose-built to render itself as HTML.

from typing import Optional, List


class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: Optional[List["HTMLNode"]] = None,
        props: dict = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props:
            return ""

        props = list(map(lambda x: f' {x[0]}="{x[1]}"', self.props.items()))
        return "".join(props)

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


# NOTE: A LeafNode is a type of HTMLNode that represents a single HTML tag with no children.
# For example, a simple <p> tag with some text inside of it:
# <p>This is a paragraph of text.</p>


class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str, props: dict = None):
        super().__init__(value=value, tag=tag, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf node must contain value")

        if not self.tag:
            return self.value

        attributes = self.props_to_html()
        leaf_node = f"<{self.tag}{attributes}>{self.value}</{self.tag}>"

        return leaf_node

# NOTE: A TextNode is a way to represent all different types of inline text.
# Examples of inline Text:
# - This is normal text
# - **This is bold text**
# - *This is italic text*
# - `This is code`
# - [This is a link](https://boot.dev)
# - ![This is an image](https://boot.dev/image.jpg)

from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

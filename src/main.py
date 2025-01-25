from splitdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def main():
    node = TextNode(
        text="This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
        text_type=TextType.TEXT,
    )

    print(split_nodes_delimiter([node]))


if __name__ == "__main__":
    main()

lis = [
    TextNode("This is ", "text", "None"),
    TextNode("text", "bold", "None"),
    TextNode(" with an ", "text", "None"),
    TextNode("italic", "italic", "None"),
    TextNode(" word and a ", "text", "None"),
    TextNode("code block", "code", "None"),
    TextNode(
        " and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
        "text",
        "None",
    ),
]

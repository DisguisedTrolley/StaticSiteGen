import re
from typing import List
from src.textnode import TextNode, TextType


TYPE_REGEX = r"(\*{1,2}|`)"
FORMAT_MAP = {"**": TextType.BOLD, "*": TextType.ITALIC, "`": TextType.CODE}


# TODO: Add children prop to TextNode and provide nesting support.


def split_nodes_delimiter(nodes: List["TextNode"]):
    final_nodes = []
    for node in nodes:
        # Gives a list of all the matching types. Occouring in order.
        matches = re.findall(TYPE_REGEX, node.text)

        # Base case. When no delimiters are found
        if not matches:
            final_nodes.append(node)

        else:
            new_nodes = []

            # Split the string by the first delimiter.
            sections = node.text.split(matches[0])

            # even split means the delimiters are not in pairs.
            if len(sections) % 2 == 0:
                raise Exception("Invalid markdown format")

            for i in range(len(sections)):
                # case when first element is a delimiter.
                if sections[i] == "":
                    continue

                if i % 2 == 0:
                    new_nodes.append(
                        TextNode(text=sections[i], text_type=node.text_type)
                    )
                else:
                    new_nodes.append(
                        TextNode(text=sections[i], text_type=FORMAT_MAP[matches[0]])
                    )
            final_nodes.extend(split_nodes_delimiter(nodes=new_nodes))

    return final_nodes

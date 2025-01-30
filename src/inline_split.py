import re
from typing import List

from textnode import TextNode, TextType

TEXT_REGEX = r"(\*{1,2}|`)"
COMBINED_REGEX = r"(!?\[([^\]]+)\]\(([^)]+)\))"
FORMAT_MAP = {"**": TextType.BOLD, "*": TextType.ITALIC, "`": TextType.CODE}


def split_nodes_delimiter(nodes: List["TextNode"]) -> List["TextNode"]:
    final_nodes = []
    for node in nodes:
        # Gives a list of all the matching types. Occouring in order.
        txt_match = re.findall(TEXT_REGEX, node.text)

        # Prioratises '**' over '*'.
        # stripping '*' first is disasterous here as it strips the bold one also.
        # Will think of a better way at some point (probably, maybe) (the answer is probably regex but i dont want to use it).
        txt_match = sorted(txt_match, reverse=True)

        # Base case. When no delimiters are found
        if not txt_match:
            final_nodes.append(node)

        else:
            new_nodes = []

            # Split the string by the first delimiter.
            sections = node.text.split(txt_match[0])

            # even split means the delimiters are not in pairs.
            if len(sections) % 2 == 0:
                raise Exception(
                    f"Invalid markdown format. Non matching '{txt_match[0]}' delimiter\nline reference: '{node.text}'"
                )

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
                        TextNode(text=sections[i], text_type=FORMAT_MAP[txt_match[0]])
                    )
            final_nodes.extend(split_nodes_delimiter(nodes=new_nodes))

    return final_nodes


def split_links(nodes: List["TextNode"]) -> List["TextNode"]:
    final_nodes = []
    for node in nodes:
        if re.search(COMBINED_REGEX, node.text) is None:
            final_nodes.append(node)
            continue

        # Learned about re.finditer, tis some woodoo shit.
        link_match = re.finditer(COMBINED_REGEX, node.text)

        new_nodes = []
        prev_match_end = 0
        for link in link_match:
            # Each match has the starting and ending indexes rel to the original string.
            # Each match also contains the groups it matched.
            # The regex used splits the string into three groups,
            # 1. the whole string from '[' to ')'.
            # 2. the alt text
            # 3. the url

            is_img = link.group(0).startswith("!")

            text = node.text[prev_match_end : link.start()]
            alt = link.group(2)
            url = link.group(3)

            if text != "":
                new_nodes.append(TextNode(text=text, text_type=TextType.TEXT))

            new_nodes.append(
                TextNode(
                    text=alt,
                    text_type=TextType.LINK if not is_img else TextType.IMAGE,
                    url=url,
                )
            )

            prev_match_end = link.end()

        ending_string = node.text[prev_match_end:]

        if ending_string.strip() != "":
            new_nodes.append(TextNode(text=ending_string, text_type=TextType.TEXT))

        final_nodes.extend(new_nodes)

    return final_nodes

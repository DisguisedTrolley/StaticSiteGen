from typing import List

from block_split import block_to_blocktype, markdown_to_blocks
from htmlnode import ParentNode
from inline_split import split_links, split_nodes_delimiter
from textnode import TextNode, TextType, text_node_to_html_node


def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    title = None

    for block in blocks:
        if block.startswith("# "):
            title = block.lstrip("# ").strip()
            break

    if not title:
        raise Exception("Heading not found")

    return title


def markdown_to_html(markdown: str) -> str:
    # Split the markdown file into digestable blocks.
    blocks = markdown_to_blocks(markdown)

    children_nodes = []

    for block in blocks:
        block_type = block_to_blocktype(block)
        node = block_to_node(block, block_type)
        children_nodes.append(node)

    final_html = ParentNode(tag="div", children=children_nodes).to_html()
    return final_html


# Helper functions.

"""
Split each block of markdown into a list of nodes.
"""


def block_to_node(block: str, block_type: str) -> ParentNode:
    match block_type:
        case "heading":
            h_index = block.count("#")
            heading = block.lstrip("# ")

            return get_children_nodes(heading, f"h{h_index}")

        case "code":
            code = block.strip("```")
            node = get_children_nodes(code, "code")
            wrapper = ParentNode(tag="pre", children=[node])

            return wrapper

        case "quote":
            quote = " ".join([q.lstrip("> ") for q in block.splitlines()])
            node = get_children_nodes(quote, "blockquote")

            return node

        case "unordered_list":
            list_items = block.splitlines()
            list_items_cleaned = [li[2:] for li in list_items]

            return handle_lists(list_items_cleaned, "ul")

        case "ordered_list":
            list_items = block.splitlines()
            list_items_cleaned = [
                list_items[i].lstrip(f"{i + 1}. ") for i in range(len(list_items))
            ]

            return handle_lists(list_items_cleaned, "ol")

        case _:
            lines = " ".join(block.splitlines())
            return get_children_nodes(lines, "p")


"""
Returns a list of child nodes from a given TextNode
"""


def get_children_nodes(text: str, tag: str) -> List[TextNode]:
    main_node = TextNode(text=text, text_type=TextType.TEXT)
    child_text_nodes = split_nodes_delimiter([main_node])
    child_text_nodes = split_links(child_text_nodes)

    child_html_nodes = []

    for node in child_text_nodes:
        child_html_nodes.append(text_node_to_html_node(node))

    parent_node = ParentNode(tag=tag, children=child_html_nodes)

    return parent_node


def handle_lists(list_items: List[str], tag: str) -> ParentNode:
    children_nodes = []
    for item in list_items:
        child_node = get_children_nodes(item, "li")
        children_nodes.append(child_node)

    return ParentNode(tag=tag, children=children_nodes)

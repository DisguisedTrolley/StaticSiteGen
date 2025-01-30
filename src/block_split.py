import re
from typing import List


def markdown_to_blocks(markdown: str) -> List[str]:
    result = []
    split_lines = markdown.split("\n\n")

    for line in split_lines:
        if line == "":
            continue

        block = line.strip()

        if block == "":
            continue

        result.append(block)

    return result


def block_to_blocktype(block: str) -> str:
    if re.match(r"^(#{1,6})\s(.*)", block):
        return "heading"

    if block.startswith("```") and block.endswith("```"):
        return "code"

    lines = block.split("\n")

    check_quote = all(line.startswith("> ") for line in lines)
    if check_quote:
        return "quote"

    check_uo_list_star = all(line.startswith("* ") for line in lines)
    check_uo_list_dash = all(line.startswith("- ") for line in lines)

    if check_uo_list_star or check_uo_list_dash:
        return "unordered_list"

    check_ordered_list = all(
        lines[i].startswith(f"{i + 1}. ") for i in range(len(lines))
    )
    if check_ordered_list:
        return "ordered_list"

    return "paragraph"

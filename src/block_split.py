from typing import List


def markdown_to_blocks(markdown: str) -> List[str]:
    result = []
    split_lines = markdown.split('\n\n')

    for line in split_lines:
        if line == '':
            continue

        block = line.strip()
        
        if block == "":
            continue
        
        result.append(block)

    return result

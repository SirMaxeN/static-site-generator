from enum import Enum
import re
from typing import List


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> List[str]:
    output: List[str] = []
    for split in markdown.split("\n\n"):
        to_join: List[str] = []
        for line in split.split("\n"):
            line = line.strip()
            if line != "" and line != "\n":
                to_join.append(line)

        split = "\n".join(to_join)
        if split == "" or split == "\n":
            continue
        output.append(split)
    return output


def block_to_block_type(block_text: str) -> BlockType:
    match block_text[0]:
        case "#":
            if block_text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
                return BlockType.HEADING
        case ">":
            split = block_text.split("\n")
            for line in split:
                if not line.startswith("> "):
                    return BlockType.PARAGRAPH
            return BlockType.QUOTE
        case '`':
            if len(re.findall(r"(```)(?s:.*?)(```)", block_text, re.M),) > 0:
                return BlockType.CODE
        case "-":
            split = block_text.split("\n")
            for line in split:
                if not line.startswith("- "):
                    return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST
        case "1":
            split = block_text.split("\n")
            count = 1
            for line in split:
                if not line.startswith(f"{count}. "):
                    return BlockType.PARAGRAPH
                count += 1
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

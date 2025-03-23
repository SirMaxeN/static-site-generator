from typing import List


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

from htmlnode import HTMLNode
from typing import List, Dict


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List['HTMLNode'], props: Dict[str, str] = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag.")
        if self.children == None or len(self.children) == 0:
            raise ValueError("All parent nodes must have at least 1 child.")

        output = ""
        for child in self.children:
            output += f"{child.to_html()}"
        return f"<{self.tag}{self.props_to_html()}>{output}</{self.tag}>"

from typing import List, Dict


class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: List['HTMLNode'] = None, props: Dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        output: str = ""
        if self.props == None:
            return output
        for i in self.props:
            output += f" {i}=\"{self.props[i]}\""

        return output

    def __eq__(self, html_node: 'HTMLNode'):
        return (
            html_node.tag == self.tag and
            html_node.value == self.value and
            html_node.children == self.children and
            html_node.props == self.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

import re
from typing import List
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node: 'TextNode'):
    if not text_node:
        raise ValueError("Missing text_node")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(
                f"Missing or incorrect text_node type: {text_node.text_type.value}")


def split_nodes_delimiter(old_nodes: List['TextNode'], delimiter: str, text_type: TextType) -> List['TextNode']:
    output: List['TextNode'] = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if delimiter not in node.text:
                raise ValueError(
                    f"Delimiter: {delimiter} missing in text: {node.text}"
                )
            splited = node.text.split(delimiter)

            if len(splited) % 2 == 0:
                raise ValueError(
                    "invalid markdown, formatted section not closed")

            for i in range(0, len(splited)):
                if splited[i] != "":
                    if i % 2 == 0:
                        output.append(TextNode(splited[i], TextType.TEXT))
                    else:
                        output.append(TextNode(splited[i], text_type))
        else:
            output.append(node)

    return output


def extract_markdown_images(text: str):
    return re.findall("\!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str):
    return re.findall("\[(.*?)\]\((.*?)\)", text)

import re
from typing import List, Tuple
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


def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_util(text: str, delimiter: str, text_type: TextType, matches: List[Tuple[str, str]] = []) -> List['TextNode']:
    output = []

    for match in matches:
        if text_type == TextType.IMAGE:
            text = text.replace(
                f"![{match[0]}]({match[1]})", f"{delimiter}_{delimiter}")
        elif text_type == TextType.LINK:
            text = text.replace(
                f"[{match[0]}]({match[1]})", f"{delimiter}_{delimiter}")

    splited = text.split(delimiter)

    if len(splited) % 2 == 0:
        raise ValueError(
            "invalid markdown, formatted section not closed")

    count = 0
    for i in range(0, len(splited)):
        if splited[i] != "":
            if i % 2 == 0:
                output.append(TextNode(splited[i], TextType.TEXT))
            else:
                if len(matches) > 0:
                    output.append(
                        TextNode(matches[count][0], text_type, matches[count][1]))
                    count += 1
                else:
                    output.append(TextNode(splited[i], text_type))
    return output


def split_nodes_delimiter(old_nodes: List['TextNode'], delimiter: str, text_type: TextType) -> List['TextNode']:
    output: List['TextNode'] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
            continue
        if node.text_type == TextType.TEXT:
            output.extend(split_nodes_util(
                node.text, delimiter, text_type))
    return output


def split_nodes_image(old_nodes: List['TextNode']) -> List['TextNode']:
    output: List['TextNode'] = []
    delimiter = "!tosplit!"
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
            continue
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            output.append(node)
            continue
        output.extend(split_nodes_util(
            node.text, delimiter, TextType.IMAGE, matches))

    return output


def split_nodes_link(old_nodes: List['TextNode']) -> List['TextNode']:
    output: List['TextNode'] = []
    delimiter = "!tosplit!"
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
            continue
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            output.append(node)
            continue
        output.extend(split_nodes_util(
            node.text, delimiter, TextType.LINK, matches))

    return output


def text_to_textnodes(text: str) -> List['TextNode']:
    options = [("**", TextType.BOLD), ("`", TextType.CODE),
               ("_", TextType.ITALIC)
               ]
    output: List['TextNode'] = [TextNode(text, TextType.TEXT)]
    for option in options:
        output = split_nodes_delimiter(output, option[0], option[1])

    output = (split_nodes_image(output))
    output = (split_nodes_link(output))

    return output

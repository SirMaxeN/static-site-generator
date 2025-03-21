from textnode import TextNode, TextType
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from utils import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, text_node_to_html_node


def main():
    tn = TextNode("This is some anchor text",
                  TextType.LINK, "https://www.boot.dev")
    print()
    print(tn)

    hn = HTMLNode(props={
        "href": "https://www.google.com",
        "target": "_blank",
    })
    print()
    print(hn)

    pn1 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    pn2 = ParentNode(
        "code",
        [
            LeafNode("b", "Bold text"),
            pn1,
            LeafNode("link", "this is link", {
                     "href": "https://somthingsomthing.com"}),
            LeafNode(None, "Normal text"),
        ],
    )
    print()
    print(pn1.to_html())
    print(pn2.to_html())

    tn = TextNode("this is alt text", TextType.IMAGE,
                  "https://urltoimage.com")
    ln: LeafNode = text_node_to_html_node(tn)
    print()
    print(tn)
    print(ln)
    print(ln.to_html())

    tn = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([tn], "`", TextType.CODE)
    print()
    print(new_nodes)

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print()
    print(extract_markdown_images(text))

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print()
    print(extract_markdown_links(text))


if __name__ == "__main__":
    main()

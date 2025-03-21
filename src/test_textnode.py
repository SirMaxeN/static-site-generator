import unittest

from utils import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("", TextType.CODE)
        node2 = TextNode("", TextType.CODE)
        self.assertEqual(node, node2)

        node = TextNode("text", TextType.IMAGE)
        node2 = TextNode("text", TextType.IMAGE, None)
        self.assertEqual(node, node2)

        node = TextNode("This is a link node", TextType.LINK, "https link")
        node2 = TextNode("This is a link node", TextType.LINK, "https link")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

        node = TextNode(None, TextType.BOLD)
        node2 = TextNode(None, TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", None)
        node2 = TextNode("This is a text node", None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

        node = TextNode("italic", TextType.ITALIC)
        node2 = TextNode("bold", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node = TextNode("italic", TextType.ITALIC)
        node2 = TextNode("italic", TextType.ITALIC, "url link")
        self.assertNotEqual(node, node2)

        node = TextNode(None, TextType.ITALIC)
        node2 = TextNode("italic", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node = TextNode("italic", TextType.ITALIC)
        node2 = TextNode("italic", None)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("some text", TextType.ITALIC)
        self.assertEqual(
            node.__repr__(),
            "TextNode(some text, italic, None)",
        )

        node = TextNode("This is a code node", TextType.CODE, "https url")
        self.assertEqual(
            node.__repr__(),
            "TextNode(This is a code node, code, https url)",
        )

        node = TextNode("This is a link node", TextType.LINK, "https link")
        node2 = TextNode("This is a link node", TextType.LINK, "https link")
        self.assertEqual(node.__repr__(), node2.__repr__(),)

    def test_text_to_leaf(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "This is a text node")

        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")
        self.assertEqual(html_node.to_html(), "<i>This is a italic node</i>")

        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
        self.assertEqual(html_node.to_html(),
                         "<code>This is a code node</code>")

        node = TextNode("this is link", TextType.LINK,
                        "https://somethinghere.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "this is link")
        self.assertEqual(html_node.props_to_html(),
                         ' href="https://somethinghere.com"')
        self.assertEqual(html_node.to_html(
        ), '<a href="https://somethinghere.com">this is link</a>')

        node = TextNode("this is alt text", TextType.IMAGE,
                        "https://urltoimage.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://urltoimage.com", "alt": "this is alt text"},
        )
        self.assertEqual(
            html_node.props_to_html(),
            ' src="https://urltoimage.com" alt="this is alt text"',
        )
        self.assertEqual(html_node.to_html(
        ), '<img src="https://urltoimage.com" alt="this is alt text"></img>')


if __name__ == "__main__":
    unittest.main()

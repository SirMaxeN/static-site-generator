import unittest

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


if __name__ == "__main__":
    unittest.main()

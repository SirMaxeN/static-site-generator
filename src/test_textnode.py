import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_0(self):
        node = TextNode("", TextType.CODE)
        node2 = TextNode("", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq_1(self):
        node = TextNode("text", TextType.IMAGE)
        node2 = TextNode("text", TextType.IMAGE, None)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.LINK, "https link")
        node2 = TextNode("This is a text node", TextType.LINK, "https link")
        self.assertEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_4(self):
        node = TextNode(None, TextType.BOLD)
        node2 = TextNode(None, TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_5(self):
        node = TextNode("This is a text node", None)
        node2 = TextNode("This is a text node", None)
        self.assertEqual(node, node2)

    def test_not_eq_0(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_not_eq_1(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = TextNode("italic", TextType.ITALIC)
        node2 = TextNode("bold", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_3(self) -> None:
        node = TextNode("italic", TextType.ITALIC)
        node2 = TextNode("italic", TextType.ITALIC, "url link")
        self.assertNotEqual(node, node2)

    def test_not_eq_4(self) -> None:
        node = TextNode(None, TextType.ITALIC)
        node2 = TextNode("italic", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_5(self) -> None:
        node = TextNode("italic", TextType.ITALIC)
        node2 = TextNode("italic", None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

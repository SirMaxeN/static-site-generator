import unittest
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

        node = HTMLNode("tag")
        node2 = HTMLNode("tag")
        self.assertEqual(node, node2)

        node = HTMLNode("tag", "value", [], {"href": "html"})
        node2 = HTMLNode("tag", "value", [], {"href": "html"})

        self.assertEqual(node, node2)
        child1 = HTMLNode()
        child2 = HTMLNode()

        node = HTMLNode("tag", "value", [child1, child2], {"href": "html"})
        node2 = HTMLNode("tag", "value", [child1, child2], {"href": "html"})
        self.assertEqual(node, node2)

        node = HTMLNode("tag", "value", None)
        node2 = HTMLNode("tag", "value")
        self.assertEqual(node, node2)

        node = HTMLNode(props={"href": "html", "p": "paragraph"})
        node2 = HTMLNode(None, None, None, {"href": "html", "p": "paragraph"})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode()
        node2 = HTMLNode("tag", "value", [], {"href": "html"})
        self.assertNotEqual(node, node2)

        child1 = HTMLNode()
        child2 = HTMLNode("tag", "value")

        node = HTMLNode("tag", "value", [child1], {"href": "html"})
        node2 = HTMLNode("tag", "value", [child2], {"href": "html"})
        self.assertNotEqual(node, node2)

        node = HTMLNode(None, None, None, {"href": "html", "p": "paragraph"})
        node2 = HTMLNode(None, None, None, {"href": "html"})
        self.assertNotEqual(node, node2)

        node = HTMLNode(None, None, None, {"href": "html", "p": "paragraph"})
        node2 = HTMLNode(None, None, None, {"href": "html"})
        self.assertNotEqual(node, node2)

        child1 = HTMLNode()

        node = HTMLNode("tag", "value", [child1], {"href": "html"})
        node2 = HTMLNode("tag", "value", None, {"href": "html"})
        self.assertNotEqual(node, node2)

        child1 = HTMLNode()

        node = HTMLNode("tag", "value", [child1])
        node2 = HTMLNode("tag", "value", [])
        self.assertNotEqual(node, node2)

        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_eq_props_to_html(self) -> None:
        child1 = HTMLNode()

        node = HTMLNode("tag", "value", [child1], {"href": "html"})
        node2 = HTMLNode("tag", "value", None, {"href": "html"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

        node = HTMLNode(props={"p": "paragraph"})
        node2 = HTMLNode("tag", "value", None, {"p": "paragraph"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

        node = HTMLNode("div", "Hello, world!", None, {
                        "class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_not_eq_props_to_html(self) -> None:
        node = HTMLNode(None, None, None, {"href": "html", "p": "paragraph"})
        node2 = HTMLNode(None, None, None, {"href": "html_", "p": "paragraph"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

        node = HTMLNode(None, None, None, {"href": "html", "p": "paragraph"})
        node2 = HTMLNode(None, None, None, {"href": "html"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_repr(self):
        node = HTMLNode("p", "What a strange world",
                        None, {"class": "primary"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

        node = HTMLNode("p", "some text", None, {"class": "primary"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, some text, children: None, {'class': 'primary'})",
        )

        child1 = HTMLNode()

        node = HTMLNode("tag", "value", [child1], {"href": "html"})
        node2 = HTMLNode("tag", "value", [child1], {"href": "html"})
        self.assertEqual(node.__repr__(), node2.__repr__(),)


if __name__ == "__main__":
    unittest.main()

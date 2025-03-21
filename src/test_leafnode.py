import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_type_error(self):
        self.assertRaises(TypeError, lambda: LeafNode("tag"))
        self.assertRaises(TypeError, lambda: LeafNode(value="value"))
        self.assertRaises(TypeError, lambda: LeafNode(
            props={"href": "html", "p": "paragraph"}))

    def test_eq(self):
        node = LeafNode(None, "text")
        node2 = LeafNode(None, "text")
        self.assertEqual(node, node2)

        node = LeafNode("tag", "value", {"href": "html"})
        node2 = LeafNode("tag", "value", {"href": "html"})

        self.assertEqual(node, node2)

        node = LeafNode("tag", "value", None)
        node2 = LeafNode("tag", "value")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode("tag1", "value")
        node2 = LeafNode("tag2", "value")
        self.assertNotEqual(node, node2)

        node = LeafNode("tag", "value", {"href": "html", "p": "paragraph"})
        node2 = LeafNode("tag", "value", {"href": "html"})
        self.assertNotEqual(node, node2)

    def test_eq_props_to_html(self) -> None:

        node = LeafNode("tag", "value", {"href": "html"})
        node2 = LeafNode("tag", "value", {"href": "html"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_not_eq_props_to_html(self) -> None:
        node = LeafNode("tag", "value", {"href": "html", "p": "paragraph"})
        node2 = LeafNode("tag", "value", {"href": "html_", "p": "paragraph"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_repr(self):
        node = LeafNode("p", "What a strange world", {"class": "primary"})
        self.assertEqual(
            node.__repr__(),
            "LeafNode(p, What a strange world, {'class': 'primary'})",
        )

        node = LeafNode("tag", "value", {"href": "html"})
        node2 = LeafNode("tag", "value", {"href": "html"})
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_to_html(self):
        node = LeafNode("tag", "value")
        node2 = LeafNode("tag", "value")
        self.assertEqual(node.to_html(), node2.to_html())

        node = LeafNode("p", "This is paragraph.")
        self.assertEqual(node.to_html(), "<p>This is paragraph.</p>")

        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

        node = LeafNode("tag", "value", {"href": "html"})
        node2 = LeafNode("tag", "value", {"href": "html"})
        self.assertEqual(node.to_html(), node2.to_html())


if __name__ == "__main__":
    unittest.main()

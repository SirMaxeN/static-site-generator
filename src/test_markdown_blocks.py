import unittest
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

        md = """
        This is **bolded** paragraph




        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        block_type: BlockType = block_to_block_type(
            "- Item 1\n- Item 2\n- Item 3")
        self.assertEqual(
            block_type,
            BlockType.UNORDERED_LIST
        )

        block_type: BlockType = block_to_block_type(
            "-Item 1\n- Item 2\n- Item 3")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "1. Item 1\n2. Item 2\n3. Item 3")
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST
        )

        block_type: BlockType = block_to_block_type(
            "1.Item 1\n2. Item 2\n3. Item 3")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "# Heading 1")
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

        block_type: BlockType = block_to_block_type(
            "## Heading 2")
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )
        block_type: BlockType = block_to_block_type(
            "### Heading 3")
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

        block_type: BlockType = block_to_block_type(
            "#### Heading 4")
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

        block_type: BlockType = block_to_block_type(
            "##### Heading 5")
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

        block_type: BlockType = block_to_block_type(
            "###### Heading 6")
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

        block_type: BlockType = block_to_block_type(
            "####### Not heading 7")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "######## Not heading 8")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "> Item 1\n> Item 2\n> Item 3")
        self.assertEqual(
            block_type,
            BlockType.QUOTE
        )

        block_type: BlockType = block_to_block_type(
            ">Item 1\n> Item 2\n> Item 3")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "``` Item 1\n Item``` 2\n Item 3```")
        self.assertEqual(
            block_type,
            BlockType.CODE
        )

        block_type: BlockType = block_to_block_type(
            "` Item 1\n Item``` 2\n Item 3")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "> Item 1\n Item``` 2\n Item 3")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )
        block_type: BlockType = block_to_block_type(
            "1. Item 1\n# Item``` 2\n Item 3")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "1 Item 1\n2 Item 2\n3 Item 3")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "1. Item 1\n2. Item 2\n3 Item 3")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "1 Item 1\n# Item``` 2\n Item 3")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

        block_type: BlockType = block_to_block_type(
            "text")
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )


if __name__ == "__main__":
    unittest.main()

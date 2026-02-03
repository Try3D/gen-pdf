#!/usr/bin/env python3
"""
Example 1: Simple Text Document
Demonstrates basic text rendering in a PDF
"""

from gen_pdf import Document, Page
from gen_pdf.blocks import TextBlock
from reportlab.lib.colors import HexColor

# Create a new page
page = Page(bg_color="#ffffff")

# Add some text blocks
page.add_block(
    TextBlock(
        "<b>Hello, Gen PDF!</b>",
        fontSize=28,
        textColor=HexColor("#1a1a1a"),
        spaceAfter=20,
    )
)

page.add_block(
    TextBlock(
        "This is a simple example showing how to create PDF documents with text.",
        fontSize=12,
        textColor=HexColor("#666666"),
        spaceAfter=12,
    )
)

page.add_block(
    TextBlock(
        "You can use <b>HTML tags</b> like <i>italic</i> and <u>underline</u> in your text!",
        fontSize=11,
        textColor=HexColor("#333333"),
    )
)

# Create document and add the page
doc = Document()
doc.add_page(page)

# Generate PDF
doc.generate("01_simple_text.pdf")
print("Generated: 01_simple_text.pdf")

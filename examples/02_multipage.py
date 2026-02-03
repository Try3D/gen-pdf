#!/usr/bin/env python3
"""
Example 2: Multi-page Document
Demonstrates creating a document with multiple pages
"""

from gen_pdf import Document, Page
from gen_pdf.blocks import TextBlock, SpacerBlock
from reportlab.lib.colors import HexColor

# Create first page
page1 = Page(bg_color="#ffffff")
page1.add_block(
    TextBlock(
        "<b>Page 1: Introduction</b>",
        fontSize=24,
        textColor=HexColor("#0066cc"),
        spaceAfter=20,
    )
)
page1.add_block(
    TextBlock(
        "This is the first page of a multi-page PDF document.",
        fontSize=12,
        textColor=HexColor("#333333"),
        spaceAfter=12,
    )
)
page1.add_block(
    TextBlock(
        "Gen PDF makes it easy to create professional-looking documents with multiple pages.",
        fontSize=11,
        textColor=HexColor("#666666"),
    )
)

# Create second page with a different background
page2 = Page(bg_color="#f0f0f0")
page2.add_block(
    TextBlock(
        "<b>Page 2: Another Page</b>",
        fontSize=24,
        textColor=HexColor("#cc0000"),
        spaceAfter=20,
    )
)
page2.add_block(
    TextBlock(
        "This page has a light gray background. Each page can have its own styling.",
        fontSize=12,
        textColor=HexColor("#333333"),
        spaceAfter=12,
    )
)

# Create third page
page3 = Page(bg_color="#ffffff")
page3.add_block(
    TextBlock(
        "<b>Page 3: Conclusion</b>",
        fontSize=24,
        textColor=HexColor("#009900"),
        spaceAfter=20,
    )
)
page3.add_block(
    TextBlock(
        "You can add as many pages as you need. Each page is independent and can have different layouts.",
        fontSize=12,
        textColor=HexColor("#333333"),
    )
)

# Create document and add all pages
doc = Document()
doc.add_page(page1)
doc.add_page(page2)
doc.add_page(page3)

# Generate PDF
doc.generate("02_multipage_document.pdf")
print("Generated: 02_multipage_document.pdf (3 pages)")

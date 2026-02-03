#!/usr/bin/env python3
"""
Example 3: Document with Tables
Demonstrates creating tables in PDF documents with color-coded indicators
"""

from build_pdf import Document, Page
from build_pdf.blocks import TextBlock, TableBlock, SpacerBlock
from reportlab.lib.colors import HexColor

# Create page
page = Page(bg_color="#ffffff")

page.add_block(
    TextBlock(
        "<b>Sales Report - Q1 2024</b>",
        fontSize=20,
        textColor=HexColor("#1a1a1a"),
        spaceAfter=20,
    )
)

# Create a table with sales data
# Note: Status column uses color-coded text instead of emojis
table_data = [
    ["Product", "Q1 Sales", "Growth", "Status"],
    ["Product A", "$50,000", "+15%", "Up"],
    ["Product B", "$35,000", "+8%", "Up"],
    ["Product C", "$42,000", "-5%", "Down"],
    ["Product D", "$28,000", "+22%", "Up"],
]

page.add_block(TableBlock(table_data, col_widths=[150, 120, 100, 100]))

page.add_block(SpacerBlock(width=100, height=20))

page.add_block(
    TextBlock(
        "<b>Summary</b>", fontSize=14, textColor=HexColor("#333333"), spaceAfter=10
    )
)

page.add_block(
    TextBlock(
        "Total Q1 revenue: <b>$155,000</b> with an average growth of <b>+10%</b>",
        fontSize=11,
        textColor=HexColor("#666666"),
    )
)

page.add_block(SpacerBlock(width=100, height=15))

page.add_block(
    TextBlock(
        "Color Legend:",
        fontSize=10,
        textColor=HexColor("#333333"),
        spaceAfter=8,
    )
)

page.add_block(
    TextBlock(
        "Up: Green (positive growth) | Down: Red (negative growth)",
        fontSize=9,
        textColor=HexColor("#666666"),
    )
)

# Create document and generate
doc = Document()
doc.add_page(page)
doc.generate("03_table_example.pdf")
print("Generated: 03_table_example.pdf")

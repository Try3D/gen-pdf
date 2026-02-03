#!/usr/bin/env python3
"""
Example 7: Font Showcase
Demonstrates all available fonts in the Gen PDF library.
Shows different font families, sizes, and styles.
"""

from build_pdf import Document, Page
from build_pdf.blocks import TextBlock, SpacerBlock
from reportlab.lib.colors import HexColor

# Create page
page = Page(bg_color="#ffffff")

page.add_block(SpacerBlock(width=100, height=20))

page.add_block(
    TextBlock(
        "<b>Font Showcase</b>",
        fontSize=26,
        textColor=HexColor("#1a1a1a"),
        spaceAfter=30,
        fontName="DMSans-Bold",
    )
)

# DM Sans font
page.add_block(
    TextBlock(
        "<b>DM Sans (Bold)</b>",
        fontSize=14,
        textColor=HexColor("#0066cc"),
        spaceAfter=8,
        fontName="DMSans-Bold",
    )
)

page.add_block(
    TextBlock(
        "This is DM Sans Bold - a geometric sans-serif font perfect for headers and titles.",
        fontSize=11,
        textColor=HexColor("#333333"),
        spaceAfter=15,
        fontName="DMSans-Regular",
    )
)

# Roboto font
page.add_block(
    TextBlock(
        "<b>Roboto (Regular)</b>",
        fontSize=14,
        textColor=HexColor("#009900"),
        spaceAfter=8,
        fontName="Roboto-Regular",
    )
)

page.add_block(
    TextBlock(
        "This is Roboto - a clean, modern sans-serif font that's highly readable on any device.",
        fontSize=11,
        textColor=HexColor("#333333"),
        spaceAfter=15,
        fontName="Roboto-Regular",
    )
)

# Poppins font
page.add_block(
    TextBlock(
        "<b>Poppins (Regular)</b>",
        fontSize=14,
        textColor=HexColor("#cc0000"),
        spaceAfter=8,
        fontName="Poppins-Regular",
    )
)

page.add_block(
    TextBlock(
        "This is Poppins - a geometric sans-serif with a friendly, approachable feel.",
        fontSize=11,
        textColor=HexColor("#333333"),
        spaceAfter=15,
        fontName="Poppins-Regular",
    )
)

# Open Sans font
page.add_block(
    TextBlock(
        "<b>Open Sans (Regular)</b>",
        fontSize=14,
        textColor=HexColor("#6600cc"),
        spaceAfter=8,
        fontName="OpenSans-Regular",
    )
)

page.add_block(
    TextBlock(
        "This is Open Sans - a humanist sans-serif optimized for legibility across devices.",
        fontSize=11,
        textColor=HexColor("#333333"),
        spaceAfter=15,
        fontName="OpenSans-Regular",
    )
)

# Lato font
page.add_block(
    TextBlock(
        "<b>Lato (Regular)</b>",
        fontSize=14,
        textColor=HexColor("#ff6600"),
        spaceAfter=8,
        fontName="Lato-Regular",
    )
)

page.add_block(
    TextBlock(
        "This is Lato - a warm, friendly sans-serif with excellent readability.",
        fontSize=11,
        textColor=HexColor("#333333"),
        fontName="Lato-Regular",
    )
)

# Create document and generate
doc = Document()
doc.add_page(page)
doc.generate("07_font_showcase.pdf")
print("Generated: 07_font_showcase.pdf")

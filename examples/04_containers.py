#!/usr/bin/env python3
"""
Example 4: Document with Containers and Layout
Demonstrates using containers for structured layouts
"""

from gen_pdf import Document, Page
from gen_pdf.blocks import TextBlock, ContainerBlock, SpacerBlock
from gen_pdf.styles import ContainerStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

# Create page
page = Page(bg_color="#ffffff")

page.add_block(
    TextBlock(
        "<b>Professional Report</b>",
        fontSize=22,
        textColor=HexColor("#1a1a1a"),
        spaceAfter=20,
    )
)

# Create a styled container
container_style = ContainerStyle(
    width=7 * inch,
    padding=20,
)

container = ContainerBlock(
    TextBlock(
        "This content is inside a container with custom styling and padding.",
        fontSize=11,
        textColor=HexColor("#333333"),
    ),
    style=container_style,
)

page.add_block(container)

page.add_block(SpacerBlock(width=100, height=20))

# Add footer
page.add_block(
    TextBlock(
        "<i>Generated with Gen PDF</i>", fontSize=9, textColor=HexColor("#999999")
    )
)

# Create document and generate
doc = Document()
doc.add_page(page)
doc.generate("04_container_example.pdf")
print("Generated: 04_container_example.pdf")

#!/usr/bin/env python3
"""
Example 6: Colored Pages
Demonstrates creating documents with colored page backgrounds.
Shows how each page can have its own unique color scheme.
"""

from build_pdf import Document, Page
from build_pdf.blocks import TextBlock, SpacerBlock
from reportlab.lib.colors import HexColor

# Create first page with blue background
page1 = Page(bg_color="#1e3a8a")  # Dark blue

page1.add_block(SpacerBlock(width=100, height=60))

page1.add_block(
    TextBlock(
        "<b>Dark Blue Theme</b>",
        fontSize=32,
        textColor=HexColor("#ffffff"),
        spaceAfter=35,
    )
)

page1.add_block(
    TextBlock(
        "This page has a dark blue background with white text. Each page can have its own color scheme.",
        fontSize=13,
        textColor=HexColor("#e0e7ff"),
        spaceAfter=20,
    )
)

page1.add_block(
    TextBlock("Perfect for:", fontSize=12, textColor=HexColor("#ffffff"), spaceAfter=10)
)

page1.add_block(
    TextBlock(
        "• Title pages<br/>• Section dividers<br/>• Branded covers",
        fontSize=11,
        textColor=HexColor("#c7d2fe"),
    )
)

# Create second page with green background
page2 = Page(bg_color="#166534")  # Dark green

page2.add_block(SpacerBlock(width=100, height=60))

page2.add_block(
    TextBlock(
        "<b>Dark Green Theme</b>",
        fontSize=32,
        textColor=HexColor("#ffffff"),
        spaceAfter=35,
    )
)

page2.add_block(
    TextBlock(
        "This page has a dark green background. Create visually distinct sections with different colors.",
        fontSize=13,
        textColor=HexColor("#dcfce7"),
        spaceAfter=20,
    )
)

page2.add_block(
    TextBlock("Great for:", fontSize=12, textColor=HexColor("#ffffff"), spaceAfter=10)
)

page2.add_block(
    TextBlock(
        "• Success pages<br/>• Verification pages<br/>• Completion certificates",
        fontSize=11,
        textColor=HexColor("#bbf7d0"),
    )
)

# Create third page with purple background
page3 = Page(bg_color="#5b21b6")  # Purple

page3.add_block(SpacerBlock(width=100, height=60))

page3.add_block(
    TextBlock(
        "<b>Purple Theme</b>", fontSize=32, textColor=HexColor("#ffffff"), spaceAfter=15
    )
)

page3.add_block(
    TextBlock(
        "This page has a purple background. Mix and match colors to create unique document layouts.",
        fontSize=13,
        textColor=HexColor("#f3e8ff"),
        spaceAfter=20,
    )
)

page3.add_block(
    TextBlock("Use cases:", fontSize=12, textColor=HexColor("#ffffff"), spaceAfter=10)
)

page3.add_block(
    TextBlock(
        "• Premium reports<br/>• Executive summaries<br/>• Special announcements",
        fontSize=11,
        textColor=HexColor("#e9d5ff"),
    )
)

# Create fourth page with teal background
page4 = Page(bg_color="#134e4a")  # Teal

page4.add_block(SpacerBlock(width=100, height=60))

page4.add_block(
    TextBlock(
        "<b>Teal Theme</b>", fontSize=32, textColor=HexColor("#ffffff"), spaceAfter=15
    )
)

page4.add_block(
    TextBlock(
        "This page has a teal background. Create professional multi-page documents with distinct visual chapters.",
        fontSize=13,
        textColor=HexColor("#ccfbf1"),
        spaceAfter=20,
    )
)

page4.add_block(
    TextBlock("Perfect for:", fontSize=12, textColor=HexColor("#ffffff"), spaceAfter=10)
)

page4.add_block(
    TextBlock(
        "• Chapter dividers<br/>• Status updates<br/>• Progress reports",
        fontSize=11,
        textColor=HexColor("#99f6e4"),
    )
)

# Create fifth page with red/orange background
page5 = Page(bg_color="#b91c1c")  # Red

page5.add_block(SpacerBlock(width=100, height=60))

page5.add_block(
    TextBlock(
        "<b>Red Theme</b>", fontSize=32, textColor=HexColor("#ffffff"), spaceAfter=15
    )
)

page5.add_block(
    TextBlock(
        "This page has a red background. Use bold colors to draw attention to important information.",
        fontSize=13,
        textColor=HexColor("#fee2e2"),
        spaceAfter=20,
    )
)

page5.add_block(
    TextBlock("Use for:", fontSize=12, textColor=HexColor("#ffffff"), spaceAfter=10)
)

page5.add_block(
    TextBlock(
        "• Alert pages<br/>• Important notices<br/>• Critical information",
        fontSize=11,
        textColor=HexColor("#fecaca"),
    )
)

# Create document with all colored pages
doc = Document()
doc.add_page(page1)
doc.add_page(page2)
doc.add_page(page3)
doc.add_page(page4)
doc.add_page(page5)

doc.generate("06_colored_pages.pdf")
print("Generated: 06_colored_pages.pdf (5 pages with different colors)")

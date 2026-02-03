#!/usr/bin/env python3
"""
Example 5: Invoice Template
Demonstrates a real-world use case - creating an invoice PDF
"""

from build_pdf import Document, Page
from build_pdf.blocks import TextBlock, TableBlock, SpacerBlock
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

# Create page with light blue background
page = Page(bg_color="#f9fbff")

# Header
page.add_block(SpacerBlock(width=100, height=20))

page.add_block(
    TextBlock(
        "<b>INVOICE</b>", fontSize=28, textColor=HexColor("#0066cc"), spaceAfter=20
    )
)

page.add_block(
    TextBlock(
        "Invoice #2024-001 | Date: February 3, 2024",
        fontSize=10,
        textColor=HexColor("#666666"),
        spaceAfter=35,
    )
)

# Company info
page.add_block(
    TextBlock(
        "<b>Bill To:</b>",
        fontSize=11,
        textColor=HexColor("#333333"),
        spaceAfter=8,
    )
)

page.add_block(
    TextBlock(
        "Acme Corporation<br/>123 Business Street<br/>New York, NY 10001",
        fontSize=10,
        textColor=HexColor("#666666"),
        spaceAfter=30,
    )
)

# Items table
items_data = [
    ["Description", "Qty", "Unit Price", "Total"],
    ["Professional Services", "40", "$150.00", "$6,000.00"],
    ["Software License (Annual)", "1", "$2,500.00", "$2,500.00"],
    ["Support & Maintenance", "1", "$1,000.00", "$1,000.00"],
]

page.add_block(TableBlock(items_data, col_widths=[250, 60, 100, 100]))

page.add_block(SpacerBlock(width=100, height=20))

# Summary
page.add_block(
    TextBlock(
        "<b>Subtotal:</b> $9,500.00",
        fontSize=11,
        textColor=HexColor("#333333"),
        spaceAfter=5,
    )
)

page.add_block(
    TextBlock(
        "<b>Tax (10%):</b> $950.00",
        fontSize=11,
        textColor=HexColor("#333333"),
        spaceAfter=10,
    )
)

page.add_block(
    TextBlock(
        "<b>Total Due: $10,450.00</b>",
        fontSize=13,
        textColor=HexColor("#0066cc"),
        spaceAfter=20,
    )
)

# Footer
page.add_block(
    TextBlock(
        "Thank you for your business!<br/>Payment terms: Net 30 days",
        fontSize=9,
        textColor=HexColor("#999999"),
    )
)

# Create document and generate
doc = Document()
doc.add_page(page)
doc.generate("05_invoice_example.pdf")
print("Generated: 05_invoice_example.pdf")

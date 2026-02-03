# Gen PDF Examples

This directory contains 7 example scripts demonstrating how to use the Gen PDF library to generate professional PDF documents.

## Examples

### 1. Simple Text (`01_simple_text.py`)
**Output:** `01_simple_text.pdf`

Basic example showing how to create a simple PDF with text blocks. Demonstrates:
- Creating a page with a background color
- Adding text blocks with HTML formatting
- Using colors and font sizes
- Generating the final PDF

```bash
python3 01_simple_text.py
```

### 2. Multi-page Document (`02_multipage.py`)
**Output:** `02_multipage_document.pdf` (3 pages)

Shows how to create documents with multiple pages. Demonstrates:
- Creating multiple pages with different content
- Setting different background colors per page
- Building a complete document with multiple pages
- Using the Document API to add pages

```bash
python3 02_multipage.py
```

### 3. Tables (`03_tables.py`)
**Output:** `03_table_example.pdf`

Demonstrates table creation for structured data. Shows:
- Creating data tables with headers and rows
- Setting column widths
- Combining tables with text content
- Creating professional data layouts

```bash
python3 03_tables.py
```

### 4. Containers and Layout (`04_containers.py`)
**Output:** `04_container_example.pdf`

Shows how to use containers for advanced layouts. Demonstrates:
- Creating styled containers with padding
- Using ContainerStyle for custom styling
- Nesting content within containers
- Building structured page layouts

```bash
python3 04_containers.py
```

### 5. Invoice Template (`05_invoice.py`)
**Output:** `05_invoice_example.pdf`

Real-world example of creating an invoice PDF. Demonstrates:
- Building a complete invoice document
- Using tables for line items
- Creating summaries and calculations
- Professional styling and layout
- Business document creation

```bash
python3 05_invoice.py
```

### 6. Colored Pages (`06_colored_pages.py`)
**Output:** `06_colored_pages.pdf` (5 pages)

Demonstrates creating documents with colored page backgrounds. Shows:
- Creating pages with custom background colors
- Using contrasting text colors for readability
- Building multi-page documents with different color schemes
- Using colors for visual hierarchy and section division
- 5 different color themes: Blue, Green, Purple, Teal, and Red

```bash
python3 06_colored_pages.py
```

### 7. Font Showcase (`07_font_showcase.py`)
**Output:** `07_font_showcase.pdf`

Demonstrates all available fonts in the Gen PDF library. Shows:
- Using different font families (DM Sans, Roboto, Poppins, Open Sans, Lato)
- Font styling and sizing
- How different fonts work for different purposes
- Color coordination with fonts

```bash
python3 07_font_showcase.py
```

## Running All Examples

To run all examples at once:

```bash
for f in *.py; do python3 "$f"; done
```

## Installation

Make sure Gen PDF is installed in your environment:

```bash
pip install -e ..
```

## Output

All examples generate PDF files in the same directory:
- `01_simple_text.pdf` (1.9 KB)
- `02_multipage_document.pdf` (2.9 KB) - 3 pages
- `03_table_example.pdf` (2.2 KB)
- `04_container_example.pdf` (1.8 KB)
- `05_invoice_example.pdf` (2.3 KB)
- `06_colored_pages.pdf` (4.8 KB) - 5 pages with different colors
- `07_font_showcase.pdf` (78 KB) - Shows all available fonts

## Features Used

| Feature | 01 | 02 | 03 | 04 | 05 | 06 | 07 |
|---------|----|----|----|----|----|----|-----|
| TextBlock | Y | Y | Y | Y | Y | Y | Y |
| SpacerBlock | - | - | Y | Y | Y | Y | Y |
| TableBlock | - | - | Y | - | Y | - | - |
| ContainerBlock | - | - | - | Y | - | - | - |
| Multiple Pages | - | Y | - | - | - | Y | - |
| Colored Backgrounds | Y | Y | Y | Y | Y | Y | Y |
| Custom Colors | Y | Y | Y | Y | Y | Y | Y |
| HTML Formatting | Y | Y | Y | Y | Y | Y | Y |
| Font Selection | - | - | - | - | - | - | Y |

## API Reference

### Creating a Document

```python
from gen_pdf import Document, Page

# Method 1: Manual
doc = Document()
page = Page(bg_color="#ffffff")
doc.add_page(page)
doc.generate("output.pdf")

# Method 2: Using DocumentBuilder
from gen_pdf import DocumentBuilder
builder = DocumentBuilder()
builder.add_page(page)
builder.generate("output.pdf")
```

### Adding Content to a Page

```python
from gen_pdf.blocks import TextBlock, TableBlock, SpacerBlock, ContainerBlock

page.add_block(TextBlock("Hello World", fontSize=14))
page.add_block(SpacerBlock(width=100, height=20))
page.add_block(TableBlock([["Col1", "Col2"], ["Data1", "Data2"]]))
```

### Styling

```python
from reportlab.lib.colors import HexColor

TextBlock("Text", fontSize=12, textColor=HexColor("#0066cc"))
```

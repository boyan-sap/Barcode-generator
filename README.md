📦 Warehouse Position Barcode Generator
This tool generates barcode labels in PDF format for warehouse positions based on an Excel input file. Ideal for organizing and marking storage locations efficiently.

🛠 Features
Reads warehouse positions from an Excel file (.xlsx)

Automatically generates barcodes (Code128 format)

Exports ready-to-print barcode labels to PDF

Customizable layout and label size

📂 Input
Excel file with a list of positions in one column (e.g., positions.xlsx):

| Position      |
|---------------|
| A1-01-01      |
| A1-01-02      |
| B2-03-05      |
...


🔧 Requirements
Python 3.7+

Libraries:

pandas

reportlab

openpyxl

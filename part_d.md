## Automatic CSV Delimiter Detection and JSON Conversion

---

# 1️⃣ Exact Prompt Used

```
Write a Python script that reads a CSV file, automatically detects the delimiter
(comma, tab, semicolon, or pipe), and converts the CSV data into a JSON file.
Use Python's csv module if appropriate and handle delimiter detection.
The output JSON file should contain a list of dictionaries representing rows.
Also include example usage.
```

---

# 2️⃣ AI-Generated Code

```python
import csv
import json
from pathlib import Path

def csv_to_json(input_file, output_file):

    with open(input_file, "r", newline="") as f:
        sample = f.read(1024)
        f.seek(0)

        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(sample, delimiters=[",", "\t", ";", "|"])

        reader = csv.DictReader(f, dialect=dialect)
        rows = list(reader)

    with open(output_file, "w") as f:
        json.dump(rows, f, indent=4)


if __name__ == "__main__":
    input_path = "data.csv"
    output_path = "output.json"

    csv_to_json(input_path, output_path)

    print("CSV successfully converted to JSON.")
```

---

# 3️⃣ Testing the Script

## Test File 1 — Comma Delimited CSV

### Input File

`sales.csv`

```
date,product,qty,price
2025-01-10,Laptop,2,50000
2025-01-10,Mouse,5,500
```

### Generated JSON

```json
[
    {
        "date": "2025-01-10",
        "product": "Laptop",
        "qty": "2",
        "price": "50000"
    },
    {
        "date": "2025-01-10",
        "product": "Mouse",
        "qty": "5",
        "price": "500"
    }
]
```

---

## Test File 2 — Semicolon Delimited CSV

### Input File

`inventory.csv`

```
product;qty;price
Keyboard;3;1200
Monitor;1;22000
```

### Generated JSON

```json
[
    {
        "product": "Keyboard",
        "qty": "3",
        "price": "1200"
    },
    {
        "product": "Monitor",
        "qty": "1",
        "price": "22000"
    }
]
```

---

# 4️⃣ Critical Evaluation (≈200 Words)

The AI-generated script successfully performs automatic delimiter detection and CSV-to-JSON conversion using Python’s `csv` module. One of the strongest aspects of the solution is the use of `csv.Sniffer()`, which analyzes a sample of the input file to determine the correct delimiter. This allows the program to handle multiple CSV formats such as comma-, tab-, semicolon-, and pipe-delimited files without requiring manual configuration. The use of `csv.DictReader` is also appropriate because it converts each CSV row directly into a dictionary, making it easy to serialize the data into JSON using `json.dump()`.

The script is concise and readable, making it suitable for beginner and intermediate Python users. It also demonstrates good file-handling practices by using `with open(...)`, which ensures files are properly closed after processing.

However, the script does not handle several potential edge cases. For example, it assumes the CSV file contains a valid header row. If the file lacks headers or contains inconsistent columns, the script may fail or produce incorrect output. It also lacks error handling for situations such as missing files, encoding errors, or malformed CSV content.

Improvements could include adding exception handling (`try/except`), validating headers, allowing command-line arguments for file paths, and supporting large files through streaming rather than loading all rows into memory. Overall, the AI produced a functional and well-structured baseline solution.

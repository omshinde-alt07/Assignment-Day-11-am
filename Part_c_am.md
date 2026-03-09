# Q1 — Conceptual

## Difference Between `json.load()` and `json.loads()`

Both functions belong to Python’s **json module** and are used to convert JSON data into Python objects such as dictionaries or lists. The difference lies in **where the JSON data comes from**.

---

## `json.load()`

### Definition

`json.load()` reads JSON data **directly from a file object** and converts it into a Python dictionary or list.

### Syntax

```python
json.load(file_object)
```

### When to Use

Use `json.load()` when the JSON data is stored in a **file on disk**.

### Example

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
```

### Real-World Example

A data analyst loads a configuration file or report stored as JSON.

Example file:

```
config.json
```

```json
{
  "database": "sales_db",
  "timeout": 30
}
```

Using `json.load()` allows the program to read the file and convert it into a Python dictionary.

---

## `json.loads()`

### Definition

`json.loads()` converts a **JSON formatted string** into a Python object.

### Syntax

```python
json.loads(json_string)
```

### When to Use

Use `json.loads()` when JSON data is received as a **string**, such as:

* API responses
* web requests
* message queues

### Example

```python
import json

json_string = '{"name": "Laptop", "price": 50000}'

data = json.loads(json_string)

print(data["name"])
```

### Real-World Example

When calling a **REST API**, the response often comes as a JSON string.
`json.loads()` converts that string into a Python dictionary for further processing.

---

## Summary

| Function       | Input       | Use Case                                       |
| -------------- | ----------- | ---------------------------------------------- |
| `json.load()`  | File object | Reading JSON files                             |
| `json.loads()` | JSON string | Parsing JSON strings (API responses, messages) |

---

# Q2 — Coding

## Function: `find_large_files(directory, size_mb)`

### Requirements

* Use `pathlib`
* Search recursively
* Return files larger than `size_mb`
* Return format:

```
[
    ("filename", size_in_mb)
]
```

* Sort results by **file size descending**

---

## Implementation

```python
from pathlib import Path

def find_large_files(directory, size_mb):

    path = Path(directory)
    results = []

    for file in path.rglob("*"):
        if file.is_file():
            size = file.stat().st_size / (1024 * 1024)

            if size > size_mb:
                results.append((file.name, round(size, 2)))

    results.sort(key=lambda x: x[1], reverse=True)

    return results
```

---

## Example Usage

```python
files = find_large_files("data_folder", 10)

for name, size in files:
    print(name, size, "MB")
```

Example Output:

```
dataset.csv 52.3 MB
backup.json 18.7 MB
logs.txt 12.1 MB
```

---

# Q3 — Debug / Analyze

## Original Code

```python
def merge_csv_files(file_list):
    all_data = []
    for filename in file_list:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                all_data.append(row)
    
    with open("merged.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(all_data)
    
    return len(all_data)
```

---

# Problems in the Code

### 1️⃣ Missing `newline=''`

When writing CSV files on Windows, not specifying `newline=''` causes **blank rows between records**.

---

### 2️⃣ Duplicate Header Rows

Each CSV file likely contains its own header row.
The current code adds every header, causing duplicates in the merged file.

---

### 3️⃣ Missing Import

The code uses `csv.reader` and `csv.writer` but does not include:

```python
import csv
```

---

# Corrected Implementation

```python
import csv

def merge_csv_files(file_list):

    all_data = []
    header_saved = False

    for filename in file_list:
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)

            header = next(reader)

            if not header_saved:
                all_data.append(header)
                header_saved = True

            for row in reader:
                all_data.append(row)

    with open("merged.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(all_data)

    return len(all_data)
```

---

# Improvements Made

### Proper CSV Handling

Using:

```python
newline=''
```

prevents blank rows when writing CSV files.

---

### Header Management

Only the **first file’s header** is kept.
Headers from subsequent files are skipped.

---

### Correct Import

Added:

```python
import csv
```

so that the CSV module functions correctly.

---

# Example Usage

```python
files = ["sales1.csv", "sales2.csv", "sales3.csv"]

rows = merge_csv_files(files)

print("Total rows merged:", rows)
```

---


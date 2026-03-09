import csv
import json
from pathlib import Path
from datetime import datetime

unique_rows = []
seen = set()
revenue = {}

files = list(Path(".").glob("data*.csv"))

for file in files:
    with open(file, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            key = (row["date"], row["product"], row["qty"], row["price"])

            if key not in seen:
                seen.add(key)
                unique_rows.append(row)

                qty = int(row["qty"])
                price = float(row["price"])
                product = row["product"]

                revenue[product] = revenue.get(product, 0) + qty * price


unique_rows.sort(key=lambda x: x["date"])


with open("merged_sales.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "product", "qty", "price"])
    writer.writeheader()
    writer.writerows(unique_rows)


total_revenue = sum(revenue.values())

report = {
    "metadata": {
        "files_processed": len(files),
        "total_rows": len(unique_rows),
        "total_revenue": total_revenue,
        "generated_at": datetime.now().isoformat()
    },
    "revenue_by_product": revenue
}

with open("revenue_summary.json", "w") as f:
    json.dump(report, f, indent=4)

print("Processing completed.")
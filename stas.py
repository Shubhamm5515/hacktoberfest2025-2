#!/usr/bin/env python3
# csv_stats.py
import csv
import sys
from statistics import mean

def is_float(s):
    try:
        float(s)
        return True
    except:
        return False

def summarize(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        numeric_cols = {}
        row_count = 0
        for row in reader:
            row_count += 1
            for k, v in row.items():
                if v is None or v.strip()=="":
                    continue
                if is_float(v):
                    numeric_cols.setdefault(k, []).append(float(v))
        print(f"Rows: {row_count}")
        if not numeric_cols:
            print("No numeric columns found.")
        else:
            for col, vals in numeric_cols.items():
                print(f"- {col}: count={len(vals)}, mean={mean(vals):.4g}, min={min(vals)}, max={max(vals)}")

def main(argv):
    if len(argv) != 2:
        print("Usage: csv_stats.py path/to/file.csv")
        return
    summarize(argv[1])

if __name__ == "__main__":
    main(sys.argv)

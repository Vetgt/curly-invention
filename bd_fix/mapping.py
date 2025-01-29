#!/usr/bin/env python3
import sys

# Input: CSV data
# Output: Key-value pairs for HeartDisease -> (age, cholesterol)

for line in sys.stdin:
    try:
        data = line.strip().split(',')
        if len(data) != 7 or data[0] == "Age":  # Skip header
            continue
        age = data[0]
        cholesterol = data[1]
        heart_disease = data[-1]
        print(f"{heart_disease}\t{age},{cholesterol}")
    except Exception as e:
        pass  # Skip any problematic lines


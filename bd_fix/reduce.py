#!/usr/bin/env python3
import sys

current_key = None
age_list = []
cholesterol_list = []

for line in sys.stdin:
    try:
        key, values = line.strip().split("\t")
        age, cholesterol = map(int, values.split(","))

        if current_key == key:
            age_list.append(age)
            cholesterol_list.append(cholesterol)
        else:
            if current_key is not None:
                # Calculate min, max, and average age
                min_age = min(age_list)
                max_age = max(age_list)
                avg_age = sum(age_list) / len(age_list) if age_list else 0
                
                # Calculate min, max, and average cholesterol
                min_cholesterol = min(cholesterol_list)
                max_cholesterol = max(cholesterol_list)
                avg_cholesterol = sum(cholesterol_list) / len(cholesterol_list) if cholesterol_list else 0
                
                # Print current key with age and cholesterol statistics and lists
                print(f"{current_key}\tCount: {len(age_list)}\tMin Age: {min_age}\tMax Age: {max_age}\tAvg Age: {avg_age:.2f}\tAge List: {age_list}\tMin Cholesterol: {min_cholesterol}\tMax Cholesterol: {max_cholesterol}\tAvg Cholesterol: {avg_cholesterol:.2f}\tCholesterol List: {cholesterol_list}")
            
            current_key = key
            age_list = [age]
            cholesterol_list = [cholesterol]
    except Exception as e:
        pass  # Skip problematic lines

# Output the last key
if current_key is not None:
    min_age = min(age_list)
    max_age = max(age_list)
    avg_age = sum(age_list) / len(age_list) if age_list else 0
    
    min_cholesterol = min(cholesterol_list)
    max_cholesterol = max(cholesterol_list)
    avg_cholesterol = sum(cholesterol_list) / len(cholesterol_list) if cholesterol_list else 0
    
    print(f"{current_key}\tCount: {len(age_list)}\tMin Age: {min_age}\tMax Age: {max_age}\tAvg Age: {avg_age:.2f}\tAge List: {age_list}\tMin Cholesterol: {min_cholesterol}\tMax Cholesterol: {max_cholesterol}\tAvg Cholesterol: {avg_cholesterol:.2f}\tCholesterol List: {cholesterol_list}")

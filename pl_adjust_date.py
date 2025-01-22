"""
pl_adjust_date.py

Adjusts the due dates in PrairieLearn's infoAssessment.json files
"""

import sys
import json

if len(sys.argv) < 3:
    print("Usage: pl_adjust_date.py file_name start_date")
    exit()

filename = sys.argv[1]
start_date = sys.argv[2] 

#
# Open and read the JSON file
#
with open(filename, 'r') as f:
    data = json.load(f)

#
# Demonstration code
#


# print all data (just for demonstration)
print("All data")
print(data)

# print the start date for the first access rule (just for demonstration)
print("---")
print(f"First start date: {data['allowAccess'][0]['startDate']}")


#
# Write JSON to file
#


# (Append "safe" to filename so the original file
#  doesn't get clobbered during development.)
with open(f"{filename}.safe", "w") as outfile:
    outfile.write(json.dumps(data, indent=2))

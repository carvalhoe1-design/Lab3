# CIS-117 Lab3
# Reads country_full.csv and writes one CSV per region with only name and region
# Uses try/except to handle file errors
# Everett Carvalho
# Worked individually

import csv

regions = {}

# Reading part
try:
    with open("country_full.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            name = row[0]
            region = row[5]
            if region == "":
                region = "Unknown"
            if region not in regions:
                regions[region] = []
            regions[region].append([name, region])
except FileNotFoundError:
    print("Error: country_full.csv was not found")
except PermissionError:
    print("Error: no permission to read country_full.csv")
except IOError as e:
    print("Error reading file:", e)

# Writing part
for region in regions:
    filename = region + ".csv"
    try:
        with open(filename, "w", newline="", encoding="utf-8") as out:
            writer = csv.writer(out)
            writer.writerow(["Name", "Region"])
            writer.writerows(regions[region])
        print("Wrote", len(regions[region]), "countries to", filename)
    except PermissionError:
        print("Error: no permission to write", filename)
    except IOError as e:
        print("Error writing", filename, ":", e)

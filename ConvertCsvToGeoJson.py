import sys
import csv
import json
import os
# Check for command-line arguments
if len(sys.argv) != 3:
    print("Usage: python ConvertCsvToGeoJson.py input.csv output.json")
    sys.exit(1)

csv_file = sys.argv[1]
out_file = sys.argv[2]

# Check if the input CSV file exists
if not os.path.exists(csv_file):
    print(f"Input file '{csv_file}' does not exist.")
    sys.exit(1)

# Read data from the input CSV file
data = []
with open(csv_file, 'r') as input_file:
    csv_reader = csv.DictReader(input_file)
    for row in csv_reader:
        data.append(row)

# Transform the data to GeoJSON format
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "id": d.get("id", d["Id"]),
                "RegionId": d.get("RegionId", d["RegionId"]),  # Adjust the field name as needed
                "RegionName": d.get("RegionName",d["RegionName"]),
                "DEOName": d.get("DEOName",d["DEOName"]),
                "Longitude": d.get("Longitude",d["Longitude"]),
                "Latitude": d.get("Latitude",d["Latitude"])
            },
            "geometry": {
                "type": "Point",
                "coordinates": [float(d["Longitude"]), float(d["Latitude"])],
            },
        }
        for d in data
    ]
}

# Write the GeoJSON data to the output file
with open(out_file, 'w') as output_file:
    json.dump(geojson, output_file)

print("Conversion completed successfully.")

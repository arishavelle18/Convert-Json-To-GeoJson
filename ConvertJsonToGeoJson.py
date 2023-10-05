import sys
from os.path import exists
import json

# Check for command-line arguments
if len(sys.argv) != 3:
    print("Usage: python ConvertJsonToGeoJson.py input.json output.json")
    sys.exit(1)

in_file = sys.argv[1]
out_file = sys.argv[2]

# Check if the input file exists
if not exists(in_file):
    print(f"Input file '{in_file}' does not exist.")
    sys.exit(1)

# Read data from the input JSON file
with open(in_file, 'r') as input_file:
    data = json.load(input_file)

# Transform the data to GeoJSON format
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": d,
            "geometry": {
                "coordinates": [float(d["longitude"]),float(d["latitude"])],
                "type": "Point",
            },
        }
        for d in data["data"]
    ]
}
print(data)
# Write the GeoJSON data to the output file
with open(out_file, 'w') as output_file:
    json.dump(geojson, output_file)

print("Conversion completed successfully.")
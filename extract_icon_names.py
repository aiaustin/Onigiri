import re

# Input and output paths
input_file = r".\Onigiri\__init__.py"
output_file = r".\icon_ids.txt"

# Regular expression pattern to match variables ending with _icon_id and their string values
pattern = r'(\w+_icon)\s*=\s*(?:"([^"]*)"|\'([^\']*)\')'

icon_ids = set()

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            var_name = match.group(1)
            str_value = match.group(2) or match.group(3)  # Get value from either double or single quotes
            if str_value:
                icon_ids.add(str_value)

pattern = r'^\s+icon_value\s*=\s*get_icon_id\(\"(\w+)\"\)'

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            # Extract the string value
            icon_id = match.group(0).split('"')[1]
            icon_ids.add(icon_id)

# Sort the unique values
icon_ids = sorted(list(set(icon_ids)))

# Write to output file
with open(output_file, 'w', encoding='utf-8') as f:
    for icon_id in icon_ids:
        f.write("\""+icon_id + '\",\n')

print(f"Found {len(icon_ids)} unique icon IDs and saved to {output_file}")

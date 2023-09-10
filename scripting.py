import json

# Read the JSON file
with open('all_decos.json', 'r') as file:
    data = json.load(file)

# Extract skill names
skill_names = list(data['decos'].keys())

# Convert list to JSON format and write it to an output file
with open('output.json', 'w') as file:
    json.dump(skill_names, file, indent=4)

# Optional: Print the result to the console
print(json.dumps(skill_names, indent=4))

import pandas as pd
import ipaddress
import re

# --- Constants ---
TAG_COLORS = [
    "red", "green", "blue", "yellow", "cyan", "magenta", "gray", "black",
    "orange", "purple", "white", "lime", "olive", "teal", "maroon"
]
used_tags = {}

# --- Helper Functions ---
def slugify(text):
    """Sanitize description to use in object name."""
    return re.sub(r'[^a-zA-Z0-9]+', '-', text.strip()).strip('-').upper()

def is_fqdn(value):
    return not any(char.isdigit() for char in value.split('.')[0])

def is_cidr(value):
    try:
        ipaddress.IPv4Network(value, strict=False)
        return '/' in value
    except ValueError:
        return False

def is_ip(value):
    try:
        ipaddress.IPv4Address(value)
        return True
    except ValueError:
        return False

def generate_standardized_name(company, obj_type, description, index):
    base = slugify(description) if description else f"OBJ{index+1}"
    return f"{company.upper()}-{obj_type.upper()}-{base}"

def assign_tag_color(tag):
    if tag not in used_tags:
        used_tags[tag] = TAG_COLORS[len(used_tags) % len(TAG_COLORS)]
    return used_tags[tag]

# --- Main CLI Builder ---
def generate_cli_commands(df):
    all_cmds = []
    tag_defs = set()

    for idx, row in df.iterrows():
        address = row['ip/fqdn/network address']
        obj_type = row['type']
        description = row.get('description', '')
        company = row['company']
        tags = str(row.get('tags', '')).split(',')

        std_name = generate_standardized_name(company, obj_type, description, idx)
        commands = ["configure"]

        # Determine address type
        if is_fqdn(address):
            commands.append(f"set address {std_name} fqdn {address}")
        elif is_cidr(address) or is_ip(address):
            commands.append(f"set address {std_name} ip-netmask {address}")
        else:
            print(f"⚠️ Skipping invalid address: {address}")
            continue

        # Add description
        if description:
            commands.append(f"set address {std_name} description \"{description}\"")

        # Handle tags
        tag_list = []
        for tag in tags:
            tag = tag.strip()
            if tag:
                color = assign_tag_color(tag)
                tag_defs.add(f"set tag {tag} color {color}")
                tag_list.append(tag)
        if tag_list:
            commands.append(f"set address {std_name} tag [ {' '.join(tag_list)} ]")

        commands.append("commit")
        all_cmds.append("\n".join(commands) + "\n")

    # Tag definitions
    if tag_defs:
        all_cmds.insert(0, "\n".join(sorted(tag_defs)) + "\n")

    return all_cmds

# --- File Paths ---
excel_file = r"C:\Users\thoug\Desktop\Desktop01\address_objects.xlsx.xlsx"        # Input Excel file
output_file = "palo_alto_cli_output.txt"     # Output CLI file

# --- Run Script ---
df = pd.read_excel(excel_file)
cli_blocks = generate_cli_commands(df)

with open(output_file, "w") as f:
    for block in cli_blocks:
        f.write(block + "\n")

print(f"✅ CLI commands written to {output_file}")

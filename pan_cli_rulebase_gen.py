import pandas as pd

# Define input and output paths
input_file = r'C:\Users\thoug\Downloads\rules.xlsx'
output_file = 'output_file.txt'

# Load the Excel file
df = pd.read_excel(input_file)

# Clean string for use in rule name only
def normalize_for_rule_name(value):
    return str(value).strip().replace(" ", "_").replace("/", "_").lower()

# Store CLI commands
all_cmds = []

for _, row in df.iterrows():
    # Extract raw values (not cleaned)
    env = str(row['env']).strip()
    direction = str(row['direction']).strip()
    src_zone = str(row['source zone']).strip()
    src_net = str(row['source network']).strip()
    dst_zone = str(row['destination zone']).strip()
    dst_net = str(row['destination network']).strip()
    service = str(row['service application']).strip()
    action = str(row['action']).strip()
    log = str(row['log']).strip()
    description = str(row['description']).strip()
    tag = str(row['tag']).strip()
    purpose = str(row['purpose']).strip()
    device_group = str(row['device-group-name']).strip()

    # Use cleaned values only for the rule name
    rule_name = f"{normalize_for_rule_name(env)}_{normalize_for_rule_name(direction)}_" \
                f"{normalize_for_rule_name(src_net)}_to_{normalize_for_rule_name(dst_net)}_" \
                f"{normalize_for_rule_name(service)}_{normalize_for_rule_name(purpose)}"

    # Construct CLI commands using original values
    cmds = [
        "configure",
        f"set device-group {device_group} pre-rulebase security rules {rule_name} from any",
        f"set device-group {device_group} pre-rulebase security rules {rule_name} to any",
        f"set device-group {device_group} pre-rulebase security rules {rule_name} source shared/{src_net}",
        f"set device-group {device_group} pre-rulebase security rules {rule_name} destination shared/{dst_net}",
        f"set device-group {device_group} pre-rulebase security rules {rule_name} service shared/{service}",
        f"set device-group {device_group} pre-rulebase security rules {rule_name} application any",
        f"set device-group {device_group} pre-rulebase security rules {rule_name} action {action}",
        f"set device-group {device_group} pre-rulebase security rules {rule_name} log-start yes",
        f"set device-group {device_group} pre-rulebase security rules {rule_name} log-end yes",
        f'set device-group {device_group} pre-rulebase security rules {rule_name} description "{description}"',
        f"set device-group {device_group} pre-rulebase security rules {rule_name} tag {tag}",
        "commit",
        ""  # Empty line for separation
    ]

    # Add to the list and print
    all_cmds.extend(cmds)
    for cmd in cmds:
        print(cmd)

# Write to output file
with open(output_file, 'w') as f:
    f.write("\n".join(all_cmds))

print(f"\n✅ All commands written to {output_file}")

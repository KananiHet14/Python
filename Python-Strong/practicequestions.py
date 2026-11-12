import csv 

def process_packages(*packages):
    """Takes an arbitrary number of package strings, slices them, and returns a valid list of dictionaries."""
    valid_packages = []
    for index,pkg in enumerate(packages, start=1):
        if (len(pkg) < 3):
            continue
        sliced_prefix = pkg[0:3]
        valid_packages.append({
            "ID": index, 
            "Name": pkg, 
            "Prefix": sliced_prefix
        })
    return valid_packages
my_list = []
with open("cmn.csv" , "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        my_list.append(row["LibraryName"])
processed_data = process_packages(*my_list)
if processed_data:
    headers = processed_data[0].keys()
    with open("clean_env.csv" , "w" , newline="") as outfile:
        writer = csv.DictWriter(outfile , fieldnames=headers)
        writer.writeheader()
        writer.writerows(processed_data)
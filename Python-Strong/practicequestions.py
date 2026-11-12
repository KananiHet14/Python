import csv 
import sys

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


def calculate_threat(n):
    if((n==0) or (n==1)):
        return 1
    else:
        return n*calculate_threat(n-1)
def log_attack(timestamp="00:00", **details):
    """must doc string"""
    pin = sys.argv[1]
    if not (int(pin) ^ 128) != 0:
        sys.exit("wrong pin")
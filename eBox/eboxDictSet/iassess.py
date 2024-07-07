def parse_and_display_address(address):
    details = address.split(',')

    labels = ["Door-no", "Street", "Area", "City", "State", "Zipcode", "Country"]

    address_dict = {label: detail for label, detail in zip(labels, details)}

    for label, detail in address_dict.items():
        print(f"{label}:{detail}")

input_address = input()

# parse_and_display_address(input_address)

def check_sets(set1, set2):
    set1 = set(map(int, set1.split(',')))
    set2 = set(map(int, set2.split(',')))

    set1_subset_set2 = set1.issubset(set2)
    print(set1_subset_set2)

    set2_subset_set1 = set2.issubset(set1)
    print(set2_subset_set1)

    set1_superset_set2 = set1.issuperset(set2)
    print(set1_superset_set2)

    set2_superset_set1 = set2.issuperset(set1)
    print(set2_superset_set1)

input_set1 = input()
input_set2 = input()

check_sets(input_set1, input_set2)


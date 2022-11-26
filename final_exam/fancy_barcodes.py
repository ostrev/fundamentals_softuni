import re
number_of_lines = int(input())

for _ in range(number_of_lines):
    text = input()
    pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
    matches = re.findall(pattern, text)
    if not matches:
        print("Invalid barcode")
    else:
        group_pattern = r'\d'
        product_group = re.findall(group_pattern,matches[0])
        if product_group:
            number = ''.join(product_group)
            print(f"Product group: {number}")
        else:
            print(f"Product group: 00")

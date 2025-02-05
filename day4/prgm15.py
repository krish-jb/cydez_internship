# Merge two Python dictionaries into one
data1 = {
    "One": 1,
    "Two": 2
}
data2 = {
    "Three": 3,
    "Four": 5
}
merged_data = data1 | data2
print(merged_data)
# Rename key of a dictionary

stuff = {
    "One": 1,
    "TWo": 2,
    "Three": 3,
    "Five": 4
}

stuff['Four'] = stuff.pop("Five")
print(stuff)



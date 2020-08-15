# conversions.py

# Used to hold the dictionaries that allow us to perform unit conversions

conversion_dict = {
    "meters": {
        "kilometers": 0.001,
        "feet": 3.28084,
        "inches": 39.37008},
    "kilometers": {
        "meters": 1000,
        "feet": 3280.84,
        "inches": 39370.1},
    "feet": {
        "meters": 0.3048,
        "kilometers": 0.0003048,
        "inches": 12},
    "inches": {
        "meters": 0.0254,
        "kilometers": 0.0000254,
        "feet": 0.0833333},
    "milliliters": {
        "liters": 0.001,
        "gallons": 0.000219969,
        "floz": 0.03381398453291231},
    "liters": {
        "milliliters": 1000,
        "gallons": 0.219969,
        "floz": 33.81398453291231},
    "gallons": {
        "milliliters": 3785.41,
        "liters": 3.78540999993543,
        "floz": 127.99993967360012448},
    "floz": {
        "milliliters": 29.5735,
        "liters": 0.0295735,
        "gallons": 0.006505260564573373},
    "ounces": {
        "grams": 28.3495,
        "pounds": 0.0625,
        "kilograms": 0.0283495},
    "grams": {
        "ounces": 0.035274,
        "pounds": 0.00220462,
        "kilograms": 0.001},
    "pounds": {
        "ounces": 16,
        "grams": 453.592,
        "kilograms": 0.453592},
    "kilograms": {
        "ounces": 35.274,
        "grams": 1000,
        "pounds": 2.20462}
}

conversion_types = {"length": ["meters", "kilometers", "feet", "inches"],
         "volume": ["milliliters", "liters", "gallons", "floz"],
         "weight": ["ounces", "grams", "pounds", "kilograms"]}

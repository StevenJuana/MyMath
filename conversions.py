# conversions.py

# Used to hold the dictionaries that allow us to perform unit conversions

conversion_dict = {
    "meter": {
        "kilometer": 0.001,
        "feet": 3.28084,
        "inch": 39.37008},
    "kilometer": {
        "meter": 1000,
        "feet": 3280.84,
        "inch": 39370.1},
    "feet": {
        "meter": 0.3048,
        "kilometer": 0.0003048,
        "inch": 12},
    "inch": {
        "meter": 0.0254,
        "kilometer": 0.0000254,
        "feet": 0.0833333},
    "milliliter": {
        "liter": 0.001,
        "gallon": 0.000219969,
        "floz": 0.03381398453291231},
    "liter": {
        "milliliter": 1000,
        "gallon": 0.219969,
        "floz": 33.81398453291231},
    "gallon": {
        "milliliter": 3785.41,
        "liter": 3.78540999993543,
        "floz": 127.99993967360012448},
    "floz": {
        "milliliter": 29.5735,
        "liter": 0.0295735,
        "gallon": 0.006505260564573373},
    "ounce": {
        "gram": 28.3495,
        "pound": 0.0625,
        "kilogram": 0.0283495},
    "gram": {
        "ounce": 0.035274,
        "pound": 0.00220462,
        "kilogram": 0.001},
    "pound": {
        "ounce": 16,
        "gram": 453.592,
        "kilogram": 0.453592},
    "kilogram": {
        "ounce": 35.274,
        "gram": 1000,
        "pound": 2.20462}
}

conversion_types = {"length": ["meter", "kilometer", "feet", "inch"],
         "volume": ["milliliter", "liter", "gallon", "floz"],
         "weight": ["ounce", "gram", "pound", "kilogram"]}

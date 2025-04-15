
from itertools import product

temps = ["SevereHypothermia", "Hypothermia", "NormalTemp", "LowFever", "HighFever"]
ages = ["Infant", "Young", "MiddleAged", "Old"]
headaches = ["LowHeadache", "MediumHeadache", "HighHeadache"]

RULES = []

for temp, age, headache in product(temps, ages, headaches):
    if age in ["Infant", "Old"]:
        output = "Urgent"
    elif temp == "HighFever" and headache == "HighHeadache":
        output = "High"
    elif temp == "NormalTemp":
        output = "Low"
    else:
        output = "Medium"
    RULES.append({
        "temperature": temp,
        "age": age,
        "headache": headache,
        "output": output
    })

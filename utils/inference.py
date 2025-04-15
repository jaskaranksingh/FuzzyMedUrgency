
import numpy as np
from models.rules import RULES

def fuzzy_and(values, urgent=False):
    vals = list(values)
    if urgent and any(v > 0.4 for v in vals):
        return max(vals)
    elif urgent:
        return min(vals)
    else:
        return min(vals)

def infer(fuzzified_inputs):
    outputs = []
    for rule in RULES:
        temp_val = fuzzified_inputs['temperature'][rule['temperature']]
        age_val = fuzzified_inputs['age'][rule['age']]
        headache_val = fuzzified_inputs['headache'][rule['headache']]
        activation = fuzzy_and([temp_val, age_val, headache_val], urgent=rule['output'] == 'Urgent')
        outputs.append((activation, rule['output']))
    return outputs

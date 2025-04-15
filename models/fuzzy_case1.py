
from utils.fuzzification import fuzzify_temperature, fuzzify_headache, fuzzify_age
from utils.inference import infer
from utils.defuzzification import scale_output, centroid_defuzz, bisector_defuzz

def run_case(temp, headache, age, method='centroid'):
    """
    Case 1: Crisp input-based fuzzy logic system.

    Parameters:
    - temp (float): Body temperature of the patient
    - headache (float): Headache level on a scale of 0 to 10
    - age (float): Age of the patient
    - method (str): Defuzzification method ('centroid' or 'bisector')

    Returns:
    - urgency_score (float): Defuzzified output representing urgency level
    """
    fuzzified_inputs = {
        'temperature': fuzzify_temperature(temp),
        'headache': fuzzify_headache(headache),
        'age': fuzzify_age(age)
    }

    # Run inference engine
    outputs = infer(fuzzified_inputs)

    # Aggregate outputs and defuzzify
    x_vals, y_vals = scale_output(outputs)
    if method == 'centroid':
        urgency_score = centroid_defuzz(x_vals, y_vals)
    else:
        urgency_score = bisector_defuzz(x_vals, y_vals)

    return round(urgency_score, 2)

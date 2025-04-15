
import numpy as np
from utils.fuzzification import fuzzify_temperature, fuzzify_headache, fuzzify_age
from utils.inference import infer
from utils.defuzzification import scale_output, centroid_defuzz

def generate_input_membership(a, b, var_type):
    """
    Create a fuzzy input membership from an interval using a flat-top Stupa-like shape
    """
    from utils.membership import stupa_membership
    x_vals = np.linspace(0, 150, 1000)
    if var_type == 'temperature':
        return x_vals, stupa_membership(x_vals, a, b, stiffness=3)
    elif var_type == 'headache':
        return x_vals, stupa_membership(x_vals, a, b, stiffness=3)
    elif var_type == 'age':
        return x_vals, stupa_membership(x_vals, a, b, stiffness=3)

def centroid_of_intersection(input_x, input_y, mf_dict):
    results = {}
    for label, mf_y in mf_dict.items():
        intersect_y = np.minimum(input_y, mf_y)
        if np.sum(intersect_y) == 0:
            results[label] = 0.0
        else:
            centroid = np.sum(input_x * intersect_y) / np.sum(intersect_y)
            results[label] = centroid / 100.0  # normalize
    return results

def run_case(temp_range, headache_range, age_range):
    # Step 1: Create fuzzy input memberships
    tx, ty = generate_input_membership(*temp_range, var_type='temperature')
    hx, hy = generate_input_membership(*headache_range, var_type='headache')
    ax, ay = generate_input_membership(*age_range, var_type='age')

    # Step 2: Fuzzify each linguistic variable
    t_members = fuzzify_temperature(tx)
    h_members = fuzzify_headache(hx)
    a_members = fuzzify_age(ax)

    temp_members = centroid_of_intersection(tx, ty, t_members)
    headache_members = centroid_of_intersection(hx, hy, h_members)
    age_members = centroid_of_intersection(ax, ay, a_members)

    fuzzified_inputs = {
        'temperature': temp_members,
        'headache': headache_members,
        'age': age_members
    }

    outputs = infer(fuzzified_inputs)
    x_vals, y_vals = scale_output(outputs)
    return round(centroid_defuzz(x_vals, y_vals), 2)


import numpy as np

OUTPUT_MF = {
    'Low': lambda x: 1 - stupa_membership(x, 0, 40),
    'Medium': lambda x: stupa_membership(x, 35, 70),
    'High': lambda x: stupa_membership(x, 60, 100),
    'Urgent': lambda x: stupa_membership(x, 80, 100)
}

def scale_output(outputs):
    x_vals = np.linspace(0, 100, 1000)
    aggregated = np.zeros_like(x_vals)
    for activation, label in outputs:
        mf = OUTPUT_MF[label]
        aggregated = np.maximum(aggregated, activation * mf(x_vals))
    return x_vals, aggregated

def centroid_defuzz(x_vals, y_vals):
    return np.sum(x_vals * y_vals) / np.sum(y_vals)

def bisector_defuzz(x_vals, y_vals):
    area = np.cumsum(y_vals)
    total = area[-1]
    idx = np.searchsorted(area, total / 2)
    return x_vals[idx]

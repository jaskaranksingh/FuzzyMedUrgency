
from utils.membership import stupa_membership

def fuzzify_temperature(value, stiffness=5):
    return {
        "SevereHypothermia": stupa_membership(value, 31, 35.5, stiffness),
        "Hypothermia": stupa_membership(value, 35, 36.5, stiffness),
        "NormalTemp": stupa_membership(value, 36, 37.5, stiffness),
        "LowFever": stupa_membership(value, 37, 39, stiffness),
        "HighFever": stupa_membership(value, 38, 40, stiffness)
    }

def fuzzify_headache(value, stiffness=5):
    return {
        "LowHeadache": stupa_membership(value, 0, 5, stiffness),
        "MediumHeadache": stupa_membership(value, 4, 8, stiffness),
        "HighHeadache": stupa_membership(value, 6.5, 10, stiffness)
    }

def fuzzify_age(value, stiffness=5):
    return {
        "Infant": stupa_membership(value, 0, 9, stiffness),
        "Young": stupa_membership(value, 6, 35, stiffness),
        "MiddleAged": stupa_membership(value, 27, 65, stiffness),
        "Old": stupa_membership(value, 55, 130, stiffness)
    }

# utils.py

def validate_inputs(inputs: dict):
    """
    Validates input values. Returns tuple: (is_valid: bool, message: str)
    """
    for key, value in inputs.items():
        if value == "" or value is None:
            return False, f"{key} is required."
        try:
            float_val = float(value)
        except ValueError:
            return False, f"{key} must be a number."
    return True, "Valid"

def body_count(age, college, raised_by_single_mother, single_mother):
    """Determines body count based on age.
    additional factors:
    - If raised by a single mother, multiplier applied.
    - If attended college, multiplier applied.
    - If a single mother herself, multiplier applied.
    """
    if 18<=age<=24:
        estimated_body_count = 4
    elif 24<age<=27:
        estimated_body_count = 12
    elif 27<age<29:
        estimated_body_count = 22
    else:
        estimated_body_count = 25

    if raised_by_single_mother:
        estimated_body_count *= 1.5
    if college:
        estimated_body_count *= 1.5
    if single_mother:
        estimated_body_count *= 1.5
    else:
        estimated_body_count *= 1

    return estimated_body_count
    
    
def dowry_negotiation(name, age, body_count_result, asked_dowry, single_mother, college):
    """Calculate dowry and return result as a string.
    - Factors in bondy count and requested dowry.
    - Ensures the calculated dowry is meaningful and provides feedback.
    """
    if body_count_result <= 0:
        return f"Please check the inputs details for {name}."
    
    actual_dowry = asked_dowry/(body_count_result+1)

    if actual_dowry < 5000:
        return f"{name}'s dowry is too low to be considered: {actual_dowry:.2f}."
    elif actual_dowry > asked_dowry:
        return f"{name}'s calculated dowry exceeds the asked dowry: {actual_dowry:.2f}."
    else:
        return f"The calculated dowry for {name}, is: {actual_dowry:.2f}."
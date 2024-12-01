def body_count(age, college, raised_by_single_mother, single_mother):
    """Determines body count based on age."""
    if 18<=age<=24:
        estimated_body_count = 4
    elif 24<age<=27:
        estimated_body_count = 12
    elif 27<age<29:
        estimated_body_count = 22
    else:
        estimated_body_count = 25
    if raised_by_single_mother:
        estimated_body_count = estimated_body_count * 1.5 
    if college:
        estimated_body_count = estimated_body_count * 1.5
    if single_mother:
        estimated_body_count = estimated_body_count * 1.5
    else:
        estimated_body_count = estimated_body_count * 1

    return estimated_body_count
    
    
def dowry_negotiation(name, age, body_count_result, asked_dowry, single_mother, college):
    """Calculate dowry and return result as a string."""
    
    actual_dowry = asked_dowry/(body_count_result+1)

    return actual_dowry
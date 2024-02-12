
try:
    height = float(input("Height (m): "))
    weight = int(input("Weight (kg): "))
except ValueError as value_error:
    print(value_error)
else:
    if (height > 3.0 or height < 0.2):
        raise ValueError("Human height must be in range of (height > 0.2m  AND height < 3.0m)")
    if (weight < 2 or weight > 350):
        raise ValueError("Human weight must be in range of (weight > 2kg AND weight < 350kg)")
    else:
        bmi = weight/(height**2)
        print(f"Your bmi is: {round(bmi,2)}")
    

    

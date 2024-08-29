#this is a test
import pandas as pd
import numpy as np 
number = 22
string = 'Angie Wang'
list = [22, 'Angie Wang']
dict = {
    'name': 'Angie',
    'age': 22,
    'grocery list': ['apples','bananas','grapes'],
    'shop address': {
        'street':'1 shop st',
        'city':'stony brook',
        'state': 'NY'
    }
}
print(dict)

# BMI Calcuation
def calculate_bmi(weight, height):
    print(f"Weight: {weight} kg")
    print(f"Height: {height} meters")
   
    # Calculate BMI
    bmi = weight / (height * 2)
    
    if bmi < 18.5:
        result = "Underweight"
    elif 18.5 <= bmi < 24.9:
        result = "Normal weight"
    else:
        result = "Obesity"
    # Print the result
    print(f"Weight Category: {result}")
   
    # Return the result
    return result

#Ex data
weight_example = 40
height_example = 1.89

bmi_result = calculate_bmi(weight_example, height_example)
print("BMI Analysis:", bmi_result)
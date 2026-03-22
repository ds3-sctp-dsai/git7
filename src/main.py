# src/main.py

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Returns:
        BMI as a float, rounded to 2 decimal places.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)





if __name__ == "__main__":
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} — {bmi_category(bmi)}")
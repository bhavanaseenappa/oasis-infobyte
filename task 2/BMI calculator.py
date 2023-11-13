def get_user_input():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        return weight, height
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return None, None

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight, height = get_user_input()

    if weight is not None and height is not None and weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()

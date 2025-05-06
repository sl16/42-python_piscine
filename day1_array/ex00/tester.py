from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# Extra tests
print("\nExtra tests:\n")

print("\nTest 2: Edge case - Empty lists")
height = []
weight = []
bmi = give_bmi(height, weight)
print("BMI:", bmi)
print("Apply Limit (26):", apply_limit(bmi, 26))

print("\nTest 3: Mismatched list sizes")
height = [1.75, 1.80]
weight = [70]
bmi = give_bmi(height, weight)

print("\nTest 4: Invalid data types")
height = [1.75, "invalid"]
weight = [70, 80]
bmi = give_bmi(height, weight)

print("\nTest 5: Apply limit with invalid BMI list")
bmi = ["invalid", 24.5]
print("Apply Limit (26):", apply_limit(bmi, 26))

print("\nTest 6: Apply limit with invalid BMI list")
bmi = [12, 24.5]
print("Apply Limit (26):", apply_limit(13, 26))

print("\nTest 7: Division by zero")
height = [0]
weight = [70]
bmi = give_bmi(height, weight)

print("\nTest 8: Negative values in input")
height = [1.75, -1.80]
weight = [70, 80]
bmi = give_bmi(height, weight)

print("\nTest 9: Zero weight")
height = [1.75, 1.80]
weight = [0, 0]
bmi = give_bmi(height, weight)
print("BMI:", bmi)
print("Apply Limit (26):", apply_limit(bmi, 26))

print("\nTest 10: Non-numeric types in lists")
height = [1.75, None]
weight = [70, True]
bmi = give_bmi(height, weight)
print("BMI:", bmi)

from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print("\n")
print(slice_me(family, 1, -2))

# Extra tests

# Test 1: Empty 2D list
print("\nTest 1: Empty 2D list")
family = []
print(slice_me(family, 0, 2))

# Test 2: Single row
print("\nTest 2: Single row")
family = [[1.80, 78.4]]
print(slice_me(family, 0, 1))
print(slice_me(family, 0, 2))  # Out-of-range slicing

# Test 3: Single column
print("\nTest 3: Single column")
family = [[1.80], [2.15], [2.10], [1.88]]
print(slice_me(family, 1, 3))

# Test 4: Negative indices
print("\nTest 4: Negative indices")
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, -3, -1))

# Test 5: Out-of-range indices
print("\nTest 5: Out-of-range indices")
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 0, 10))  # End index exceeds the list length
print(slice_me(family, 10, 20))  # Both indices are out of range

# Test 6: Non-rectangular 2D list
print("\nTest 6: Non-rectangular 2D list")
family = [[1.80, 78.4], [2.15], [2.10, 98.5]]
print(slice_me(family, 0, 2))

# Test 7: Mixed data types
print("\nTest 7: Mixed data types")
family = [[1.80, "Alice"], [2.15, "Bob"], [2.10, "Charlie"]]
print(slice_me(family, 0, 2))

# Test 8: Large 2D list
print("\nTest 8: Large 2D list")
family = [[i, i + 1] for i in range(1000)]
print(slice_me(family, 100, 200))

# Test 9: Zero-length slice
print("\nTest 9: Zero-length slice")
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 2, 2))  # Start and end indices are the same

# Test 10: Invalid input types
print("\nTest 10: Invalid input types")
family = "Not a 2D list"
print(slice_me(family, 0, 2))

family = [[1.80, 78.4], [2.15, 102.7]]
print(slice_me(family, "start", "end"))  # Invalid start and end types

# Test 11: Empty rows
print("\nTest 11: Empty rows")
family = [[], [], []]
print(slice_me(family, 0, 2))
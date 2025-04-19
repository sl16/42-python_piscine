ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

# A list can be accessed via index
ft_list[1] = "World!"

# Tuples are immutable, but we can reassign the variable
ft_tuple = ("Hello", "Czech Republic!")

# A set is unordered, so we cannot access an item via its index
# Because of this, the printed order may be different each time
ft_set.discard("tutu!")
ft_set.add("Prague!")

# We need to assign a new value for the key
ft_dict["Hello"] = "42 Prague!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
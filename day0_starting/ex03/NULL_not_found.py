def NULL_not_found(object: any) -> int:
	
	type_found = True
	type_description = ""
	match object:
		case None:
			var_name = "Nothing"
			type_description = "None"
		case float():
			var_name = "Cheese"
			type_description = "nan"
		case bool():
			var_name = "Fake"
			type_description = "False"
		case int():
			var_name = "Zero"
			type_description = "0"
		case str() if object == "":
			var_name = "Empty"
			type_description = ""
		case _:
			type_description = "Type not found"
			type_found = False

	if type_found:
		print(f"{var_name}: {type_description} {type(object)}")
		return 0
	else:
		print(f"{type_description}")
		return 1
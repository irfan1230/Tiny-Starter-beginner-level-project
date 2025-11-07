employ = []
tup=tuple(employ)
def employees():
	if employ == []:
		print("Empty")
	else:
		for i,j in enumerate(employ,1):
			print(f"{i}.{j}")
def add_employees():
	while True:	
		try:
			addem=int(input("\nHow Many Employees Can Add :- "))
			break
		except:
			print("\nOnly Enter Number Try Agin ")
	for i in range(addem):
		while True:
			ade = input(f"\nEnter Employ Name :- {i+1}.")
			if ade.isidentifier():
				break
			else:
				print('\nDont Use Space Use "_"')
		employ.append(ade)
	print("\nSuccesfully Added . . . . .\n")
	print(employ)
def delete_employee():
	pass	


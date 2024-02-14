my_list = ["Benz","Subaru","Audi","Range","BMW"]
my_list.append("Mazda")
print(my_list)
print(f"{my_list[4]} is manufactured in Germany")
my_list[2] = "Benz"
print(f"{my_list[1]} is manufactured in Japan")


my_list.insert(2,"Prado")
print(my_list)

print(type(my_list))
# tuple datastructures
my_tuple=("Banana","Apple","Orange","Mangoes")
print(my_tuple)

print(f"I like eating {my_tuple[0]}")
# my_tuple[2]= "Apple"   tuple is immutable because it does not support assign

# set datastructure
# my set data structure is unordered and has no index
my_set = {"Kenya","Uganda","Tanzania","Somalia"}
print(my_set)

# dictionary datastructures
my_dict={"Name":"Zack","Age":26,"Gender":"Male","Education":"University"}
print(my_dict)
print(f"My name is {my_dict['Name']} and I am {my_dict['Age']} years old")
print(f"{my_dict['Name']} has a {my_dict['Education']} degree from Moi University")
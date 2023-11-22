print("hello, world")
names = input("Enter the first and last name of your friend separated by comma : ").split(", ")
for name in names:
  person = []
  person.append(name)
  ", ".join(person)
  print(person)

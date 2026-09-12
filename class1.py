print("hello world")

name= "Akash"
Department="Data Analytics"
city="Lucknow"
print(name,Department,city)
print(name)
print(city)
print(Department)

#string indexing

name= "Python"
print(name[0])
print(name[3])
print(name[4])

# string slicing
# example
name="Python"
print(name[0:3])
print(name[1:5])

# upper case()
# example
Name="akash kumar"
print(Name.upper())

# Lower case()
# example
name='AKASH KUMAR'
print(name.lower())
print(name.lower())

# strip()
# example
name="   akash  kumar  "
print(name)
print(name.strip())

# replace()
# example
city='benguluru'
print(city.replace('benguluru','Noida'))
print(city.replace('benguluru','New Delhi'))


# split()
# example 
text = "Data Analytics Course"
print(text.split())
text='its rain today'
print(text.split())

# join()
# example
name=['akash','kumar','chaudhary']
result=" ".join(name)
print(result)

# length()
# example
text="Data Anayltics "
# print(text.len()) this is wrong
print(len(text))

# STARTWITH() EXAMPLE
email="akashk0522@gmail.com"
print(email.startswith("akash"))
print(email.startswith('@'))

# endswith example 
email="akashk0522@gmail.com"
print(email.endswith(".com"))
print(email.endswith("akash"))



customers = ["  Rahul", "Priya  ", "  Amit  ", "NEHA"]

for customer in customers:
    print(customer.strip().upper())

    # •	Create a variable containing your name and print it.
    name="akash kumar"
    print(name)

    # Convert "data analyst" to uppercase
course="data anaylst"
print(course.upper())

# •	Convert "PYTHON" to lowercase.

name="PYTHON"
print(name.lower())

# •	Remove extra spaces from "   Rahul   ".

name="   Rahul   "
print(name.strip())

# •	Replace "Excel" with "Python" in "I love Excel".

text=  "I love Excel"
print(text.replace('Excel','Python'))

# •	Print the first and last characters of "Python".

name="Python"
print(name[0])
print(name[5])

# # •	Split "Data Analytics Course" into individual words.

text="Data Analytics Course"
print(text.split())

# # •	Find the length of "Data Analyst".

name="Data Analyst"
print(len(name))

"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""
text = input("Introduce-ti un text: ")

second = text[2]

if second =="a":
    print("'a' se afla pe pozitia 2")
else:print("'a' nu se afla pe pozitia 2")

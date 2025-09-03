num1 = int(input("Gib eine Zahl ein:"))
num2 = int(input("Gib noch eine Zahl ein:"))
geburtsjahr = int(input("In welchem Jahr bist du geboren?"))

num1 = int(num1)
num2 = int(num2)
geburtsjahr = int(geburtsjahr)


sum = num1 + num2
produkt = num1 * num2
differenz = num1 - num2
age_this_year = 2025 - geburtsjahr

print(f"Summe: {sum}")
print(f"Produkt: {produkt}")
print(f"Differenz: {differenz}")
print(f"You are this year {age_this_year} years old")

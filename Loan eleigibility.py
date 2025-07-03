#Take user input for name, age, and monthly income. If age ≥ 21 and
#income ≥ ₹25,000, print eligible. Else, print ineligible.
name=input("Enter name:")
Age=int(input("Enter Age:"))
Income=int(input("Enter income:"))
if(Age>=21 and Income>=25000):
    print("Eligible")
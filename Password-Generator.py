import random
import string

password = []
print("Welcomme to the Password Generator!")
tall = int(input("Enter the total number of characters in the password: "))

letter = int(input("Enter the number of letters in the password: "))
digits = int(input("Enter the number of numbers in the password: "))
sympol = int(input("Enter the number of sympols in the password: "))

total = letter + digits + sympol

if tall == total:
  random_letter = random.choices((string.ascii_letters),k=letter)
  random_digits = random.choices((string.digits),k=digits)
  random_sympol = random.choices((string.punctuation),k=sympol)

  password.extend(random_letter)
  password.extend(random_digits)
  password.extend(random_sympol)

  random.shuffle(password)
  passwd = "".join(password)
  print(f"Generated Password: {passwd}")
else:
  print("Invalid input. The sum of letters, numbers ,and sympols dosen't much password.")
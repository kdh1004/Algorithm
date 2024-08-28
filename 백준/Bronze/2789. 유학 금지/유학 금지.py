ban = list("CAMBRIDGE")
mail = ""
for i in input():
    if i not in ban:
        mail += i
print(mail)
'''
https://docs.google.com/document/d/175kiYt16pO-cIINARSEQOzgI-9CV9Q-o6xJ13yIcCB0/edit?tab=t.0
'''
txt=str(input("Enter string to update in file: "))
with open("output.txt", "w") as f:
    f.write(txt + "\n")
print("Data successfully written to output.txt")
txt=str(input("Enter additional text to append: "))
with open("output.txt", "a") as f:
    f.write(txt + "\n")
print("Data successfully append to output.txt")

with open("output.txt", "r") as f:
    line=f.read()
print(line)

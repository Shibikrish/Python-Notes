'''
https://docs.google.com/document/d/175kiYt16pO-cIINARSEQOzgI-9CV9Q-o6xJ13yIcCB0/edit?tab=t.0
'''
try:
    with open ("sample.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
except:
    print("Error: The file sample.txt was not found")

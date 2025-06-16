name=str(input("Enter student's name: "))
ledger= {
        "John":"100",
        "Alice":"20",
        "Sean":"90",
        "Paul":"70"}
if name in ledger:
    print(name, "marks is:", ledger[name])
else:
    print("Student's name not found") 


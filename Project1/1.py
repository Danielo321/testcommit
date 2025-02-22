# Att göra lista

tasks = ["cykla", " Simma","Gym", "Springa", "Plugga"]
print("Välkommen till Att göra appen")
print("------------------------------------------------")

def display_list():
    if len(tasks) == 0: 
        print("Du har inga uppgifter kvar!")

    elif len(tasks) == 1:
        print("Du har en uppgift att göra!")

    else:
        print("Du har " + str(len(tasks)) + " uppgift kvar att göra!");

print(tasks)

        
display_list()


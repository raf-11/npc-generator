import logic

print("Welcome to NPC genrator!")
run = True

while run:
    valid_input = False
    while not valid_input:
        print("Do you wish to generate an npc?")
        user_input = input().strip().lower()
        if user_input == "yes":
            valid_input = True
        elif user_input == "no":
            valid_input = True
        else:
            print("Invalid choice\nPlease choose again(yes/no)")
    if user_input == "yes":
        npc_name, npc_job, npc_personality, npc_secret, npc_catchphrase, npc_weird_habit = logic.generate_npc() 
        print(f"NPC Name: {npc_name}\nNPC Job: {npc_job}\nNPC Personality: {npc_personality}\nNPC Secret: {npc_secret}\nNPC Catchphrase: {npc_catchphrase}\nNPC Weird Habit: {npc_weird_habit}")
    else:
        print("Bye bye")
        run = False
        
    
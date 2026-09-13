import logic

print("Welcome to NPC genrator!")
run = True

while run:
    print("Do you wish to generate an npc?")
    user_input = input().lower()
    if user_input == "yes":
        npc_name, npc_job, npc_personality, npc_secret, npc_catchphrase, npc_weird_habit = logic.generate_npc() 
        print(f"NPC Name: {npc_name}\nNPC Job: {npc_job}\nNPC Personality: {npc_personality}\nNPC Secret: {npc_secret}\nNPC Catchphrase: {npc_catchphrase}\nNPC Weird Habit: {npc_weird_habit}")
    elif user_input == "no":
        print("Bye bye")
        run = False
    else:
        print("Invalid choice\nPlease choose again(yes/no): ")
        
    
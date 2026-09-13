import data
import random

def generate_npc():
    npc_name = random.choice(data.names)
    npc_job = random.choice(data.jobs)
    npc_personality = random.choice(data.personalities)
    npc_secret = random.choice(data.secrets)
    npc_catchphrase = random.choice(data.catchphrases)
    npc_weird_habit = random.choice(data.weird_habits)
    
    return npc_name, npc_job, npc_personality, npc_secret, npc_catchphrase, npc_weird_habit
team_dict = {
    "Anil": "ECE", "RAMU": "EEE", "Mahesh": "IT", "Kiran": "Civil",
    "RAJU": "CSE", "Vahid": "CSE", "Naresh": "CSE", "Mallesh": "ECE",
    "RAJU": "CSE", "Karan": "IT", "Sachin": "CSE", "Jadeja": "IT",
    "Pranav": "CSE", "Praneeth": "IT", "Praneeth": "CSE"
}

total_players = 0 #initially zero
cse_count = 0
it_count = 0
cse_players = []
it_players = []

for value in team_dict.values():
    total_players += 1
    if value == "CSE":   #If the value is "CSE", it increments the cse_count variable; if it's "IT", it increments the it_count variable.
        cse_count += 1
    elif value == "IT":
        it_count += 1

for key, value in team_dict.items():
    if value == "CSE":
        cse_players.append(key) #append if the key value pair is cse
    elif value == "IT":
        it_players.append(key) #append if the key value pair is IT

print("Total Players count:", total_players)
print("CSE & IT Players Count:", cse_count + it_count)
print("CSE Player names:", ", ".join(cse_players))
print("IT Player names:", ", ".join(it_players))



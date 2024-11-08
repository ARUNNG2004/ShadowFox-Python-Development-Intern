#1 Calculate the number of members in the Justice League
print("--------------------task-1----------------------------")
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Number of members in justice league:", len(justice_league))
print("------------------------------------------------")


#Batman recruited Batgirl and Nightwing as new members.
print("----------------------task-2--------------------------")

justice_league.extend(["Batgirl", "Nightwing"])
print("Updated list:", justice_league)

print("------------------------------------------------")

print("-------------------------task-3-----------------------")
#Wonder Woman is now the leader of the Justice League.
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman is now the leader:", justice_league)

print("------------------------------------------------")


print("-----------------------task-4-------------------------")
# Separate Aquaman and Flash by inserting Green Lantern between them:

justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")


print("Separated Aquaman and Flash:", justice_league)
print("------------------------------------------------")


print("-------------------------task-5-----------------------")
#Replace the existing list with a new team

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

print("------------------------------------------------")

print("------------------------task-6------------------------")
#Sort Justice League alphabetically to find new leader
justice_league.sort()
print("Sorted list:", justice_league)
print("New leader:", justice_league[0])

print("------------------------------------------------")

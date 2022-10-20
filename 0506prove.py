print()
print("You open your eyes to an evening sky in an old, small paddle boat drifting in the middle of the sea with no recollection of how you got there. Everything seems so hazy, almost dream-like. You sit up to assess your surroundings. To the north about 10 miles, you see the silhouette of an island. To the south about 30 miles, you see what seems to be a tiny dot of light. You have about 2 days worth of fresh water with you. Should you start paddling NORTH, SOUTH, or WAIT for someone to rescue you? Note: paddling will cause you to sweat, forcing you to drink more water to stay hydrated.")
print()
scenario1 = input("Enter NORTH, SOUTH, or WAIT: ")
print()
if scenario1.lower() == "north":
    print("You start paddling north. A few hours later, you reach the shoreline of a dark, mysterious island teeming with tall trees. Dark clouds now blanket the night sky, obstructing the moon’s shine on the island. It’s going to rain and you might want to find shelter. Do you enter the dark and ominous FOREST, or wait in the open rain until morning on the SEASHORE?")
    print()
    north = input("Enter FOREST or SEASHORE: ")
    print()
    if north.lower() == "forest":
        print("You decide the best option would be to find shelter in the forest. As you enter the forest, you notice a dim glow coming from deep within. You push your way through large bushes, vines, and scattered foliage to find where the dim glow is escaping from. You come to a semi-bright opening of a hidden cave that otherwise would not have been found unless it were dark. As you approach the cave you notice settle green vapor escaping from the mouth of the cave. From the outside, you can see a pool of fresh water surrounded by glowing rocks in the center of the cave. Do you ENTER the cave or TURN AROUND?")
        print()
        forest = input("Enter ENTER or TURN AROUND: ")
        print()
        if forest.lower() == "enter":
            print("You enter the cave and walk towards the pool of clean water. The green mist seems to not have any effect on you. You happily drink your fill of water and start building a fire. This is where you will safely stay until morning comes and you can thoroughly inspect the island.")
        elif forest.lower() == "turn around":
            print("You turn around, not wanting to take your chances with unknown vapors. As you blindly walk through the forest, your foot gets caught on the root of a tree, causing you to trip and collide your head with a very ragged boulder. That’s the last thing you’ll ever remember.")
        elif forest.lower() == "wake up":
            print("Congratulations! You've successfully figured out the hidden option. It was all just an eerie dream. ")
    elif north.lower() == "seashore":
        print("You don’t want to enter the forest not knowing or seeing what’s in there. You decide to just sit on the beach and patiently wait in the rain until morning comes. As the rain slowly diminishes and the sun starts to rise, you start developing symptoms of a severe illness from the cold rain. Should you REST in the sun on the beach to regain strength or FORCE yourself to get up and seek help from within the forest?")
        print()
        seashore = input("Enter REST or FORCE: ")
        print()
        if seashore.lower() == "rest":
            print("Feeling the warmth of the sunlight on your skin, you decide to rest in the sun for a while. After a few hours into the day, your body becomes too weak to move. You sadly succumb to your illnesses by nightfall.")
        elif seashore.lower() == "force":
            print("You force yourself to stand up and start making your way into the forest. Stumbling through foliage and dense greenery, you come across colorful mushrooms. With nothing to lose, you decide to consume it. Minutes pass and a tingly sensation starts coursing through your body. All of a sudden you feel fully regenerated. Now you can start making plans to be rescued.")
        elif seashore.lower() == "wake up":
            print("Congratulations! You've successfully figured out the hidden option. It was all just an eerie dream. ")
    elif north.lower() == "wake up":
        print("Congratulations! You've successfully figured out the hidden option. It was all just an eerie dream. ")
    else:
        print("Please restart the program and choose a valid answer.")
    print()
elif scenario1.lower() == "south":
    print("You start paddling south. After many hours of paddling, your water supply is fully depleted. You finally get close enough to tell that the light source is coming from an eerie, old lighthouse in the middle of a tiny island. As you land and approach the door to the lighthouse, you hear loud smashing noises from within. Should you KNOCK or quietly EXPLORE the dark and tiny island?")
    print()
    south = input("Enter KNOCK or EXPLORE: ")
    print()
    if south.lower() == "knock":
        print("As you tentatively knock on the door, the smashing noises immediately stop. A few moments later, a masked madman with a sledgehammer swings the door open and lurches at you. Do you dodge and RUN, or do you stay and FIGHT?")
        print()
        knock = input("Enter RUN or FIGHT: ")
        print()
        if knock.lower() == "run":
            print("You quickly dodge the sledgehammer swing and maneuver your way behind the masked madman, running away as quickly as possible. The masked madman turns quickly to start rushing after you. Luckily, the large sledgehammer is slowing him down. You are quickly able to lose him and hide. For the moment, you’re safe to come up with a plan to escape the island. ")
        elif knock.lower() == "fight":
            print("You stand your ground to fight off the incoming attacks. After a few dodges accompanied by some counterattacks of your own, you feel an ice-cold sensation spreading from your left temple—you’ve been struck with the sledgehammer to your head. Your vision starts to blur out and you’re left seeing nothing but black and red.")
        elif knock.lower() == "wake up":
            print("Congratulations! You've successfully figured out the hidden option. It was all just an eerie dream. ")
        print()
    elif south.lower() == "explore":
        print("You start quietly exploring the surroundings of the island. After further investigation, you find a vacant jet boat on the opposite side of the island not too far away from the lighthouse. Thinking it must belong to whoever was smashing everything in the lighthouse, you decide to take the boat to find help. As you start the engine you hear the lighthouse door violently swing open. A masked madman carrying a sledgehammer starts running after you. As you try to pull away from the island, you notice the boat is anchored. Should you risk trying to UNANCHOR the boat, or ABANDON the boat and try running away?")
        print()
        explore = input("Enter UNANCHOR or ABANDON: ")
        print()
        if explore.lower() == "unanchor":
            print("You jump off the jet boat and scramble to unanchor the ship. As the madman closes in, you hurriedly jump back in the ship and accelerate the jet boat forward. You take a quick glance back to find the madman standing where the jet boat was just seconds ago. He’s too late, you’re far gone now. ")
        elif explore.lower() == "abandon":
            print("You quickly leap out of the boat and start running perpendicular to the beach. In your rush to escape, your trip on the slippery sand. The madman has already fallen upon you as you struggle to pick yourself up. The sandy beach beneath your hands is the last thing you will ever see.")
        elif explore.lower() == "wake up":
            print("Congratulations! You've successfully figured out the hidden option. It was all just an eerie dream. ")
    elif south.lower() == "wake up":
        print("Congratulations! You've successfully figured out the hidden option. It was all just an eerie dream. ")
    else:
        print("Please restart the program and choose a valid answer.")
elif scenario1.lower() == "wait":
    print("You decide to wait, conserving your energy and water. Hopefully, 2 days should be more than enough time for someone to find and rescue you. After a few hours, you notice dark clouds covering the sky--it’s about to heavily rain. Upon frantically searching, you find a tarp large enough to barely cover the top of the boat from the rain. Should you use the tarp to COVER the entire top of the boat, or use the tarp as a water BASIN to capture more drinkable water but risk the extra water weight in the old boat?")
    print()
    wait = input("Enter COVER or BASIN: ")
    if wait.lower() == "cover":
        print("You don’t want to risk the extra water weight sinking your small, worn-down boat. You completely cover yourself and the boat’s opening as the downpour of rain starts. A few more hours pass and the rain slowly diminishes. As the rain fully subsides, you hear loud sirens. You quickly tear off the tarp and sit up to find yourself shrouded in deep fog. You locate the sirens to be off to your left about 300 yards, but you cannot see the source. Should you APPROACH the sirens, or RETREAT the opposite way?")
        print()
        cover = input("Enter APPROACH or RETREAT: ")
        if cover.lower() == "approach":
            print("Hope swells up as you try to paddle your way toward the sirens. As you near what seems to be a large vessel a bright light shines on your boat. It’s the coastal guard, you’re saved!")
        elif cover.lower() == "retreat":
            print("Hearing a loud siren frightens you. Not knowing what the source is, you decide it’s better to take your chances paddling away from the sirens. Days go by and you’ve completely depleted your water supply. With no hope of anyone ever finding you, you slowly drift into a state of hallucinations and craze. ")
        elif cover.lower() == "wake up":
            print("Congratulations! You've successfully figured out the hidden option. It was all just an eerie dream. ")
        print()
    elif wait.lower() == "basin":
        print("You form a basic water basin with the tarp as the downpour of rain starts. However, you did not expect it to rain so brutally. 10 minutes in, and your water basin is already full. With the weight of the water in the water basin and the weight of the water pouring into the boat, you notice the boat starts sinking. The last thing you can remember is the sound of heavy rain splashing against the watery surface of the sea as you drift off into a deep slumber.")
    elif wait.lower() == "wake up":
        print("Congratulations! You've successfully figured out the hidden option. It was all just an eerie dream. ")
    else:
        print("Please restart the program and choose a valid answer.")
elif scenario1.lower() == "wake up":
    print("Congratulations! You've successfully figured out the hidden option. It was all just an eerie dream. ")
else:
    print("Please restart the program and choose a valid answer.")
print()
import random
import string
words=["Apple", "Bicycle", "Elephant", "Sunshine", "Telescope", "Whisper", "Harmonica", "Glacier", "Tornado", "Lantern", "Puzzle", "Fragrance", "Ballet", "Skylight", "Octopus", "Enigma", "Cactus", "Symphony", "Quasar", "Bamboo", "Paradox", "Serenade", "Rainbow", "Velociraptor", "Saffron", "Avalanche", "Moonlight", "Kaleidoscope", "Jaguar", "Peacock", "Chimera", "Quicksilver", "Lighthouse", "Marzipan", "Quagmire", "Phoenix", "Nebula", "Utopia", "Zephyr", "Monsoon", "Avalanche", "Galactic", "Fractal", "Daffodil", "Aardvark", "Lemur", "Pendulum", "Velour", "Serendipity", "Solarium", "Whisper", "Mandolin", "Volcano", "Pegasus", "Infinity", "Quasar", "Vermilion", "Twilight", "Bubblegum", "Pantomime", "Vanilla", "Kaleidoscope", "Tangerine", "Mystique", "Bliss", "Nirvana", "Quasar", "Tundra", "Zephyr", "Oracle", "Cascade", "Horizon", "Nebula", "Radiant", "Quicksilver", "Alabaster", "Serenity", "Gossamer", "Sonnet", "Harmonica", "Cascade", "Labyrinth", "Elusive", "Whimsical", "Lagoon", "Monolith", "Enigma", "Nebula", "Lullaby", "Phoenix", "Whisper", "Placid", "Eclipse", "Synchronicity", "Velvet", "Cascade", "Solarium", "Melody", "Ethereal", "Horizon", "Iridescent", "Symphony", "Celestial", "Oasis", "Zephyr", "Cascade", "Serenity", "Pendulum", "Radiant", "Mirage", "Velvet", "Nebula", "Quasar", "Pantomime", "Cascade", "Tranquil", "Utopia", "Serendipity", "Melody", "Moonlight", "Lullaby", "Cascade", "Enigma", "Serenade", "Velvet", "Celestial", "Ephemeral", "Lagoon", "Odyssey", "Cascade", "Radiant", "Labyrinth", "Mirage", "Ephemeral", "Harmonica", "Aurora", "Serenade", "Cascade", "Ethereal", "Odyssey", "Quicksilver", "Mirage", "Sonnet", "Whisper", "Elusive", "Velvet", "Lagoon", "Utopia", "Cascade", "Serenity", "Radiant", "Ethereal", "Harmonica", "Celestial", "Cascade", "Lullaby", "Serenade", "Zephyr", "Quasar", "Eclipse", "Lagoon", "Horizon", "Melody", "Cascade", "Ephemeral", "Utopia", "Mirage", "Radiant", "Odyssey", "Serenade", "Celestial", "Whisper", "Velvet", "Cascade", "Harmonica", "Iridescent", "Ethereal", "Zephyr", "Aurora", "Odyssey", "Serendipity", "Cascade", "Radiant", "Lagoon", "Celestial", "Enigma", "Quasar", "Ephemeral", "Mirage", "Velvet", "Serenade", "Aurora", "Utopia", "Whisper", "Cascade", "Ethereal", "Labyrinth", "Radiant", "Harmony", "Celestial", "Lagoon", "Serendipity", "Quasar", "Odyssey", "Ephemeral", "Mirage", ]

def play():
    selected=random.choice(words).upper()
    alpha=set(string.ascii_letters.upper())
    collection=set()
    selected_sort=set(selected)
    lives=10
    while len(selected_sort)>0 and lives>0:
        print("YOU HAVE GUESSED THE ALPHABETS : ", " ".join(collection))
        print(f"YOU HAVE REMAINING LIVES  : {lives}")
        listee=[]
        for char in selected:
            if char in collection:
                listee.append(char)
            else:
                listee.append("_")

        print("CURRENT WORDS : ", " ".join(listee))
        inp_user=input("SELECT AN ALPHABET : ").upper()
        if inp_user in alpha-collection:
           collection.add(inp_user)
           
           if inp_user in selected_sort:
                selected_sort.remove(inp_user)
           else:
               lives=lives-1
                
        elif inp_user in collection:
            lives=lives-1
            print("YOU HAD ALREADY USED THIS LETTER")
        else:
            print("INVALID OUTPUT")
    if lives==0:
        print(f"YOU HAVE USED ALL THE LIVES, THE WORD WAS {selected}")
    else:
        print(f"YOU HAVE GUESSED THE WORD {selected} !! ")
play()

    





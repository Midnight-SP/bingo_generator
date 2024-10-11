import random
import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader][1:]  # Skip header and get first column

def random_item():
    items = read_csv('./all_minecraft_items_1_21.csv')
    return random.choice(items)

def random_mob():
    mobs = read_csv('./all_minecraft_mobs_1_21.csv')
    return random.choice(mobs)

def random_biome():
    biomes = read_csv('./all_minecraft_biomes_1_21.csv')
    return random.choice(biomes)

def random_advancement():
    advancements = read_csv('./all_minecraft_advancements_1_21.csv')
    return random.choice(advancements)

def random_effect():
    effects = read_csv('./all_minecraft_effects_1_21.csv')
    return random.choice(effects)

def tile_generator():
    tile_type = random.randint(1, 5)
    
    if tile_type == 1:
        return "Get " + random_item()
    if tile_type == 2:
        return "Kill " + random_mob()
    if tile_type == 3:
        return "Find " + random_biome()
    if tile_type == 4:
        return "Complete " + random_advancement()
    if tile_type == 5:
        return "Get " + random_effect()

def random_tile():
    return tile_generator()

bingo = [[0 for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5):
        bingo[i][j] = random_tile()

for i in range(5):
    for j in range(5):
        print(f"{bingo[i][j]:<25}", end=" ")  # Adjust the width as needed
    print()
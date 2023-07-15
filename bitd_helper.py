import random


def dice_roll(n):
    """
    Rolls the dice and gives the results of the roll
    :param n: number of dice to roll
    :return: [0] List of dice rolls [1] Highest roll [2] Outcome of roll
    """
    result = []
    for _i in range(0, n):
        result.append(random.randint(1, 6))
    if result.count(6) >= 2:
        outcome = "Critical Success"
    elif max(result) == 6:
        outcome = "Full Success"
    elif 4 <= max(result) <= 5:
        outcome = "Partial Success with Complication"
    else:
        outcome = "Failure"
    return result, max(result), outcome


def random_from_file(text_file):
    """
    Picks a random name from a text file
    :param text_file: Path to text file
    :return: A random name from the text file
    """
    file = open(text_file, "r")
    output = file.read().split("\n")
    return random.choice(output)


def random_full_name():
    """
    Picks a random full name based off the output from function "random_name"
    :return: [0] Full name [1] First name [2] Alias [3] Last name
    """
    first_name = random_from_file("first_names.txt")
    family_name = random_from_file("family_names.txt")
    alias = random_from_file("aliases.txt")
    full_name = f"{first_name} \"{alias}\" {family_name}"
    return full_name, first_name, alias, family_name


def random_look():
    """
    Picks a random "look" for the player / NPC
    :return: [0] Gender [1] Overall look [2] Clothing choice
    """
    gender = random.choice(["man", "woman", "ambiguous", "concealed"])
    look = random_from_file("look.txt")
    clothing = random_from_file("clothing.txt")
    return gender, look, clothing


def main():
    alias_true = random.choice([True, False])
    if alias_true:
        name = random_full_name()[0]
    else:
        name = f"{random_full_name()[1]} {random_full_name()[3]}"
    print(f"Name:     {name}")
    print(f"Gender:   {random_look()[0].capitalize()}")
    print(f"Look:     {random_look()[1]}")
    print(f"Clothing: {random_look()[2]}")


if __name__ == "__main__":
    main()

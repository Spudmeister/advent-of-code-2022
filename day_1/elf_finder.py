from data_loader import data_loader


def part_1():
    raw_data = data_loader(day=1, year=2022)

    best_elf_calories = 0
    for elf in raw_data.split('\n\n'):
        elf_snack_calories = elf_calories(elf)
        if elf_snack_calories > best_elf_calories:
            best_elf_calories = elf_snack_calories

    print(best_elf_calories)
    return best_elf_calories


def part_2():
    raw_data = data_loader(day=1, year=2022)

    elves_calories = [elf_calories(elf) for elf in raw_data.split('\n\n')]

    elves_calories.sort()
    top_3 = sum(elves_calories[-3:])

    print(top_3)
    return top_3


def elf_calories(elf):
    elf_snack_calories = 0
    for snack in elf.split('\n'):
        elf_snack_calories += int(snack)
    return elf_snack_calories

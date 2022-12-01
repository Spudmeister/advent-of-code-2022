from data_loader import data_loader


raw_data = data_loader(day=1, year=2022)

best_elf_calories = 0
for elf in raw_data.split('\n\n'):
    elf_snack_calories = 0
    for snack in elf.split('\n'):
        elf_snack_calories += int(snack)
    if elf_snack_calories > best_elf_calories:
        best_elf_calories = elf_snack_calories

print(best_elf_calories)

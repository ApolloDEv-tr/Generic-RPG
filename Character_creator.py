name = input("Name: ")
print('Choose your race:')
print('1. Human')
print('2. Elf')
print('3. Dwarf')
print('4. Angel')

race_choice = input('Enter the number of your choice: ')

if race_choice == '1':
    print('You have chosen Human.', 'You have adrealine rush and can run faster than the others.')
elif race_choice == '2':
    print('You have chosen Elf.', 'You have a natural affinity for magic and can cast spells more effectively')
elif race_choice == '3':
    print('You have chosen Dwarf.', 'You can see in the dark and get more materials from mining.')
elif race_choice == '4':
    print('You have chosen Angel.', 'You can fly for a short period of time and can heal yourself and others.')
else:
    print('Invalid choice. Defaulting to human')
    
print('Choose your class:')
print('1. Warrior')
print('2. Mage')
print('3. Tank')
print('4. Archer')
print('5. Thief')

class_choice = input('Enter the number of your choice: ')

if class_choice == '1':
    print('You have chosen Warrior.', 'You are specialized in meele combat.')
    health = 100
elif class_choice == '2':
    print('You have chosen Mage.', 'You have big mana reserves and you are skilled in spell casting.')
    health = 80
elif class_choice == '3':
    print('You have chosen  Tank', 'You have high health and high resistance to damage.')
    health = 150
elif class_choice == '4':
    print('You have chosen Archer.', 'You are skilled in ranged combat and have high dexterity.')
    health = 90
elif class_choice == '5':
    print('You have chosen Thief.', 'You are skilled in stealth and are more agile than other classes')
    health = 70
else:
    health = 100
    print('Invalid choice. Defaulting to Warrior')

print('Choose your difficulty: ')
print('1. Easy')
print('2. Medium')
print('3. Hard')
print("4. Extreme")

difficulty_choice = input('Enter the number of your choice: ')

if difficulty_choice == '1':
    health += 20
    print('You have chosen Easy difficulty. Your health has been increased by 20 and enemies deal less damage.')
elif difficulty_choice == '2':
    print('You have chosen Medium difficulty. Your health remains the same and enemies deal normal damage.')
elif difficulty_choice == '3':
    health -= 20
    print('You have chosen Hard difficulty. Your health has been decreased by 20.')
elif difficulty_choice == '4':
    health -= 20
    print('You have chosen Extreme difficulty. Your health has been decreased by 20 and enemies deal more damage.', 'Becareful, you have Permadeath.')
else:
    print('Invalid choice. Defaulting to Medium difficulty')

player = {
    'name': name,
    'race': race_choice,
    'class': class_choice,
    'health': health,
    'difficulty': difficulty_choice
}
print('Character created. Good Luck!')

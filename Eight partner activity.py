import random

print "A monster approaches! Prepare to fight!"

playerHealth = 100
monsterHealth = 100
punchDmg = 5
swordDmg = 10
fireballDmg = 30



while (monsterHealth > 0 and playerHealth > 0):
    damagebyMonster = random.randint (1,35)
    healAmount = random.randint(30,40)
    print "--------------------------------"
    print "Your health is " + str(playerHealth)
    print "The monster's health is " + str(monsterHealth)
    print "What attack to you wish to use?"
    print "1- Punch. 2- Fireball. 3- Sword. 4- Heal"
    userInput = raw_input()
    if userInput == "1":
        print "--------------------------------"
        print "You used Punch on the monster!"
        monsterHealth = monsterHealth - punchDmg   
        playerHealth = playerHealth - damagebyMonster
        print "The monster's health is " + str(monsterHealth)
        print "Oh no! The monster hit you for " + str(damagebyMonster)
    elif userInput == "2":
        print "--------------------------------"
        print "You used Fireball on the monster!"
        monsterHealth = monsterHealth - fireballDmg   
        playerHealth = playerHealth - damagebyMonster
        print "The monster's health is " + str(monsterHealth)
        print "Oh no! The monster hit you for " + str(damagebyMonster)
    elif userInput == "3":
        print "--------------------------------"
        print "You used Sword on the monster!"
        monsterHealth = monsterHealth - swordDmg
        print "The monster's health is " + str(monsterHealth)   
        playerHealth = playerHealth - damagebyMonster
        print "Oh no! The monster hit you for " + str(damagebyMonster)  
    elif userInput == "4":
        print "--------------------------------"
        print "You used Heal for " + str(healAmount)
        playerHealth = playerHealth + healAmount
        playerHealth = playerHealth - damagebyMonster
        print "Oh no! The monster hit you for " + str(damagebyMonster)
        print "The monster's health is " + str(monsterHealth)    
    elif playerHealth <= 0:
        print "--------------------------------"
        print "Uh oh! You have been slan!"
    elif monsterHealth <= 0:
        print "--------------------------------"
        print "Hoorah! You have slan the enemy!"
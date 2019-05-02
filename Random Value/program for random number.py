import random

playerHp = 260
enemyatkl = 60
enemyatkh = 80

while playerHp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    print(dmg)
    playerHp = playerHp - dmg

    if playerHp <= 0:
        playerHp = 0

    print("Enemy strikes for ", dmg, "points of damage. Current HP is ", playerHp)

    if playerHp == 0:
        print('You have died. You can not respond, as you are dead.')


'''

randrange (start, stop)

randrange ([start,] stop [,step])

Note − This function is not accessible directly, so we need to import random module and then we need to call this function using random static object.
Parameters

    start − Start point of the range. This would be included in the range.

    stop − Stop point of the range. This would be excluded from the range.

    step − Steps to be added in a number to decide a random number.

Return Value

This method returns a random item from the given range


'''    

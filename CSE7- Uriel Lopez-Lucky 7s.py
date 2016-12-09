import random
player_money = 10
round_number = 0
totrolls = 0
best = 0
while player_money > 0:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    player_money -= 1
    round_number += 1
    totrolls += 1
    dice_sum = dice1 + dice2
    if dice_sum == 7:
        print "%d + %d == %d" % (dice1,dice2,dice_sum)
        player_money += 5
        print "Congratulations, you now have $%d!" % player_money
        best = player_money
    elif dice_sum != 7:
        print "%d + %d == %d" % (dice1,dice2,dice_sum)
        print "You have $%d left." % (player_money)
        print "Your totals rolls were %d." % (totrolls)
        print "Your best was $%s." % (best)
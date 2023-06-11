def wincalc():
    try:
        print('How many wins do you have?')
        wins = input()
        print('How many losses do you have?')
        losses = input()

        totalgames = int(wins) + int(losses)
        winningpercentage = int(wins) / int(totalgames) * 100
        print('Your winning percentage in this arena is ' + str(round(float(winningpercentage), 2)) + ' %')
    except ValueError:
        print('You did not enter a number.')

wincalc()


#
print('4.  ....................')
for i in range(1, 6):
    if i < 6:
        svar = input('Are you tired? (yes/no):')
        if svar == 'yes':
            print("You didn't finish the race")
            break
        else:
            print("Keep it up, you have finished lap ", i)
            continue
    else:
        print("Congratulations! You have finished the race!")



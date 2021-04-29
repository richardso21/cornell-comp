# not sus yet 😳
sus = False
night = False
walnuts = False
catDog = False
askedWorked = False
names = set()

while True:
    dialog = input()
    # end of day
    if dialog == "all the birds":
        break

    # is he saying Hi properly?
    elif "Hi " in dialog:
        if dialog == "Hi Daniel":
            sus = True
        # append to names to say
        sp = dialog.split()
        if len(sp) > 2:
            sus = True
        name = sp[1]
        if name == "Roger":
            name = "Daniel"
        names.add(name)

    # if 'night night'
    elif dialog == 'night night':
        if night == True:
            sus = True
        night = True

    # if 'mmmmmm'
    elif dialog == 'mmmmmm':
        if night == False:
            sus = True
        walnuts = True

    # if what are you doing
    elif dialog == 'what are you doing':
        if night == True or askedWorked == True:
            sus = True
        askedWorked = True

    elif dialog == "awwww kitty":
        catDog = True

    elif dialog not in ["Kermit", "Kermit Kermit", "Kermit Kermit Kermit"]:
        sus = True

# night night must be said!
if night == False:
    sus = True

if sus:
    print("Im-parrot-ator!")
else:
    print("Could be Kermit")
    if walnuts:
        print("He had walnuts")
    for name in sorted(list(names)):
        print(f'He saw {name}')
    if askedWorked:
        print("His human worked from home")
    if catDog:
        print("There was a cat or a small dog")
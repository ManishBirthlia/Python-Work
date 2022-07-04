# defining game 
def GHS():
    return 56455

# updating game high score
with open('High_score_game.txt','r') as f:
    score=int(f.read()[-6:])
# Condition
if GHS()>=score:
    with open('High_score_game.txt','w') as f:
        f.write('your highest score is    ')
    with open('High_score_game.txt','a') as f:
        f.write(f"{GHS()}")
else:
    pass
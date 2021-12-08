import random

msg_ = [""] * 15
msg_[0] = "Stock pieces:"
msg_[1] = "Computer pieces:"
msg_[2] = "player pieces:"
msg_[3] = "Domino snake:"
msg_[4] = "Status:"
msg_[5] = "=" * 70
msg_[6] = "Stock size:"
msg_[7] = "Your pieces:"
msg_[8] = "Computer pieces:"
msg_[9] = "Status: Computer is about to make a move. Press Enter to continue..."
msg_[10] = "Status: It's your turn to make a move. Enter your command."
msg_[11] = "Invalid input. Please try again."
msg_[12] = "Status: The game is over. You won!"
msg_[13] = "Status: The game is over. The computer won!"
msg_[14] = "Status: The game is over. It's a draw!"
#

def format_tab(t, n=""):
    res = "tab " + n + "\n"
    for i in range(len(t)):
        res += str(i) + ":" + str(t[i]) + ", "
    return(res)  # , sep='\n'

def format_snake(t):
    res = ""
    t_len = len(t)
    for i in range(t_len):
        if t_len > 6 and i == 3:
            i = t_len -3
            res += "..."
        res += str(t[i])
    return(res)

def format_pieces(t):
    res = ""
    for i in range(len(t)):
        res += str(i + 1) + ":" + str(t[i]) + "\n"
    return res

def is_str_int(v):
    res = False
    if len(v) > 0:
        if v[0] == "-":
            v = v[1:]

        if v.isdigit():
            res = True
    return res

def comp_input():
    a = input()
    a = random.randint(-len(game["computer"]), len(game["computer"]))
    print("comp select", a)
    return a
    

def player_input(s="player"):
    a_is_right = False
    a = 0
    while not a_is_right:
        #print(msg_[3])
        a = input()
        if is_str_int(a):
            a = int(a)
            if abs(a) <= len(game[s]):
                a_is_right = True
        else:
            print(msg_[11])
            # continue
    return a


status = ""
while not status:
    stock = [[a, b] for a in range(7) for b in range(a, 7)]
    random.shuffle(stock)
    comp = stock[0:7]
    player = stock[7:14]
    stock[:14] = []
    
    # print("-------")
    # print(format_tab(stock, "stock"))
    # print(format_tab(comp, "computer"))
    # print(format_tab(player, "player"))

    i = 6
    status = ""
    while not status and i >= 0:
        hit = [i, i]
        if hit in comp:
            status = "computer"
            
        elif hit in player:
            status = "player"
        i += -1
        
game = {"stock":stock,
        "computer":comp,
        "player":player,
        "snake":[hit],
        "first":status
        }

#print("status", status, game[status].index(hit), hit)
#print("-------")
# print(hit, game[status][game[status].index(hit)])

del game[status][game[status].index(hit)]
# print(msg_[0], game["stock"])
# print(msg_[1], game["computer"])
# print(msg_[2], game["player"])
# print(msg_[3], game["snake"])
# print(msg_[4], status)

while status == "player" or status == "computer":
    
    if status == "player":
        status = "computer"
    else:
        status = "player"
    
    print(msg_[5])  # ======
    print(msg_[6], len(game["stock"]))
    print(msg_[8], len(game["computer"]))
    print()
    print(format_snake(game["snake"]))
    print()
    print(msg_[7])
    print(format_pieces(game["player"]))
    print()
    
    
    
    if status == "computer":
        print(msg_[9])
        ans = comp_input()
    else:
        print(msg_[10])
        ans = player_input()
    if ans == 0:
        if len(game["stock"]) > 0:
            i = len(game["stock"])
            game[status].append(game["stock"].pop(i - 1))
    else:
        i = 0
        if ans > 0:
            i = len(game["snake"])
        game["snake"].insert(i, game[status].pop(abs(ans) - 1))
    

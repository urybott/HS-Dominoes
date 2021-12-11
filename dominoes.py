import random

msg_ = [""] * 20
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
msg_[15] = "Stock is empty!"
msg_[16] = "Illegal move. Please try again."
#

def format_tab(t, n=""):
    res = "tab " + n + "\n"
    for i in range(len(t)):
        res += str(i) + ":" + str(t[i]) + ", "
    return(res)

def format_snake(t):
    res = ""
    t_len = len(t)
    if t_len > 6:
        t[3:t_len-3] = ["..."]
        t_len = len(t)
    for i in range(t_len):
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
        if v[0] == "-" or v[0] == "+":
            v = v[1:]
        if v.isdigit():
            res = True
    return res

def check_input(hit):
    i = 0
    a = 0
    if hit > 0:
        i = len(game["snake"])
        a = 1
    b = 1 - a
    c = game[status][abs(hit) - 1]
    d = game["snake"][i - a]
    return d[a] in c  # c[b] d[a]

def count_nums(p="computer"):
    s = {x: 0 for x in range(8)}
    d = game["snake"] + game[p]
    for el in d:
        for n in el:
            s[n] += 1
    return s

def hit_reting(p="computer"):
    s = count_nums(p)
    d = {}
    for el in game[p]:
            d[tuple(el)] = s[el[0]] + s[el[1]]
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

def comp_input():
    a_is_right = False
    # print(format_pieces(game["computer"]))
    a = input()
    a = 0
    while 0:  # not a_is_right:
        a = random.randint(-len(game["computer"]), len(game["computer"]))
        # print("comp select", a, game[status][abs(a) - 1])
        if a == 0 or check_input(a):
            a_is_right = True
        # else:
            # print(msg_[16])
    b = game["snake"][0][0]
    e = game["snake"][-1][1]
    d = hit_reting("computer")
    # print("hit_reting", d)
    for el in d:
        if e in el:
            a = game["computer"].index(list(el)) + 1
            break
        elif b in el:
            a = -(game["computer"].index(list(el)) + 1)
            break
    # print("comp select :", a)
            
    return a
    

def player_input(s="player"):
    a_is_right = False
    a = 0
    m = 11
    while m:
        # print(msg_[3])
        m = 11
        a = input()
        if is_str_int(a):
            a = int(a)
            if a == 0:
                m = 0
            elif abs(a) > len(game[s]):
                m = 11
            elif check_input(a):
                m = 0
            else:
                m = 16

        if m:
            print(msg_[m])
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
    
snake = [hit]  # [[a, 0] for a in range(7)]  # 
        
game = {"stock":stock,
        "computer":comp,
        "player":player,
        "snake":snake,
        "first":status
        }

# print("status", status, game[status].index(hit), hit)
# print("-------")
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
    print(format_snake(game["snake"].copy()))
    print()
    print(msg_[7])
    print(format_pieces(game["player"]))
    print()
    
    if len(game["computer"]) == 0:
        print(msg_[13])
        break
    if len(game["player"]) == 0:
        print(msg_[12])
        break
    if len(game["snake"]) > 6 and game["snake"][0][0] == game["snake"][-1][-1]:
        s = [a for b in game["snake"] for a in b]
        if s.count(s[0]) == 8:
            print(msg_[14])
            break
        
    
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
        #else:
        #    print(msg_[15])
    else:
        i = 0
        a = 0
        if ans > 0:
            i = len(game["snake"])
            a = 1
        b = 1 - a
        c = game[status].pop(abs(ans) - 1)
        d = game["snake"][i - a]
        if d[a] != c[b]:
            c.reverse()
        game["snake"].insert(i, c)
        
    

import random
imp_loc = ["<",">","_","~",":","#"]
mobs = ["g","o","t","D"]
items = ["s","d","b",""]
has_door = False
player_name= raw_input("What is your name?")
player_chara = player_name[:1]
room_rng = random.randrange(1,10,)
def room_gen(rng):
    room_dim = rng * 2
    def room(dim):
        border = False
        print dim
        for i in range(0,dim):
            if i == 0 or i == dim-1:
                border = True
            else:
                border = False
            if border:
                print "-" * (dim+2)
            elif border == False:
                print "|" + "." * dim + "|"
            elif has_door == False:
                room_door():
    def room_door():
        if has_door == False:
            for j in range(1,room_dim-2):
                door_rng = random.randrange(0,10)
                if door_rng == j:
                    print imp_loc[4]
                    has_door = True
# 'g' stands for green (+1)
# '0' stands for white (-0.04)
# 'b' stands for brown (-1)
# 'w' stands for walls (Wall)
# 's' stands for start (Start)

#get reward from symbol
def get_reward(position,map):
    symbol = map[position[0]][position[1]]
    match symbol:
        case 'g':
            return 1
        case '0':
            return -0.04
        case 'b':
            return -1
        case _:
            return 0

#get possible action from position
def get_value(position,state_value):

    return state_value[position[0]][position[1]]

#get destination from position and action
def get_destination(position,action,map):

    if (position[0]+action[0] < 0) or (position[0]+action[0] > 5) or (position[1]+action[1] < 0) or (position[1]+action[1] > 5) or  map[position[0]+action[0]][position[1]+action[1]]=='w':
        new_position= position
    else:
        new_position = [position[0] + action[0], position[1] + action[1]]

    return new_position

def value_of_action(position,action,map):
    if action[0] == 0:
        action1 = [1 ,0]
        action2 = [-1,0]
    else:
        action1 = [0 , 1]
        action2 = [0 ,-1]

    straight_value = get_value(get_destination(position,action,map),state_value)*GAMMA + get_reward(get_destination(position,action,map),map)
    turn_value1 = get_value(get_destination(position,action1,map),state_value)*GAMMA + get_reward(get_destination(position,action1,map),map)
    turn_value2 = get_value(get_destination(position, action2, map),state_value)*GAMMA + get_reward(get_destination(position,action2,map),map)

    average_value = straight_value*0.8 + (turn_value1 + turn_value2)*0.1

    return average_value

# (row,column) format
map= [
    ['g','0','0','0','0','0'],
    ['w','b','0','0','w','0'],
    ['g','0','b','s','w','0'],
    ['0','g','0','b','w','0'],
    ['0','w','g','0','b','0'],
    ['g','b','0','g','0','0'],
    ]

#initialize_state_value table
state_value = [[0]*6 for i in range(6)]

#initialize policy table
policy_table = [[[0,1] for k in range(6)] for j in range(6)]

#accuracy threshold variable
THETA = 0.01

#Discount factor
GAMMA = 0.99

#Possible Action
action = [
    [0,1], [0,-1], [1,0], [-1,0]
]

policy_stable_flag = False
while not policy_stable_flag:
    #maximum error variable
    ERROR = 1
    while ERROR > THETA:
    #for i in range(30):
        ERROR = 0
        for row in range(6):
            for column in range(6):

                old_v = get_value([row,column],state_value)

                #update state_value

                state_value[row][column] = value_of_action([row,column],policy_table[row][column],map)

                ERROR = max(ERROR,abs(old_v - state_value[row][column]))

    #policy improvement
    policy_stable_flag = True
    for row in range(6):
        for column in range(6):
            old_action = policy_table[row][column]
            max_value= float('-inf')
            for a in action:
                a_value = value_of_action([row,column],a,map)
                if a_value >= max_value:
                    max_value = a_value
                    new_action = a
            policy_table[row][column] = new_action
            if old_action != new_action:
                policy_stable_flag = False
    print(state_value)









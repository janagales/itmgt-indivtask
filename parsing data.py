'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
     
    follower = False
    followed_by = False
    
    if to_member in social_graph[from_member]["following"]:
        follower = True
        
    if from_member in social_graph[to_member]["following"]:
        followed_by = True
        
    if follower and followed_by:
        return "friends"
    elif follower:
        return "follower"
    elif followed_by:
        return "followed by"
    else:
        return "no relationship"


board1 = [
        ['X','X','O'],
        ['O','X','O'],
        ['O','','X'],
    ]

board2 = [
        ['X','X','O'],
        ['O','X','O'],
        ['','O','X'],
    ]

board3 = [
        ['O','X','O'],
        ['','O','X'],
        ['X','X','O'],
    ]

board4 = [
        ['X','X','X'],
        ['O','X','O'],
        ['O','','O'],
    ]

board5 = [
        ['X','X','O'],
        ['O','X','O'],
        ['X','','O'],
    ]

board6 = [
        ['X','X','O'],
        ['O','X','O'],
        ['X','',''],
    ]

board7 = [
        ['X','X','O',''],
        ['O','X','O','O'],
        ['X','','','O'],
        ['O','X','','']
    ]

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
def tic_tac_toe(board):    
    for i in range(0, len(board)):
        X = True
        O = True
        for j in range(0, len(board[i])):
            if board[i][j] == 'O':
                X = False
            elif board[i][j] == 'X':
                O = False
            elif board[i][j] == '':
                X = False
                O = False
        if X:
            return 'X'
        if O:
            return 'O'


    for i in range(0, len(board)):
        X = True
        O = True    
        for j in range(0, len(board[i])):
            if board[j][i] == 'O':
                X = False
            elif board[j][i] == 'X':
                O = False
            elif board[j][i] == '':
                X = False
                O = False
        if X:
            return 'X'
        if O:
            return 'O'
    
    X = True
    O = True    
    for i in range(0, len(board)):
        if board[i][i] == 'O':
            X = False
        elif board[i][i] == 'X':
            O = False
        elif board[i][i] == '':
            X = False
            O = False
    if X:
        return 'X'
    if O:
        return 'O'
    
    X = True
    O = True    
    for i in range(0, len(board)):
        if board[i][len(board) - 1 - i] == 'O':
            X = False
        elif board[i][len(board) - 1 - i] == 'X':
            O = False
        elif board[i][len(board) - 1 - i] == '':
            X = False
            O = False
    if X:
        return 'X'
    if O:
        return 'O'

    return 'no winner'
                       

legs1 = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}        

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    routes = list()
    times = list()
    
    for key in route_map:
        routes.append(key[0])
        times.append(route_map[key]['travel_time_mins'])
    
    i_1 = routes.index(first_stop)
    i_2 = routes.index(second_stop)
    total = 0
                                    
    if i_1 < i_2:
        for i in range(i_1, i_2):
            total += times[i]
    
    else:
        for i in range(i_1, len(routes)):
            total += times[i]
        for i in range(0, i_2):
            total += times[i]
    
    return total
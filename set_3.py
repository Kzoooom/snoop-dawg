'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

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

#to_member and from_member are parameters within the dictionary
#from_member and to_member are either the first keys of the dictionary or the values in 'following'
    follower = to_member in social_graph.get(from_member, {}).get('following', [])
    followed = from_member in social_graph.get(to_member,{}).get('following', [])

#boolean data types; check if true
    if follower and followed:
        return "friends"

    elif follower:
        return "follower"
    
    elif followed:
        return "followed by"

    else:
        return "no relationship"

from_member="@eeebeee"
to_member="@jobenilagan"
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
relationship_status(from_member, to_member, social_graph)


def tic_tac_toe(board):
    '''Tic Tac Toe.

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
    #get the number of lists (which is the also the number of rows and columns since rows=columns)
    dimensions = len(board) 
    #this should count how many entities (or lists, in this context) are in the list 
    #if there are visibly 3 rows, the length of the board should be 3 (or 3x3 if u think about it)
    
    #STRAIGHTS
    for row in board:
        #row should be the entity or the list in the list
        if len(set(row))==1 and all(symbol != "" for symbol in row):
            #this respectively checks if there is only 1 symbol in a row and there are no empty values
            return row[0] #this returns the winning symbol, aka the first value of the row or nested list
        
    length = range(dimensions)
    #goes through the i-th value of the row, serving as columns
    for i in length:
        column = [board[j][i] for j in length]
        #j is the row (or nested list) and i is the column (or the i-th value in the row)
        if len(set(column))==1 and all(symbol != "" for symbol in column):
            return column[0]
        
    #DIAGONALS    
    diagonal_left = [board[i][i] for i in length]
    diagonal_right = [board[i][dimensions-i-1] for i in length]
    if len(set(diagonal_left))==1 and all(symbol != "" for symbol in diagonal_left):
        return diagonal_left[0]
    if len(set(diagonal_right))==1 and all(symbol != "" for symbol in diagonal_right):
        return diagonal_right[0]
    
    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    '''ETA.

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
    # Check if the destination is directly reachable from the origin
    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]['travel_time_mins']
    else:
        # If the destination is not directly reachable, find shortest path
        # by iterating through the route_map and summing the travel times
        total_time = 0
        current_stop = first_stop
        while current_stop != second_stop:
            # Find the next stop in the route
            for stop, travel_info in route_map.items():
                if stop[0] == current_stop:
                    next_stop = stop[1]
                    total_time += travel_info['travel_time_mins']
                    current_stop = next_stop
                    break
        return total_time
#%%
import csv 

def make_all_stops():
    all_stops = []  
    all_lines = []                                                              # List for all stops
    for i in range(1,13):                                                       # For loop to iterate through the 12 metro lines
        with open("data/linea-"+str(i)+".csv") as file:                         # Open the specific file of each metro line
            fileReader = csv.reader(file)                                       # Open reader   
            holder = []      
            for i in fileReader:                                                # Iterate through reader
                all_stops.append(i[0])
                holder.append(i[0])                                             # For each stop in each line append
            all_lines.append(holder)

    return all_stops, all_lines                                                 # Returning a list with all stops, and all lines

(all_stops, all_lines)  = make_all_stops()                                      # Destructuring

# neighbour_stations() method: Helper function for exercise_4, produces a dictionary where the keys are all stations 
# in madrid metro system and the values are lists with all the stations that are one stop away.
def neighbour_stations() -> dict:                                               # Loading up data
    neighbour_dict = {}                                                         # Dictionary (keys: stations, values: list with neighbour stations)          

    for line in all_lines:                                                      # Iterating though all lines in the metro system
        for station in line:                                                    # Iterating though all stations in the line
            if station not in neighbour_dict:                                   # Itroducing each station if they are not already in the dictionary
                neighbour_dict[station] = exercise_3(station)                   # Calling exercise_3 that returns a list with the neighbour stations

    return neighbour_dict                                                       # Method returns a dictionary that represents a graph!!!!


# exercise_1(): COUNTING THE NUMBER OF METRO STATIONS - Create a function exercise_1 in main.py that returns the number of stations that 
# exist in the Metro network (according to the data you have in the CSV files)
def exercise_1():
    metro_stops = set(all_stops)                                                # Eliminating repeated stops with set

    return len(metro_stops)                                                     # Returns the number of stations which is equal to the set length


# exercise_2(): MOST CONNECTED STATIONS - Create a function exercise_2 in main.py that returns a list of the top 5 stations by number of 
# lines available in them, sorted by which one has more lines available.
def exercise_2():
    dictionary = dict()                                                         # Dictionary that will store the 5 stations with more number of correspondeces
    for stop in all_stops:                                                      # Iterating though the list of all stops
        if stop in dictionary.keys():                                           # If station in dictionary,
            dictionary[stop] += 1                                               # increase number by one
        else:                                                                   # If station not in dictionary,
             dictionary[stop] = 1                                               # set number to one to initialize 

    result = sorted([(v, k) for (k, v) in dictionary.items()], reverse=True)
    result = [k for (v, k) in result]
    return result[:5]                                                           # Returning a list with the 5 largest stations

# exercise_3(station: str): CLOSEST STATIONS - Create a function exercise_3 in main.py that receives a Metro station name 
# and returns a list with other stations that are one stop away.
def exercise_3(station):
    circular_indexes = [5, 11]                                                  # Taking into account circular lines (6 and 12) but their indexes in my_metro are 5 and 11
    near_stations = [] 
    
    for linea in all_lines:                                                     # Iterating though the lines in 'my_metro'
        for estacion in linea:                                                  # Iterating through the stations in each line
            index = linea.index(estacion)                                       # Index of the station in the line (starting at 0)
            if (estacion == station):                                           # If we find the station
                if (linea.index(station)== 0):                                  # If the station is the first stations in the line
                    near_stations.append(linea[index+1])                        # Just append the next one
                    if all_lines.index(linea) in circular_indexes:              # Unless it is a circular line, where you have to continue the line from the end
                        near_stations.append(linea[len(linea)-1])
                elif(linea.index(station)== len(linea)-1):                      # If the station is the last station in the line
                    near_stations.append(linea[index-1])                        # Just append the previous one
                    if all_lines.index(linea) in circular_indexes:              # Unless it is a circular line, where you have to continue the line from the beginning
                        near_stations.append(linea[0])
                else:                                                           # If the station is not the last nor the first
                    near_stations.append(linea[index+1])                        # Append the next station
                    near_stations.append(linea[index-1])                        # Append the previous station

    return list(set(near_stations))                                             # Returns a list with the nearest stations

# # Path() class: This class helps us store variables that we can modify thoughout the recursion
# class Path: 
#     def __init__(self, origen: str, destino: str):                              # Constructor that initiates the attributes of the class
#         self.origin = origen                                                    # origin specified by user
#         self.destination = destino                                              # destination specified by user
#         self.found = False                                                      # found boolean, flag for when we find the destination in the recursion
#         self.tour = []                                                          # List that will store the stations of the first path we find
#         self.visited = [origen]                                                 # List that stores the stations that have been visited in the recursion, Origin is the first station that is visited
    
#     def detected(self):                                                         # Method to change found flag to true when we find the destination and exit the recursion
#         self.found = True


# # aventurero() method: recursive finction that calls itself to explore each of the neighbour nodes of each input node
# def aventurero (nodito: str, caminito: Path, correspondencias: dict):
#     for child in correspondencias[nodito]:                                      # Iterating through the neighbour nodes
#         if child in caminito.visited:                                           # If the node has been already visited we are not interested in exploring it again
#             continue                                                            # so we skip this iteration
#         else:
#             caminito.visited.append(child)                                      # If the node has not been visited, we append it to the visited nodes list of the class Path()

#         if child == caminito.destination:                                       # If the station we are exploring is equal to the destination
#             caminito.detected()                                                 # We have found the right path so we change the found flag in the class Path()
#         else:
#             aventurero(child, caminito, correspondencias)                       # It the node we are exploring is not the destination we call the function again to explore its children (or neighbouring stations)
        
#         if caminito.found == True:                                              # If we have found the destination
#             caminito.tour.append(child)                                         # We append the station to the tour list in the Path() class to store in the list all the stations of the first path found
#             return 


# # exercise_4(start: str, end: str): FINDING A ROUTE - Create a function exercise_4 in main.py that receives the names 
# # of two Metro stations as parameters, and returns a way to go from one to another, in case there's a way. The returned data 
# # should be a list containing all Metro stations one would need to go through from start to finish.
# def exercise_4(start: str, end: str) -> list: 
#     correspondences = neighbour_stations()                                      # Calling neighbour_stations() helper functions to obtain the adjacencies graph dictionary
#     caminito_de_la_muerte = Path(start, end)                                    # Declaring a Path() object to store all the variables we will need, this will allow us more freedom to manipulate the data 

#     aventurero(start, caminito_de_la_muerte, correspondences)                   # Calling recursive function for the origin node, function receives the node, the class, and the adjacencies dictionary
#     caminito_de_la_muerte.tour.append(start)                                    # Not forgetting about the first node
#     return caminito_de_la_muerte.tour[::-1]                                     # The recursive function returns the reversed tour path so we return that same list but inverted


# # exercise_4(start: str, end: str): FINDING A ROUTE - Create a function exercise_4 in main.py that receives the names 
# # of two Metro stations as parameters, and returns a way to go from one to another, in case there's a way. The returned data 
# # should be a list containing all Metro stations one would need to go through from start to finish.

# DIJKSTRA'S ALGORITHM IMPLEMENTATION
def exercise_4(start_station, end_station, adjacency_List: dict = neighbour_stations()):
    def solve( graph, node1, node2):
        path_list = [[node1]]
        path_index = 0
        previous_nodes = {node1}
        if node1 == node2:
            return path_list[0]
            
        while path_index < len(path_list):
            current_path = path_list[path_index]
            last_node = current_path[-1]
            next_nodes = graph[last_node]
            if node2 in next_nodes:
                current_path.append(node2)
                return current_path
            for next_node in next_nodes:
                if not next_node in previous_nodes:
                    new_path = current_path[:]
                    new_path.append(next_node)
                    path_list.append(new_path)
                    previous_nodes.add(next_node)
        
            path_index += 1
        return []

    return solve(adjacency_List, start_station, end_station)


######################################################################################################################################################
# CHECKING EVERYTHING WORKS PERFECTLY 

#%% EXERCISE 1: --------------------------------------------------------------------------------------------------------------------------------------

print("The number of stations in madrid metro is: " + str(exercise_1()))

#%% EXERCISE 2: --------------------------------------------------------------------------------------------------------------------------------------

print("The 5 stations with more correspondences are: " )
big_stations = exercise_2()
i = 1
for station in big_stations: 
    print(str(i) + ". " + station)
    i+=1
print("DISCLAIMER: note that there are several stations with 3 correspondences")


#%% EXERCISE 3: --------------------------------------------------------------------------------------------------------------------------------------
my_station = "Avenida de América"                               # Insert the station you want to explore 
stations_one_stop_away = exercise_3(my_station)                 # Calling exercise 3: returns a list with the nearest stations
print("The neighbour stations for " + my_station + " are:")     # Answer header
for station in stations_one_stop_away:                          # Iterating through the list and printing each station
    print("-> " + station)


#%% EXERCISE 4: --------------------------------------------------------------------------------------------------------------------------------------

my_origin = "Avenida de América"                                # Insert the origin station
my_destination = "Fuencarral"                                   # Insert where you want to go
my_journey = exercise_4(my_origin, my_destination)              # Calling exercise 4, returns a list with the tour we have to take

print("You will have to go through the next stations to reach you destination:")
i = 1
for station in my_journey:                                      # Iterating through the list 
    if i == 1:
        print(str(i) + ". "+ station + " -> Origin")            # If it is the origin, letting the user know
    elif i == len(my_journey):
        print(str(i) + ". "+ station + " -> Destination")       # If it is the destination, letting the user know
    else:
        print(str(i) + ". "+ station)
    i += 1

# %%

from roadmap import RoadMap
from environment import Environment
from ant import Ant


map_size = 10
population_size = 10
ant_number = 2
ant_or_vehicle = False  #true for constructing ant and false for vehicle
environment = Environment(map_size, ant_number, ant_or_vehicle)

myMap = RoadMap(10)

myMap.show_map()
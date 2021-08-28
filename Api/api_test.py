from connector import Connector

connector = Connector()

name = str(input('Name (string): '))
size_x = int(input('size_x (positive integer): '))
size_y = int(input('size_y (positive integer): '))

data_for_create_galaxy = {
   "name": name,
   "size_x": size_x,
   "size_y": size_y
}
print(connector.create("galaxies", data_for_create_galaxy))

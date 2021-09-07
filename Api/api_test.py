import time
from connector import Connector

con = Connector()

q1 = str(input('What do you want to create? (gAlaxy, sTarsystem, staR, pLanet): ')).lower()

if q1 == 'a':
    response = con.get_list('galaxies')['results']
    print('List of galaxies: ', response)
    time.sleep(1.5)
    print('Enter data...')
    time.sleep(1.5)
    data = {
        'name': input('Input name: '),
        'size_x': input('Input size-x: '),
        'size_y': input('Input size-y: ')
    }

    print(con.create('galaxies', data))

elif q1 == 't':
    response = con.get_list('starsystems')['results']
    print('list of star systems: ', response)
    time.sleep(1.5)
    print('Enter data...')
    time.sleep(1.5)
    data = {
        'name': input('Input name: '),
        'position_x': input('Input position-x: '),
        'position_y': input('Input position-y: '),
        'galaxy': input(
            '{}\nChoose a galaxy please (needed id key value): '.format(con.get_list('galaxies')['results'])
        )
    }

    print(con.create('starsystems', data))

elif q1 == 'r':
    response = con.get_list('stars')['results']
    print('list of stars: ', response)
    time.sleep(1.5)
    print('Enter data...')
    time.sleep(1.5)
    data = {
        'name': input('Input name: '),
        'diameter': input('Input diameter: '),
        'color': input('Input color: '),
        'starsystem': input(
            '{}\nChoose a star system please (needed id key value): '.format(con.get_list('starsystems')['results'])
        )
    }

    print(con.create('stars', data))

elif q1 == 'l':
    response = con.get_list('planets')['results']
    print('list of planets: ', response)
    time.sleep(1.5)
    print('Enter data...')
    time.sleep(1.5)
    data = {
        'name': input('Input name: '),
        'diameter': input('Input diameter: '),
        'color': input('Input color: '),
        'life': input('Input life (boolean): '),
        'starsystem': input(
            '{}\nChoose a star system please (needed id key value): '.format(con.get_list('starsystems')['results'])
        )
    }

    print(con.create('planets', data))

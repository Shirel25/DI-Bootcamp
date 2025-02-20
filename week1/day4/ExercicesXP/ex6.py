magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(list):
    for magician in list:
        print(magician)

show_magicians(magician_names)

def make_great(list):
    for i in range(len(list)):
        list[i] = list[i] + " the Great"
    
make_great(magician_names)
show_magicians(magician_names)
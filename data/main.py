from data import get_data, load_data
# while True :
#     vedenia = int(input("fjfjf"))
#     if vedenia == 1 :
#         create_hall(file_path)
#     elif vedenia == 2 :
#         pass
#     elif vedenia == 3 :
#         pass
#     elif vedenia == 4 :
#         pass
#     elif vedenia == 5 :
#         pass
#     elif vedenia == 0 :
#         break
        
def show_empty_seats(file_path) :
    halls = get_data(file_path)
    hall_name = input("name")
    if hall_name not in halls :
        print("fdsa")
    else:
        selected = halls[hall_name]
        empty = []
        seats = selected.values()
        for seat in selected :
            for key, value in seat.items():
                if value is False:
                    empty.append(key)
        return empty






def create_hall(file_path) :
    content = get_data(file_path)
    hall = input("hall")
    if hall in content :
        print("already have")
    else:
        riad = int(input("riad"))
        col = int(input("col"))
        new = {hall:[]}
        for i in range(1, riad) :
            for j in range(1, col) :
                seat = {f"{i, j}": False}
                new[hall].append(seat)
        hall.update(new)
    load_data(hall, file_path)

create_hall("kse_pb\data\cinema_halls.json")



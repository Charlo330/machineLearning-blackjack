import csv


def write_data(data):
    with open('data.csv', 'a', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f, delimiter=';')
        # write a row to the csv file
        writer.writerows(data)


def get_total_game_win_lost():
    total_win = 0
    total_lost = 0
    total_game = 0
    # open the file in the read mode
    with open('data.csv', 'r', encoding='UTF8') as f:
        # create the csv reader
        reader = csv.reader(f, delimiter=';')
        # create a list of lists
        data = list(reader)

    for row in data:
        total_win += int(row[0])
        total_lost += int(row[1])
        total_game += int(row[2])
    return total_win, total_lost, total_game


# V1


def write_storage_data(data):
    with open('storage.csv', 'w', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f, delimiter=';')
        # write a row to the csv file
        for single_data in data:
            writer.writerow(single_data)


def get_storage_data():
    with open('storage.csv', 'r', encoding='UTF8') as f:
        # create the csv reader
        reader = csv.reader(f, delimiter=';')
        # create a list of lists
        data = list(reader)
    return data

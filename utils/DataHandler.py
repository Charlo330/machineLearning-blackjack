from utils.csvHandler import get_storage_data, write_storage_data

global found


class DataHandler:

    data = []

    @staticmethod
    def init_data():
        DataHandler.data = get_storage_data()

    @staticmethod
    def get_data():
        return DataHandler.data

    @staticmethod
    def set_data(data):
        DataHandler.data = data

    @staticmethod
    def store_data():
        write_storage_data(DataHandler.data)

    @staticmethod
    def get_data_by_player_dealer_hand(player_hand, dealer_hand):
        for single_data in DataHandler.data:
            if int(single_data[0]) == player_hand and int(single_data[1]) == dealer_hand:
                if int(single_data[3]) > int(single_data[4]):
                    return single_data[2]
                else:
                    if single_data[2] == 'HIT':
                        return 'HOLD'
                    else:
                        return 'HIT'
        return None

    @staticmethod
    def get_data_by_player_dealer_hand_figure_out(player_hand, dealer_hand, nb_figure_out):
        for single_data in DataHandler.data:
            if int(single_data[0]) == player_hand and int(single_data[1]) == dealer_hand and nb_figure_out == int(single_data[2]):
                if int(single_data[4]) > int(single_data[5]):
                    return single_data[3]
                else:
                    if single_data[3] == 'HIT':
                        return 'HOLD'
                    else:
                        return 'HIT'
        return None

    @staticmethod
    def add_data(shot):
        index = 0
        find = 0
        for single_data in DataHandler.data:
            if single_data[0] == shot[0] and single_data[1] == shot[1] and single_data[2] == shot[2]:
                find = 1
                if shot[3] == "WIN":
                    DataHandler.data[index] = [single_data[0], single_data[1], single_data[2],
                                               single_data[3] + 1, single_data[4]]
                else:
                    DataHandler.data[index] = [single_data[0], single_data[1], single_data[2], single_data[3],
                                               single_data[4] + 1]
                return
            index += 1

        if find == 0:
            if shot[3] == "WIN":
                format_data = [shot[0], shot[1], shot[2], 1, 0]
            else:
                format_data = [shot[0], shot[1], shot[2], 0, 1]

            DataHandler.data.append(format_data)

    @staticmethod
    def add_data_with_figure(shot):
        index = 0
        find = 0
        for single_data in DataHandler.data:
            if (single_data[0] == shot[0] and single_data[1] == shot[1] and single_data[2] == shot[2]
                    and single_data[3] == shot[3]):

                find = 1
                if shot[4] == "WIN":
                    DataHandler.data[index] = [single_data[0], single_data[1], single_data[2],
                                               single_data[3], single_data[4] + 1, single_data[5]]
                else:
                    DataHandler.data[index] = [single_data[0], single_data[1], single_data[2], single_data[3],
                                               single_data[4], single_data[5] + 1]
                return
            index += 1

        if find == 0:
            if shot[3] == "WIN":
                format_data = [shot[0], shot[1], shot[2], shot[3], 1, 0]
            else:
                format_data = [shot[0], shot[1], shot[2], shot[3], 0, 1]

            DataHandler.data.append(format_data)

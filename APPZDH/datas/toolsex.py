import xlrd
class Dates():

    def data_Dl_ex(self):
        data = xlrd.open_workbook("../datas/mishiyuan_login.xlsx")
        table = data.sheet_by_name("login")
        e_list = []
        for n_row in range(1, table.nrows):
            e_list.append(table.row_values(n_row))
        return (e_list)


# print(data_Dl_ex()[0])
    def data_Dl_rex(self):
        data = xlrd.open_workbook("../datas/mishiyuan_login.xlsx")
        table = data.sheet_by_name("register")
        e_list = []
        for n_row in range(1, table.nrows):
            e_list.append(table.row_values(n_row))
        return (e_list)
import json

class Data_file:

    data_clientes = []
    data_pelis = []

    def __init__(self):
        pass

    def data_readClientes(self):
        with open("data/clientes.json", "r") as file:
            data = json.load(file)
            for row in data['results']:
                self.data_clientes.append(row)

    def data_readPelis(self):
        with open("data/peliculas.json", "r") as file:
            data = json.load(file)
            for row in data['results']:
                self.data_pelis.append(row)


    def data_campoName(self,camponame):
        list_temp = []
        for row in self.data_clientes:
            campo = row[camponame]
            if campo not in list_temp:
                list_temp.append(campo)
        return list_temp

    def data_campoMovie(self,camponame):
        list_temp = []
        for row in self.data_pelis:
            campo = row[camponame]
            if campo not in list_temp:
                list_temp.append(campo)
        return list_temp


    def data_getClientes(self):
        return self.data_clientes

    def data_getPelis(self):
        return self.data_pelis

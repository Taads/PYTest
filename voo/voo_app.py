class SistemaReservas:
    def __init__(self):
        self.voos = []
        self.reservas = {}

    def adicionar_voo(self, voo):
        self.voos.append(voo)

    def pesquisar_voos(self, origem, destino):
        voos_disponiveis = [voo for voo in self.voos if voo.origem == origem and voo.destino == destino and voo.assentos > 0]
        return voos_disponiveis

    def realizar_reserva(self, id_voo):
        for voo in self.voos:
            if voo.id_voo == id_voo and voo.assentos > 0:
                voo.assentos -= 1
                self.reservas[id_voo] = self.reservas.get(id_voo, 0) + 1
                return True
        return False

    def visualizar_reservas(self):
        return self.reservas

    def cancelar_reserva(self, id_voo):
        if id_voo in self.reservas and self.reservas[id_voo] > 0:
            self.reservas[id_voo] -= 1
            for voo in self.voos:
                if voo.id_voo == id_voo:
                    voo.assentos += 1
                    return True
        return False
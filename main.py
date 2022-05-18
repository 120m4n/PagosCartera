class Cartera:
    def __init__(self, codigocartera, codigoperiodo, montoperiodo, estadocartera):
        self.codigocartera = codigocartera
        self.codigoperiodo = codigoperiodo
        self.montoperiodo = montoperiodo
        self.estadocartera = estadocartera
        self.fechapago = None
        self.saldo = montoperiodo


    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.codigocartera, self.codigoperiodo, self.montoperiodo, self.saldo, self.estadocartera, self.fechapago)

    def getCodigoCartera(self):
        return self.codigocartera

    def setCodigoCartera(self, codigo):
        self.codigocartera = codigo

    def getCodigoPeriodo(self):
        return self.codigoperiodo

    def setCodigoPeriodo(self, codigo):
        self.codigoperiodo = codigo

    def getMontoPeriodo(self):
        return self.montoperiodo

    def setMontoPeriodo(self, monto):
        self.montoperiodo = monto

    def getEstadoCartera(self):
        return self.estadocartera

    def setEstadoCartera(self, estado):
        self.estadocartera = estado

    def setFechaPago(self, fecha):
        self.fechapago = fecha

    def getFechaPago(self):
        return self.fechapago

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo

class Pagos:
    def __init__(self, codigopago, codigoperiodo, monto):
        self.codigopago = codigopago
        self.codigoperiodo = codigoperiodo
        self.monto = monto
        self.montoperiodo = monto
    
    def __str__(self):
        return '{} {} {} {}'.format(self.codigopago, self.codigoperiodo, self.monto, self.montoperiodo)

    def getCodigoPago(self):
        return self.codigopago

    def setCodigoPago(self, codigo):
        self.codigopago = codigo


    def getCodigoPeriodo(self):
        return self.codigoperiodo

    def setCodigoPeriodo(self, codigo):
        self.codigoperiodo = codigo

    def getMonto(self):
        return self.monto

    def setMonto(self, monto):
        self.monto = monto

    def getMontoPeriodo(self):
        return self.montoperiodo

    def setMontoPeriodo(self, monto):
        self.montoperiodo = monto

c1 = Cartera(12345, 201501, 10000, 'A')
c2 = Cartera(56421, 201502, 20000, 'A')
c3 = Cartera(32345, 201503, 30100, 'A')
c4 = Cartera(12453, 201504, 40300, 'A')
c5 = Cartera(12454, 201505, 40700, 'A')
c6 = Cartera(12455, 201506, 40300, 'A')
c7 = Cartera(12456, 201507, 40500, 'A')
c8 = Cartera(12457, 201508, 40700, 'A')

p1 = Pagos(12345, 201601, 11230)
p2 = Pagos(12545, 201701, 82730)
p3 = Pagos(12645, 201705, 1530)
# create a list of cateras
listaCarteras = [c1, c2, c3, c4, c5, c6, c7, c8]
listaPagos = [p1, p2, p3]

for p in listaPagos:
    for c in listaCarteras:
        if c.getEstadoCartera() == 'A' or c.getEstadoCartera() == 'D':
            if (c.getMontoPeriodo() - p.getMonto()) > 0:
                c.setEstadoCartera('D')
                c.setFechaPago(p.getCodigoPeriodo())
                c.setSaldo(c.getMontoPeriodo() - p.getMonto())
                p.setMonto(0)
                break
            else:
                c.setEstadoCartera('P')
                c.setFechaPago(p.getCodigoPeriodo())
                c.setSaldo(0)
                p.setMonto(p.getMonto() - c.getMontoPeriodo())

# print the list
print('Carteras')
for c in listaCarteras:
    print(c)
print('Pagos')
for p in listaPagos:
    print(p)
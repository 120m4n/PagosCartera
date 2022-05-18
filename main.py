class Cartera:
    def __init__(self, codigocartera, codigoperiodo, montoperiodo, estadocartera):
        self.codigocartera = codigocartera
        self.codigoperiodo = codigoperiodo
        self.montoperiodo = montoperiodo
        self.estadocartera = estadocartera
        self.fechapago = None
        self.saldo = montoperiodo


    def __str__(self):
        return '{:10} {:10} {:10} {:10} {:10} {}'.format(self.codigocartera, self.codigoperiodo, self.montoperiodo, self.saldo, self.estadocartera, self.fechapago)

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
        return '{:10} {:10} {:10} {:10}'.format(self.codigopago, self.codigoperiodo, self.monto, self.montoperiodo)

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


c1 = Cartera(147742, 201612, 2869, 'A')
c2 = Cartera(312884, 201702, 5264, 'A')
c3 = Cartera(147740, 201703, 5308, 'A')
c4 = Cartera(147739, 201704, 7043, 'A')
c5 = Cartera(147733, 201711, 3511, 'A')
c6 = Cartera(147732, 201712, 1064, 'A')
c7 = Cartera(147696, 202012, 3726, 'A')
c8 = Cartera(147695, 202101, 3750, 'A')
c9 = Cartera(147691, 202105, 3563, 'A')


p1 = Pagos(431836, 202112, 32535)






# create a list of cateras
listaCarteras = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
# create a list of pagos
listaPagos = [p1]


for p in listaPagos:
    for c in listaCarteras:
        if (c.getEstadoCartera() == 'A' or c.getEstadoCartera() == 'D'):
            if p.getMonto() > 0:
                if (c.getSaldo() - p.getMonto()) > 0:
                    c.setEstadoCartera('D')
                    c.setFechaPago(p.getCodigoPeriodo())
                    c.setSaldo(c.getSaldo() - p.getMonto())
                    p.setMonto(0)
                    break
                else:
                    c.setEstadoCartera('P')
                    c.setFechaPago(p.getCodigoPeriodo())
                    p.setMonto(p.getMonto() - c.getSaldo())
                    c.setSaldo(0)
            else:
                break
# print the list
print('Carteras')
for c in listaCarteras:
    print(c)

print('Pagos')
print('{:13} {:13} {:13} {:10}'.format(
    'codigopago', 'periodo', 'saldo', 'montoperiodo'))
for p in listaPagos:
    print(p)
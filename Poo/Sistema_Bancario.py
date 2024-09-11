

class Usuario ():
    def __init__(self, nombre,edad,direccion,numeroCuenta,saldoActual):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numeroCuenta = numeroCuenta
        self.saldoActual = saldoActual

    def depositar(self):
        deposito = float(input("¿Que valor desea depositar?"))
        self.saldoActual+=deposito
        print(f"Su saldo actual es de ${self.saldoActual}")
    
    def debitar(self):
        if self.saldoActual<=0:
            print(f"Actualmente su cuenta esta en ceros y por ende no cuenta con los fondos suficientes")
        else:
            retiro = float(input("¿Que valor desea retirar?"))
            if retiro>self.saldoActual:
                print(f"Actualmente no cuenta con los fondos suficientes para el valor que desea retirar")
            else:
                self.saldoActual-=retiro
                print(f"Su saldo actual es de ${self.saldoActual}")
                
    
    def cumpleanos(self):
        self.edad+=1
        print(f"Su edad actual es {self.edad} años")


class Cliente(Usuario):
    def __init__(self, nombre,edad, direccion,numeroCuenta, saldoActual,idCliente,profesion):
        super().__init__(nombre,edad, direccion,numeroCuenta, saldoActual)
        self.idCliente = idCliente
        self.profesion = profesion
        self.prestamoEnCurso = False
    
    def solicitarPrestamo(self):
        self.prestamoEnCurso = True
        print(f"{self.nombre} ha solicitado un prestamo")
    
    def informacionDelUsuario(self):
        print(f"Nombre del cliente: {self.nombre}, Edad: {self.edad}, Direccion: {self.direccion}, Saldo Actual: {self.saldoActual}, Id Cliente: {self.idCliente}, Profesion: {self.profesion} ")


class Empleado(Usuario):
    def __init__(self, nombre,edad, direccion,numeroCuenta, saldoActual,cargo,idEmpleado,sueldo):
        super().__init__(nombre,edad, direccion,numeroCuenta, saldoActual)
        self.idEmpleado = idEmpleado
        self.cargo = cargo
        self.sueldo = sueldo
        self.prestamoEnCurso = False

    def informacionDelEmpleado(self):
        print(f"Nombre del empleado: {self.nombre}, Edad: {self.edad}, Direccion: {self.direccion}, Saldo Actual: {self.saldoActual}, Id empleado: {self.idEmpleado}, Cargo: {self.cargo}, Prestamos: {self.prestamoEnCurso}, Sueldo:{self.sueldo} ")
    

    def adelantarSueldo(self, cantidad):
        if cantidad <= self.sueldo:
            self.sueldo+=cantidad
            self.prestamoEnCurso = True
            print(f"Su saldo actual es de ${self.sueldo}")
        else:
            print(f"No se puede adelantar")

    def pagarNomina(self,prestamo):
        if self.prestamoEnCurso :
            deposito = float(input("Que valor desea depositar: "))
            cantidad =  self.sueldo+deposito
            print(f"Su saldo actual es de ${cantidad-prestamo} Ya que cuenta con un adelanto de {prestamo}")
        else:
            deposito = float(input("Que valor desea depositar: "))
            self.sueldo +=deposito
            print(f"Su saldo actual es de ${self.sueldo}")



usuario1 = Usuario("Juan Manuel", 24,'rosario',33555555,12000)
usuario1.depositar()
usuario1.debitar()
usuario1.cumpleanos()

cliente1 = Cliente("Juan Manuel",24, 'rosario', 324512, 12000,12,'tecnico')
cliente1.solicitarPrestamo()
cliente1.informacionDelUsuario()
cliente1.cumpleanos()

empleado = Empleado("Juan Manuel", 24,'rosario',33555555,12000,'aaaa',14,12000)
empleado.adelantarSueldo(2000)
empleado.informacionDelEmpleado()
empleado.pagarNomina(2000)


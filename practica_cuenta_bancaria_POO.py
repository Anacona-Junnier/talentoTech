class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} \nBalance de la cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro exitoso")
        else:
            print("Fondos insuficientes")

def crear_cliente():
    nombre_cliente = input('Ingrese su nombre: ')
    apellido_cliente = input('Ingrese su apellido: ')
    numero_cuenta= input('Ingrese su número de cuenta: ')
    cliente = Cliente(nombre_cliente, apellido_cliente, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print("Elije: Depositar (D), Retirar (R) o Salir (S)")
        opcion = input()

        if opcion == 'D':
            monto_deposito = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_deposito)
        elif opcion == 'R':
            monto_retiro = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_retiro)
        print(mi_cliente)

    print("Gracias por utilizar el Banco Talento Tech")

inicio()
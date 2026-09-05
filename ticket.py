Nombre = input("Nombre:")
Compra = input("Producto:")
Valor = float(input("Precio:"))
print (f"---Ticket-- \nCliente: {Nombre.strip().title()} \nProducto: {Compra.upper().strip()} \nTotal: {Valor:.2f} \nGracias por tu compra!")
nombre = input("Nombre:")
compra = input("Producto:")
valor = float(input("Precio:"))
print (f"---Ticket-- \nCliente: {nombre.strip().title()} \nProducto: {compra.upper().strip()} \nTotal: {valor:.2f} \nGracias por tu compra!")
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def add_IVA_invoice(subtotal_invoice, applicable_IVA = 21):
    return round(subtotal_invoice + (subtotal_invoice * (applicable_IVA / 100)), 2)

def main():
    while True:
        try:
            subtotal_invoice = float(input('>>> INGRESE EL SUBTOTAL DE LA FACTURA:\n>>> $'))
            if subtotal_invoice >= 0:
                break
            else:
                print('>>> ERROR: EL SUBTOTAL SOLO PUEDE UN CANTIDAD MAYOR O IGUAL QUE CERO')
        except ValueError:
            print('>>> ERROR: POR FAVOR, INGRESE UNA CANTIDAD VÁLIDA COMO SUBTOTAL DE LA FACTURA')

    while True:
        applicable_IVA = input('>>> INGRESE EL PORCENTAJE DE IVA\n>>> ').strip()
        try:
            if applicable_IVA == '':
                applicable_IVA = 21
                break
            if float(applicable_IVA) >= 0:
                applicable_IVA = float(applicable_IVA)
                break
            else:
                print('>>> ERROR: INGRESE UNA CANTIDAD MAYOR O IGUAL A CERO COMO PORCENTAJE DE IVA')
        except ValueError:
            print('>>> ERROR: POR FAVOR, INGRESE UNA CANTIDAD VÁLIDA COMO PORCENTAJE DE IVA')

    total_invoice = add_IVA_invoice(subtotal_invoice, applicable_IVA)
    print(f'>>> TOTAL ${total_invoice}')

if __name__ == '__main__':
    main()

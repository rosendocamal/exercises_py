# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

while True:
    mail = input('>>> INGRESE SU CORREO ELECTRÓNICO:\n>>> ')
    if bool(mail) and len(mail) >= 5 and mail.rfind('@', 1) >= 1 and mail.count('@') == 1:
        break
    else:
        print('>>> INTRODUZCA UNA DIRECCIÓN ELECTRÓNICA VÁLIDA')

rmail = f'>>> {mail[:mail.index("@")]}@ceu.es'

print(rmail)

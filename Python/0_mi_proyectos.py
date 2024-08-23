### Practir lo apredido.

### crear Login.
dic_data = {
    "jpineda": {"password": "1010", "user": "Juan Francisco"},
    "user2": {"password": "2020", "user": "pedro"},
    "admin": {"password": "3030", "user": "loe"}
}

## Ingreso de User y Password
log: str = "Login System"
print(log.center(20, '.'))
user: str = input("Ingrese su Usuario: ")
passw: int = input("Ingrese Password: ")

# Validar usuario y password ingresado
if user in dic_data:
    if dic_data[user]["password"] == passw:
        print("Bienvenido:", dic_data[user]["user"])
    else:
        print("Password Incorrecto")
else:
    print("Usuario no existe")

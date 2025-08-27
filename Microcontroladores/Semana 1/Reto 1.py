def grasa_corporal_general(peso, altura, edad, sexo):

    imc = peso / (altura ** 2)
    
    if sexo.lower() == "hombre":
        return 1.20 * imc + 0.23 * edad - 16.2
    elif sexo.lower() == "mujer":
        return 1.20 * imc + 0.23 * edad - 5.4
    else:
        raise ValueError("Sexo inválido. Use 'hombre' o 'mujer'.")

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
edad = int(input("Edad: "))
sexo = input("Sexo (hombre/mujer): ").strip().lower()

resultado = grasa_corporal_general(peso, altura, edad, sexo)
print(f"Porcentaje de grasa corporal aproximado: {resultado:.2f}%")

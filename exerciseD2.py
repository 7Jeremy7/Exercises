with open('colaboradores.txt', 'r+') as archivo:
    content = [line.strip() for line in archivo.readlines()]

def fivemembers(members=None):
    if members is None:
        members = content

    numb_colab = input("Ingrese un número de colaboradores: ")

    if numb_colab.isdigit():
        response = int(numb_colab)
        if response <= len(members):
            for memb in members[:response]:
                print(f"- {memb}")
        else:
            print(f"Solo hay {len(members)} colaboradores disponibles.")
    else:
        print("No ingresaste un número válido. Mostrando algunos nombres de la lista:")
        for memb in members[:5]:
            print(f"- {memb}")

    while len(members) < 15:
        agregar_mas = input("¿Deseas agregar un nuevo colaborador? (si/no): ").strip().lower()
        if agregar_mas == 'si':
            insert_colab = input("Ingrese nuevo colaborador: ")
            members.append(insert_colab)
            with open('colaboradores.txt', 'a') as archivo:
                archivo.write(f"{insert_colab}\n")

            print("Lista de colaboradores actualizada:")
            for memb in members:
                print(f"- {memb}")
        elif agregar_mas == 'no':
            break
        else:
            print("Por favor, ingrese 'si' para sí o 'no' para no.")
    
    if len(members) >= 15:
        print("No puedes agregar más de 15 colaboradores.")








    

if __name__ == "__main__":
    fivemembers()
    
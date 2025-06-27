import json
import asyncio
import os

PATIENTS_FILE = 'patients.json'


def load_patients():
    """Carga los registros de pacientes desde un archivo JSON."""
    if os.path.exists(PATIENTS_FILE):
        with open(PATIENTS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_patients(patient_list):
    """Guarda los registros de pacientes en un archivo JSON."""
    with open(PATIENTS_FILE, 'w') as file:
        json.dump(patient_list, file)


async def save_patients_async(patient_list):
    """Guarda los registros de pacientes de forma asíncrona."""
    await asyncio.sleep(1)  # Simula una operación de I/O
    save_patients(patient_list)


def add_patient(patient_list, patient):
    """Agrega un nuevo paciente a la lista."""
    patient_list.append(patient)


def update_patient(patient_list, patient_id, new_info):
    """Actualiza la información de un paciente existente."""
    return [new_info if patient['id'] == patient_id else patient for patient in patient_list]


def delete_patient(patient_list, patient_id):
    """Elimina un paciente por su ID."""
    return [patient for patient in patient_list if patient['id'] != patient_id]


def display_patients(patient_list):
    """Muestra todos los registros de pacientes."""
    for patient in patient_list:
        print(
            f"ID: {patient['id']} - Nombre: {patient['name']} - Edad: {patient['age']} - Diagnóstico: {patient['diagnosis']}")


async def main():
    patients = load_patients()

    while True:
        print("\nGestor de Pacientes")
        print("1. Ver pacientes")
        print("2. Añadir paciente")
        print("3. Actualizar paciente")
        print("4. Eliminar paciente")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            display_patients(patients)
        elif choice == '2':
            name = input("Escribe el nombre del paciente: ")
            age = int(input("Escribe la edad del paciente: "))
            diagnosis = input("Escribe el diagnóstico: ")
            add_patient(patients, {'id': len(patients) + 1, 'name': name, 'age': age, 'diagnosis': diagnosis})
            await save_patients_async(patients)
            print("Paciente añadido.")
        elif choice == '3':
            patient_id = int(input("Escribe el ID del paciente a actualizar: "))
            name = input("Escribe el nuevo nombre: ")
            age = int(input("Escribe la nueva edad: "))
            diagnosis = input("Escribe el nuevo diagnóstico: ")
            patients = update_patient(patients, patient_id,
                                      {'id': patient_id, 'name': name, 'age': age, 'diagnosis': diagnosis})
            await save_patients_async(patients)
            print("Paciente actualizado.")
        elif choice == '4':
            patient_id = int(input("Escribe el ID del paciente a eliminar: "))
            patients = delete_patient(patients, patient_id)
            await save_patients_async(patients)
            print("Paciente eliminado.")
        elif choice == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    asyncio.run(main())

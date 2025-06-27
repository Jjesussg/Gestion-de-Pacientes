# Gestion-de-Pacientes
Proyecto Final de Lenguaje

---
Este proyecto crea un .exe para la gestión de pacientes en un hospital 
---

▎Informe sobre el uso de los paradigmas de programación en el código 

▎ Programación imperativa

El código sigue principalmente el paradigma imperativo, donde se especifican las instrucciones paso a paso para manipular el estado del programa. Por ejemplo, las funciones add_patient, update_patient y delete_patient modifican explícitamente la lista de pacientes mediante operaciones como añadir, actualizar o eliminar elementos.

▎ Programación funcional

Se observa cierto uso del paradigma funcional en funciones como update_patient y delete_patient, donde se utilizan expresiones basadas en comprensión de listas para crear nuevas listas sin modificar las originales directamente. Esto promueve la inmutabilidad y evita efectos secundarios

▎ Programación asíncrona

El código incorpora programación asíncrona con asyncio para simular operaciones de entrada/salida (I/O) no bloqueantes al guardar los datos en disco. La función save_patients_async utiliza async def y await asyncio.sleep(1) para simular una operación que podría tardar tiempo, permitiendo que el programa pueda realizar otras tareas mientras espera:


Esto es útil para mejorar la eficiencia y la capacidad de respuesta en aplicaciones más complejas o con operaciones I/O reales.

---

▎Requisitos técnicos para ejecutar la aplicación

• Python 3.7 o superior:  
  Se requiere una versión moderna de Python que soporte la sintaxis async/await usada para la programación asíncrona.

• Módulos estándar:  
  La aplicación solo utiliza módulos estándar (json, asyncio, os), por lo que no es necesario instalar paquetes externos.

• Permisos de lectura/escritura:  
  El programa lee y escribe en un archivo local llamado  patients.json. Se necesita permiso para crear y modificar este archivo en el directorio donde se ejecute el script.

• Entorno de consola:  
  La interacción con el usuario se realiza vía consola (terminal), por lo que debe ejecutarse en un entorno que permita entrada y salida estándar.


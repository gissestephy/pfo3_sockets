# Sistema Cliente-Servidor con Sockets en Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Arquitectura-Cliente--Servidor-blue?style=for-the-badge" alt="Cliente servidor">
  <img src="https://img.shields.io/badge/Comunicación-TCP%20Sockets-green?style=for-the-badge" alt="TCP Sockets">
  <img src="https://img.shields.io/badge/Concurrencia-Threading-orange?style=for-the-badge" alt="Threading">
</p>

## 📌 Descripción

**Store Market** es un proyecto académico desarrollado en Python que implementa una arquitectura distribuida de tipo **Cliente - Servidor**, utilizando sockets TCP para establecer la comunicación entre ambos componentes.

El sistema permite que un cliente envíe diferentes solicitudes a un servidor, que recibe las tareas, las incorpora a una cola y las distribuye entre distintos Workers para su procesamiento concurrente.

El objetivo principal es aplicar conceptos de programación sobre redes, comunicación mediante sockets, concurrencia y distribución de tareas.

## 🎯 Funcionalidades

- 🔌 Comunicación entre cliente y servidor mediante sockets TCP.
- 📥 Recepción de tareas desde el cliente.
- 📋 Administración de tareas mediante una cola.
- ⚙️ Procesamiento concurrente utilizando hilos (*Threads*).
- 👷 Dos Workers independientes para procesar las solicitudes.
- 📤 Envío de resultados desde el servidor hacia el cliente.
- 🛒 Menú interactivo de Store Market.

### 📋 Actividades disponibles

| Opción | Actividad |
|:---:|---|
| 1 | Registrar usuario |
| 2 | Consultar información |
| 3 | Actualizar registro |
| 4 | Eliminar registro |
| 5 | Generar reporte |
| 6 | Salir |

## 🛠️ Tecnologías utilizadas

| Tecnología | Descripción |
|---|---|
| Python | Lenguaje de programación |
| Socket | Comunicación mediante TCP |
| Threading | Ejecución concurrente de tareas |
| Queue | Cola para administrar solicitudes |
| JSON | Intercambio de información |
| Time | Simulación del tiempo de procesamiento |

**Nota:** El proyecto utiliza módulos incluidos en la biblioteca estándar de Python. No requiere instalar dependencias externas.

## 📁 Estructura del proyecto

```text
pf03_sockets/
│
├── servidor.py    # Servidor TCP y administración de Workers
├── cliente.py     # Cliente interactivo que envía solicitudes
│
└── README.md      # Documentación del proyecto
```

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, necesitás tener instalado:

- [Python 3](https://www.python.org/downloads/) (versión 3.10 o superior).
- [Visual Studio Code](https://code.visualstudio.com/) (opcional).
- [Git](https://git-scm.com/downloads/).

Para verificar que Python esté instalado, ejecutá:

```bash
python --version
```

Para verificar Git:

```bash
git --version
```

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

Abrí una terminal y ejecutá:

```bash
git clone https://github.com/gissestephy/pfo3_sockets.git
```

Ingresá a la carpeta del proyecto:

```bash
cd pfo3_sockets
```

### 2. Iniciar el servidor

Abrí una primera terminal y ejecutá:

```bash
python servidor.py
```

El servidor quedará escuchando conexiones en:

```text
127.0.0.1:5000
```

Se iniciarán automáticamente los dos Workers, que permanecerán disponibles para recibir y procesar tareas.

### 3. Iniciar el cliente

Abrí una segunda terminal, dentro de la misma carpeta del proyecto, y ejecutá:

```bash
python cliente.py
```

El cliente establecerá una conexión con el servidor y mostrará el menú interactivo de Store Market.

### 4. Interactuar con el sistema

Seleccioná el número de la actividad que deseás realizar.

El cliente enviará la solicitud al servidor, uno de los Workers procesará la tarea y el resultado será devuelto al cliente.

Para finalizar la ejecución, seleccioná la opción **6. Salir**.

## 🔄 Flujo de funcionamiento

```text
        CLIENTE
           |
           | Solicitud TCP
           v
        SERVIDOR
           |
           v
       COLA DE TAREAS
           |
       +---+---+
       |       |
       v       v
    WORKER 1  WORKER 2
       |       |
       +---+---+
           |
           v
     RESULTADO
           |
           v
        CLIENTE
```

## 🧠 Conceptos aplicados

- **Arquitectura Cliente-Servidor:** separación entre el componente que solicita operaciones y el que las procesa.
- **Sockets TCP:** comunicación entre procesos mediante una conexión de red.
- **Multithreading:** ejecución de múltiples hilos de trabajo.
- **Cola de tareas:** organización de las solicitudes pendientes de procesamiento.
- **Concurrencia:** posibilidad de procesar distintas tareas utilizando Workers independientes.
- **Intercambio de datos:** serialización y deserialización de mensajes mediante JSON.

## 👩‍💻 Gisela Stephanie Colmeiro

Proyecto desarrollado como parte de la práctica académica de **Programación sobre Redes**.

---

<p align="center">
  💻 Desarrollado con Python | 🛒 Store Market
</p>

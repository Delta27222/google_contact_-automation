# **Automatización de Gestión de Contactos y Creación de Grupos en WhatsApp**

Este proyecto tiene como objetivo automatizar el proceso de carga de datos de usuario en **Google Contacts** y la creación de **grupos de WhatsApp** mediante un flujo completamente automatizado. La solución se divide en dos componentes principales:

## **Componentes Principales:**

### **1. Carga de Datos a Google Contacts:**
- **Importación de datos desde archivos Excel (XLSX):** Permite cargar un conjunto de datos de usuarios desde un archivo Excel estructurado. Los usuarios pueden incluirse automáticamente en Google Contacts.

- **Integración con la API de Google Contacts:** La API se encarga de mapear correctamente los campos como nombre, correo electrónico, teléfono, etc., y crea nuevos contactos rápidamente.


### **2. Automatización de Creación de Grupos en WhatsApp:**
- **Uso de Selenium:** Se utiliza Selenium para automatizar el flujo de creación de grupos en WhatsApp Web. El script navega por WhatsApp Web y realiza las acciones necesarias para crear grupos.

- **Criterios de Segmentación:** Los grupos de WhatsApp se generan en función del identificador único asignado a cada usuario durante su creación y subida a Google Contacts.


- **Flujo Automatizado:** Selenium se encarga de:
  1. Iniciar sesión en WhatsApp Web.
  2. Buscar los contactos utilizando las identificaciones asignadas.
  3. Crear el gruepo de WhatsApp y agrega los contactos de manera automática.

## **Tecnologías Utilizadas:**

- **API de Google Contacts:** Para la gestión e importación de contactos a Google.

- **API de WhatsApp (o herramientas de automatización):** Para crear y administrar grupos en WhatsApp de manera automática.

- **Selenium:** Utilizado para automatizar el flujo de creación de grupos en WhatsApp Web.

- **Lenguajes y Frameworks:** Python, Node.js, o cualquier otro lenguaje compatible con las APIs mencionadas.

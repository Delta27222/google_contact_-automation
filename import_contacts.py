import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/contacts']

def get_service():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('people', 'v1', credentials=creds)

def read_excel(file_path, required_columns):
    df = pd.read_excel(file_path)
    print("Verificando columnas requeridas...")
    print(f"Columnas encontradas en el archivo: {df.columns.tolist()}")

    obligatorias = ['Nombre', 'Tel', 'Correo']
    faltantes = [col for col in obligatorias if col not in df.columns]
    if faltantes:
        raise Exception(f"El archivo Excel debe tener al menos las columnas: {', '.join(obligatorias)}. Faltan: {', '.join(faltantes)}")

    adicionales_faltantes = [col for col in required_columns if col not in df.columns]
    if adicionales_faltantes:
        print(f"⚠️  Advertencia: Las siguientes columnas requeridas personalizadas no se encontraron: {adicionales_faltantes}")

    return df

def create_contact(service, nombre, apellido, telefono, correo, carrera=None, etiqueta_resource=None):
    contact_body = {
        "names": [{"givenName": nombre, "familyName": apellido if apellido else ""}],
        "emailAddresses": [{"value": correo}],
        "phoneNumbers": [{"value": telefono}],
        "memberships": [{"contactGroupMembership": {"contactGroupResourceName": etiqueta_resource}}] if etiqueta_resource else [],
    }

    # Agregar carrera como parte de la biografía
    if carrera:
        contact_body["biographies"] = [{"value": f"Carrera: {carrera}"}]

    service.people().createContact(body=contact_body).execute()

def get_or_create_label(service, etiqueta_nombre):
    groups = service.contactGroups().list(pageSize=200).execute().get('contactGroups', [])
    for group in groups:
        if group['name'].lower() == etiqueta_nombre.lower():
            return group['resourceName']
    new_group = service.contactGroups().create(body={"contactGroup": {"name": etiqueta_nombre}}).execute()
    return new_group['resourceName']

def importar_contactos(excel_path, required_columns=None, etiqueta='ImportadosDesdeExcel'):
    print("Autenticando con Google...")
    service = get_service()

    required_columns = required_columns or []

    print("Leyendo Excel...")
    df = read_excel(excel_path, required_columns)

    print("Creando/obteniendo etiqueta...")
    etiqueta_resource = get_or_create_label(service, etiqueta)

    for i, row in df.iterrows():
        print(f"📡 Agregando contacto {row['Nombre']} {row.get('Apellido', '')}...")
        create_contact(
            service,
            etiqueta+ ' - '+row['Nombre'],
            row.get('Apellido', ''),
            str(row['Tel']),
            row['Correo'],
            row.get('Carrera', None),
            etiqueta_resource
        )

    print("✅ Todos los contactos fueron importados correctamente.")

# USO:
if __name__ == "__main__":
    columnas_deseadas = ['Nombre', 'Tel', 'Correo', 'Apellido', 'Carrera']  # Añade lo que necesites

    importar_contactos('contactos.xlsx', columnas_deseadas, 'CINU_12025')

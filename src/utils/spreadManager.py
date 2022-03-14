import os
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

#Cambiamos directorio de trabajo al directorio del archivo para poder abrir el .json de credenciales
fileDir = os.path.dirname(os.path.realpath(__file__))
os.chdir(fileDir)

"""
Atributos:
- scope: APIs a usar (Google SpreadSheets y Drive)
- spreadsheet: Nombre del Libro de Calculo 
- spreadsheet_id: Identificador de nuestro Libro de Calculo
- validationSheet: Nombre de la Hoja a modificar (hoja de validacion)
- creds: Credenciales de la cuenta
- client: Conexion a la Hoja de Calculo
"""
class spreadManager:

    def __init__(self,spreadsheet, spreadsheetId, validationSheet):

        self.scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.spreadsheet = spreadsheet
        self.spreadsheetId = spreadsheetId
        self.validationSheet = validationSheet
        
        if os.path.exists('credentials.json'):
            self.creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', self.scope)
            service = build("sheets","v4",credentials=self.creds, cache_discovery=False)
            self.client = service.spreadsheets()
        else:
            print("DB ERROR > Missing Credentials for accessing")
            exit()

    def insertRow(self, row):
        """
        Funcion auxiliar que inserta una nueva fila en la Hoja de Validacion
        """
        values = (
            self.client.values()
            .append(
                spreadsheetId=self.spreadsheetId,
                range=f"{self.validationSheet}!A:D",
                body=dict(values=row),
                valueInputOption="USER_ENTERED",
            )
            .execute()
        )
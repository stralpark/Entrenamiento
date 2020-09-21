import configparser

configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome' : 'C:\DriverChrome\chromedriver.exe'}
configuracion['Paginas'] = {'page' : 'https://www.steren.com.mx/cables/cables-de-red'}

with open('Configuracion.ini', 'w') as archivoconfig:
	configuracion.write(archivoconfig)
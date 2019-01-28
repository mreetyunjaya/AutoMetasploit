class Config:
    APP_NAME = 'AutoMetasploit'
    CREADOR = 'ConnorXploit'
    TITULO = 'Herramienta automatica de escaneos'
    CONTINUAR = 'Continuar'
    SELECCIONA = 'Selecciona una opción'
    SALIR = 'Saliendo de AutoMetasploit...'
    MODULO_FUNCION = {'interfaces':'elegirInterfaz', 'nmap':'elegirParametrosNmap'}
    
class ConfigInterfaces:
    PARAMETROS_OBLIGATORIOS = True

class ConfigNmap:
    PARAMETROS_OBLIGATORIOS = True
    PARAMETROS = {
		'-O':'Sistema Operativo', 
		'-A': 'All', 
		'-sV':'Version de Protocolos'
	}

class ConfigErrores:
    ERROR = 'ERROR'
    NO_CONTROLADO = 'No controlado'
    SELEC_INC = 'Seleccion incorrecta'
    PARAMETRO_OBLIGATORIO = 'Debes seleccionar al menos una opcion del menu'
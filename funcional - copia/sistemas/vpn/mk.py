""" AUTENTICACION A ESCRITORIOS REMOTOS A TRAVES DEL PROTOCOLO SSH """

import paramiko
import time

HOST = ''
PORT ='22'
USER = ''
PASS= ''
""" datos =dict(hostname=HOST, port=PORT, username=USER)"""

if __name__ == '__main__':
    # try:
    client = paramiko.SSHClient()
    
            
    
    client.connect(HOST, PORT, USER, PASS, banner_timeout=200)
            
    stdin, stdout, stderr = client.exec_command("ppp secret add name=\"" + {{Usuario.nombre }} +"\" password=\"" + {{Usuario.contraseña }} +"\" profile=OVPN service=ovpn")
            
    time.sleep(1)
            
    result = stdout.read().decode()
    # except paramiko.ssh_exception.AuthenticationException as e:
    #     print('Autenticacion fallida')
    #export file=flash/prueba_export.backup to=C:\rmikrotik
    print(result)
    
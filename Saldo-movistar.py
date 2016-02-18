#!/usr/bin/fades
# Script para consulta de Saldo de Movistar

################
# Dependencias #
################
# Fades - Se instala con "pip3 install fades"
# PhantomJS  - "apt-get install phanthomjs -y"

from selenium import webdriver # fades.pypi
import sys

try:
    username=sys.argv[1]
    password=sys.argv[2]
except IndexError:
    print ("Imposible continuar, debe ingresar usuario y contraseña")
    sys.exit()

try:
    driver= webdriver.PhantomJS()
    driver.get('https://www.movistar.com.ar/micuenta')
    usuario= driver.find_element_by_id('userNamesmall')
    usuario.send_keys(username)
    contraseña= driver.find_element_by_id('password-clear')
    contraseña.send_keys(password)
    submit=driver.find_element_by_css_selector('.btn-violeta')
    #Envio click para avanzar (algunas veces falló por eso esta este try)
    submit.click()
except:
    print ("Falla al querer ingresar a la web, por favor, intente nuevamente en unos minutos")
    sys.exit()

saldo=driver.find_element_by_id('balance')
print (saldo.text)
driver.close()

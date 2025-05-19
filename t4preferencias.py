#Importar
from nicegui import ui
#mostrar
def mostrar():
 #seleccionar el color seleccionado por medio de lsta desplegable
 ui.notify(f'Color: {color.value}, Tema oscuro: {tema.value}')
color = ui.select(['Rojo', 'Verde', 'Azul'], label='Color favorito')
#Seleccionar el tema oscuro por medio de un switch
tema = ui.switch('Tema oscuro')
#Guardar los cambios
ui.button('Guardar preferencias', on_click=mostrar)
ui.run()
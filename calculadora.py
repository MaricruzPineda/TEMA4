from nicegui import ui

#Título
ui.label('Calculadora de suma simple')

#Entrada de datos
num1=ui.number(label='  Número 1', value=0)
num2=ui.number(label='  Número 2', value=0)

#Resultado
resultado= ui.label('Resultado: 0').classes('text-h6')

#Botón suma
def suma():
    suma=num1.value+num2.value
    resultado.text =f'Resultado:{suma}'
    ui.notify(f'La suma es: {suma}')


def resta():
    resta=num1.value-num2.value
    resultado.text =f'Resultado:{resta}'
    ui.notify(f'La resta es: {resta}')

def multi():
    multi=num1.value*num2.value
    resultado.text =f'Resultado:{multi}'
    ui.notify(f'La multiplicación es: {multi}')

def division():
    division=num1.value/num2.value
    resultado.text =f'Resultado:{division}'
    ui.notify(f'La división es: {division}')

with ui.row():
    ui.button('Sumar', on_click=suma)
    ui.button('Restar', on_click=resta)
    ui.button('Multiplicar', on_click=multi)
    ui.button('Dividir', on_click=division)

#Ejecutar la app
ui.run()
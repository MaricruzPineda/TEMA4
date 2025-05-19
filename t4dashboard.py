from nicegui import ui
#por filas se organizan tarjetas
with ui.row():
	with ui.card():
		#Primer tarjeta
		ui.label('Ventas')
		ui.label('💰$1,200')
	with ui.card():
		#Segunda tarjeta
		ui.label('Usuarios')
		ui.label('👤 342')
	with ui.card():
		#Tercera tarjeta
		ui.label('Tickets')
		ui.label('🎫18')
ui.run()
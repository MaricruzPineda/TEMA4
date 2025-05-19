from nicegui import ui
# nombre del audio local en tu proyecto
AUDIO_URL = 'intro.mp3'
ui.label(' Reproductor de audio')
# Control de audio
audio = ui.audio(AUDIO_URL, autoplay=False, controls=True)
# Botones para controlar manualmente desde Python
with ui.row():
	ui.button('Reproducir', on_click=lambda: audio.run_method('play'))
	ui.button('Pausar', on_click=lambda: audio.run_method('pause'))
ui.run()
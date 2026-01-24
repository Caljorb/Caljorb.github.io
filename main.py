from nicegui import ui

'''
TODO:
  1. make bg img (pixel art rainbow bunnies in space?)
  2. idkkkkkk
'''

dark = True

def root():
  ui.dark_mode(dark)
  #ui.colors(primary='#1aae77', dark='#1d1d1d', secondary='#1d1d1d')
  ui.colors(primary="#3B3B3B")

  with ui.row().classes('w-full justify-between'):
    with ui.card().classes('shadow-lg'):
      with ui.row().mark('a'):
        ui.link(text='About').style('color: #ffffff; font-size: 125%;')
        ui.link(text='Posts').style('color: #ffffff; font-size: 125%;')
        ui.link(text='Random').style('color: #ffffff; font-size: 125%;')
    ui.button(icon='brightness_medium', on_click=lambda: dark_mode()).props('flat round')
  ui.separator()
  with ui.row().classes('w-full justify-center'):
    ui.label('Hello').style('font-size: 200%;')
  with ui.row().classes('w-full justify-center'):
    with ui.card(align_items='center').classes('w-1/2 h-1/2'):
      #ui.image('./img/space.png').style('max-width: 50%; max-width: 50%;')
      ui.interactive_image('./img/space.png')#.style('max-width: 50%; max-width: 50%;')


def dark_mode():
  global dark
  dark = not dark
  color = '#ffffff' if dark else '#000000'
  ui.query('a').style(f'color: {color}')
  ui.dark_mode(dark)

  

ui.run(root)
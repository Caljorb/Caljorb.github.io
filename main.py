from nicegui import ui
import random as rand

dark = True
def menu():
  # TODO: add favicon <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
  ui.add_head_html('''
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@100..900&display=swap" rel="stylesheet">
    <style>
    @font-face {
      font-family: "League Spartan", sans-serif;
      font-optical-sizing: auto;
      font-weight: <weight>;
      font-style: normal;
    }
    </style>
  ''')
  ui.dark_mode(dark)
  color = '#ffffff' if dark else '#000000'
  #ui.colors(primary='#1aae77', dark='#1d1d1d', secondary='#1d1d1d')
  ui.colors(primary="#3B3B3B")

  with ui.row().classes('w-full justify-between'):
    with ui.card().classes('shadow-lg'):
      with ui.row():
        ui.link(text='Home', target=root).classes('menu')
        ui.link(text='About', target=about).classes('menu')
        ui.link(text='Posts', target=posts).classes('menu')
        ui.link(text='Random', target=random).classes('menu')
    ui.button(icon='brightness_medium', on_click=lambda: dark_mode()).props('flat round')
  ui.separator()
  ui.query('.menu').style(f'color: {color}; font-size: 125%; font-family: League Spartan;')

def dark_mode():
  global dark
  dark = not dark
  color = '#ffffff' if dark else '#000000'
  ui.query('.menu').style(f'color: {color}')
  ui.query('.post').style(f'color: {color}')
  ui.query('.text').style(f'color: {color}')
  ui.query('.random').style(f'color: {color}')
  ui.dark_mode(dark)

@ui.page('/')
def root():
  menu()
  with ui.row().classes('w-full justify-center'):
    ui.label('The Future is Now!').style('font-size: 200%; font-family: League Spartan;')
  with ui.row().classes('w-full justify-center'):
    with ui.card(align_items='center').classes('w-1/2 h-1/2'):
      ui.interactive_image('./img/space.png')

@ui.page('/about')
def about():
  menu()
  with ui.row(wrap=False).classes('w-3/4 justify-around'):
    ui.interactive_image('./img/bunnrydfebu.png').classes('border-2 border-solid').props('round')
    ui.html('''
      Welcome to my site! This is home to my ramblings on whatever I am interested in at the time. <br><br>
      <strong>Please note that any work/opinions produced on this site are reflective of my own ideas and may not
      pertain to those of any employer.</strong>
    ''', sanitize=False).style('font-size: 150%; font-family: League Spartan;')

@ui.page('/random')
def random():
  menu()
  color = '#ffffff' if dark else '#000000'
  with ui.row().classes('w-full justify-center'):
    ui.label('Random Links').style(f'font-family: League Spartan; font-size: 250%; font-weight: bold; text-decoration-line: underline;')
  with ui.row().classes('w-full justify-center'):
    with ui.grid(columns=2):
      with ui.card().classes('items-center shadow-lg'):
        ui.link(text='Quotes', target=quotes).classes('random')
      
      with ui.card().classes('items-center shadow-lg'):
        ui.link(text='Drawings', target=drawings).classes('random')

  ui.query('.random').style(f'color: {color}; font-size: 125%; font-family: League Spartan;')

@ui.page('/quotes')
def quotes():
  menu()
  # TODO: get more quotes
  quote_list = [
    'It\'s a terrible day for rain',
    'See you next time',
  ]

  # TODO: check i can do this with jsut a standard label
  class quote_label(ui.label):
    def _handle_text_change(self, text: str) -> None:
        super()._handle_text_change(text)
  model = {'quote': rand.choice(quote_list)}
  with ui.row().classes('w-full justify-center'):
    with ui.card().classes('items-center shadow-lg'):
      quote_label().bind_text_from(model, 'quote').style('font-size: 125%; font-family: League Spartan;')
  with ui.row().classes('w-full justify-center'):
    ui.button(text='New Quote', on_click=lambda: model.update(quote=rand.choice(quote_list)))

@ui.page('/drawings')
def drawings():
  menu()
    
### POSTS ###

@ui.page('/posts')
def posts():
  menu()
  color = '#ffffff' if dark else '#000000'
  # TODO: add bg for posts
  with ui.row().classes('w-full justify-center'):
    add_post('1-24-2026', 'First Post', 'first_post')
  ui.query('.post').style(f'font-family: League Spartan; font-size: 150%; color: {color};')

def add_post(date, title, dst):
  with ui.row():
    ui.label(date).classes('post')
    ui.link(title, target=f'/posts/{dst}').classes('post')

# TODO: is there a better way of doing posts? I don't think making a method for each is a good idea...
@ui.page('/posts/first_post')
def first_post():
  menu()
  color = '#ffffff' if dark else '#000000'
  with ui.row().classes('ml-100 mr-100'):
      ui.label('Welcome to my site').style(f'font-family: League Spartan; font-size: 250%; font-weight: bold; text-decoration-line: underline;')
      ui.label('I\'m not entirely sure what I\'ll be using it for yet, but I plan on sharing my progress on personal projects and whatever else comes to mind. Thanks for checking it out!').style('font-family: League Spartan; font-size: 150%;')


ui.run(root)

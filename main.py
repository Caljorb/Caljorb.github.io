from nicegui import ui

'''
TODO:
  1. make bg img (pixel art rainbow bunnies in space?)
  2. idkkkkkk
'''

dark = True

def menu():
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
  ui.label('Under construction').style('font-size: 150%; font-family: League Spartan;')

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
  with ui.row().classes('w-1/2 justify-center'):
    ui.html('''
            <h2>First Post</h2>
            <p>This is a test for my first post</p>
            ''', sanitize=False).classes('text')
  ui.query('.text').style(f'font-family: League Spartan; color: {color};')
  ui.query('p').style('font-size: 150%;')


ui.run(root)
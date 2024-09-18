import webview
import webview.menu as wm
def click_me():
    active_window = webview.active_window()
    if active_window:
        active_window.load_html('<h1>You clicked me!</h1>')

menu_items = [
    wm.Menu(
        'Test Menu',
        [
            wm.MenuAction('Change Active Window Content', click_me),
            wm.MenuSeparator(),
            wm.Menu(
                'Random',
                [
                    wm.MenuAction('Click Me', click_me),
                    wm.MenuAction('File Dialog', click_me),
                ],
            ),
        ],
    ),
    wm.Menu('Nothing Here', [wm.MenuAction('This will do nothing', click_me)]),
]

columns = 4
rows = 1
screen_choice = 0
padding = 25

urls = [
    'https://spelling-bee-free.pages.dev/',
    'https://www.nytimes.com/games/strands',
    'https://www.nytimes.com/games/wordle/index.html',
    'https://spelling-bee-free.pages.dev/',
]

if len(webview.screens) > screen_choice:
    screen = webview.screens[screen_choice]
else:
    screen = webview.screens[0]

window_width = int(screen.width / columns) - (padding * columns)
window_height = int(screen.height / rows) - (padding * (rows+1)) - 50 - 150


windows = []
# Tile the windows
window_x = padding
window_y = padding

url_index = 0
for c in range(columns):
    if c > 0:
        window_x += window_width + (padding*2)
    else:
        window_x = padding

    for r in range(rows):
        if r == 0:
            window_y = padding
        else:
            window_y += window_height + (padding*2)
        url_index = len(windows)
        url = urls[url_index]
        window = webview.create_window(f"Window {c}|{r}", url, 
                                       width=window_width, height=window_height, x=window_x, y=window_y, screen=screen,
                                       frameless=True, easy_drag=True,shadow=False, zoomable=True)
        windows.append(window)

webview.start(menu=menu_items)

# # Create four windows that are tiled and take up the whole screen
# windows = []
# for i in range(4):
#     window = webview.create_window("Window {}".format(i), "https://example.com")
#     windows.append(window)

# # Tile the windows
# window_width = 1024
# window_height = 768
# for i, window in enumerate(windows):
#     x = (i % 2) * window_width
#     y = (i // 2) * window_height
#     window.move(x, y)
#     window.resize(window_width, window_height)

# webview.start()
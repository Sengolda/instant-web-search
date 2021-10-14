# Built using vscode-ext

import sys
import vscode
import webbrowser

ext = vscode.Extension(
    name="instant-web-search",
    display_name="instant-web-search",
    version="0.1.0",
    description="Search the web in ur vscode!",
    publisher="Sengolda",
)


@ext.command(name="searchweb")
def _searchweb():
    opts = vscode.ext.InputBoxOptions(title="What would you like to search for?")
    result1 = vscode.window.show_input_box(opts)
    opts2 = vscode.ext.InputBoxOptions(
        title="What Search engine do you wanna use? (duckduckgo, google)"
    )
    result2 = vscode.window.show_input_box(opts2)
    if result2 == "duckduckgo":
        to_open_url = "https://duckduckgo.com/?q={}".format(result1.replace(" ", "+"))
    elif result2 == "google":
        to_open_url = "https://www.google.com/search?q={}".format(
            result1.replace(" ", "+")
        )

    webbrowser.open_new_tab(to_open_url)




def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()

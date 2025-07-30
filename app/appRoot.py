from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

def appFunc():
    class AppClass(App):

        def compose(self) -> ComposeResult:

            yield Header()
            yield Footer()

    if __name__ == "__appRoot__":
        app = AppClass()
        app.run
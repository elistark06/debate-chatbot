from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static, Input
from textual.containers import Horizontal, VerticalScroll


class TestApp(App):
    CSS_PATH= "app.tcss"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield VerticalScroll(
            Horizontal(
                Static("Welcome To The Debatebot App! Scroll To Interact", classes="header"),
            ),
            Horizontal(
                Horizontal(
                    Input(placeholder="An integer", type="integer")
                ),
                Horizontal(
                    Input(placeholder="An integer", type="integer")
                ),    
                classes="mainGrid",
            ),
        )
        yield Footer()
 
if __name__ == "__main__":
    app = TestApp()
    app.run()
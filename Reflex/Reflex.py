"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import Reflex as rx

class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="red",
            border_radius="1em"
        ),
        rx.heading(State.count, font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="green",
            border_radius="1em"
        ),
    )

app = rx.App()
app.add_page(index)
app.compile()

"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from luxtron.pages.home import create as home_page
from luxtron.pages.products import create as products_page
from luxtron.pages.contact import create as contact_page

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

# def index() -> rx.Component:
#     # Welcome Page (Index)
#     return rx.fragment(
#         rx.el.style(
#             """
#         @font-face {
#             font-family: 'LucideIcons';
#             src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
#         }
#     """
#         ),
#         home_page()
#     )

# def index() -> rx.Component:
    # return rx.container(
    #     rx.color_mode.button(position="top-right"),
    #     rx.vstack(
    #         rx.heading("Welcome to Luxtron!", size="9"),
    #         rx.text(
    #             "Get started by editing ",
    #             rx.code(f"{config.app_name}/{config.app_name}.py"),
    #             size="5",
    #         ),
    #         rx.link(
    #             rx.button("Check out our docs!"),
    #             href="https://reflex.dev/docs/getting-started/introduction/",
    #             is_external=True,
    #         ),
    #         spacing="5",
    #         justify="center",
    #         min_height="85vh",
    #     ),
    #     rx.logo(),
    # )

app = rx.App(
    stylesheets=['https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css',
                 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap'],
    )

app.add_page(home_page, route='/')
app.add_page(contact_page, route='/contact')
app.add_page(products_page, route='/products')

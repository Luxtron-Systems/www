import reflex as rx
from luxtron.components.navbar import navbar
from luxtron.templates.footer import create_footer
from luxtron.templates.hero_section import create_hero_container
from luxtron.templates.featured_products import create_featured_products
from luxtron.templates.control_solutions import create_lighting_control_solutions
from luxtron.templates.cta_section import create_cta_section

def create_main_content():
    """Create the main content of the page including hero, products, solutions, and CTA."""
    return rx.box(
        navbar(),
        rx.container(
        rx.vstack(
            rx.heading("Welcome to Luxtron!", size="9"),
            rx.text("House of Lighting Solutions", size="5"),
            spacing="5", justify="center", min_height="85vh")
        ),
        create_hero_container(),
        rx.box(
            create_featured_products(),
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        rx.box(
            create_lighting_control_solutions(),
            background_color="#F3F4F6",
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        rx.box(
            create_cta_section(),
            background_color="#2563EB",
            padding_top="4rem",
            padding_bottom="4rem",
            color="#ffffff",
        ),
    )

def create():
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        create_main_content(),
        rx.box(
            create_footer(),
            background_color="#1F2937",
            padding_top="3rem",
            padding_bottom="3rem",
            color="#ffffff",
        ),
        class_name="font-['Poppins']",
        background_color="#F9FAFB",
        color="#1F2937",
    )
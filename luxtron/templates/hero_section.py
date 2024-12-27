import reflex as rx
from luxtron.components.button import create_styled_button

def create_hero_content():
    """Create the hero section content with heading, text, and CTA button."""
    return rx.box(
        rx.heading(
            "House of Lighting Solutions",
            font_weight="700",
            margin_bottom="1rem",
            font_size=rx.breakpoints(
                {"0px": "2.25rem", "768px": "3rem"}
            ),
            line_height=rx.breakpoints(
                {"0px": "2.5rem", "768px": "1"}
            ),
            as_="h1",
        ),
        rx.text(
            "Discover innovative lighting solutions for every space.",
            margin_bottom="1.5rem",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        create_styled_button(
            button_text="Explore Products"
        ),
        margin_bottom=rx.breakpoints(
            {"0px": "2rem", "768px": "0"}
        ),
        width=rx.breakpoints({"768px": "50%"}),
    )

def create_hero_section():
    """Create the complete hero section with content and image."""
    return rx.flex(
        create_hero_content(),
        rx.box(
            rx.image(
                src="https://placehold.co/600x400?text=Modern+Lighting+Fixture",
                alt="Modern lighting fixture illuminating a sleek interior space",
                border_radius="0.5rem",
                box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
            ),
            width=rx.breakpoints({"768px": "50%"}),
        ),
        display="flex",
        flex_direction=rx.breakpoints(
            {"0px": "column", "768px": "row"}
        ),
        align_items="center",
    )

def create_hero_container():
    """Create the container for the hero section with gradient background."""
    return rx.box(
        rx.box(
            create_hero_section(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
        ),
        class_name="bg-gradient-to-r from-blue-500 to-purple-600",
        padding_top="5rem",
        padding_bottom="5rem",
        color="#ffffff",
    )
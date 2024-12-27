import reflex as rx
from luxtron.components.text import create_centered_heading
from luxtron.components.button import create_styled_button

def create_cta_section():
    """Create the call-to-action section with heading, text, and button."""
    return rx.box(
        create_centered_heading(
            margin_bottom="2rem",
            heading_text="Ready to Upgrade Your Lighting?",
        ),
        rx.text(
            "Contact us today for a free consultation and let us illuminate your space.",
            margin_bottom="2rem",
            text_align="center",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        rx.flex(
            create_styled_button(
                button_text="Get in Touch"
            ),
            display="flex",
            justify_content="center",
        ),
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
    )
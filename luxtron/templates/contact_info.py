import reflex as rx
from luxtron.components.text import create_custom_heading, create_line_break

def create_contact_info():
    """Create the contact information section for the footer."""
    return rx.box(
        create_custom_heading(
            font_size="1.125rem",
            margin_bottom="1rem",
            heading_text="Contact Us",
        ),
        rx.text(
            "413, Luxtron Experience Center",
            create_line_break(),
            "Al Qusais Plaza",
            create_line_break(),
            "info@luxtron.net",
            create_line_break(),
            "+971 4 327 3594",
            color="#9CA3AF",
        ),
    )
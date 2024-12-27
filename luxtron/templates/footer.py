import reflex as rx
# from luxtron.components.comps import *
from luxtron.components.text import create_colored_text
from luxtron.components.links import create_hover_link, create_social_link
from luxtron.components.text import create_custom_heading
from luxtron.templates.contact_info import create_contact_info


def create_footer():
    """Create the complete footer with content and copyright notice."""
    return rx.box(
        create_footer_content(),
        rx.box(
            create_colored_text(
                text_color="#9CA3AF",
                text_content="© 2024 Luxtron. All rights reserved.",
            ),
            border_color="#374151",
            border_top_width="1px",
            margin_top="2rem",
            padding_top="2rem",
            text_align="center",
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

def create_footer_link_item(link_text):
    """Create a footer link list item."""
    return rx.el.li(
        create_hover_link(
            hover_styles={"color": "#ffffff"},
            text_color="#9CA3AF",
            link_text=link_text,
        )
    )

def create_footer_content():
    """Create the main content of the footer including about, links, contact, and social."""
    return rx.box(
        # rx.box(
        #     create_custom_heading(
        #         font_size="1.125rem",
        #         margin_bottom="1rem",
        #         heading_text="About Luxtron",
        #     ),
        #     create_colored_text(
        #         text_color="#9CA3AF",
        #         text_content="Innovative lighting solutions for homes and businesses. Illuminating spaces with style and efficiency.",
        #     ),
        # ),
        rx.box(
            create_custom_heading(
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Quick Links",
            ),
            rx.list(
                create_footer_link_item(
                    link_text="Products"
                ),
                create_footer_link_item(
                    link_text="Solutions"
                ),
                create_footer_link_item(
                    link_text="Support"
                ),
                create_footer_link_item(
                    link_text="Contact"
                ),
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
        ),
        create_contact_info(),
        rx.box(
            create_custom_heading(
                font_size="1.125rem",
                margin_bottom="1rem",
                heading_text="Follow Us",
            ),
            rx.flex(
                create_social_link(
                    icon_alt="Facebook", icon_tag="facebook"
                ),
                create_social_link(
                    icon_alt="Twitter", icon_tag="twitter"
                ),
                create_social_link(
                    icon_alt="Instagram",
                    icon_tag="instagram",
                ),
                create_social_link(
                    icon_alt="LinkedIn", icon_tag="linkedin"
                ),
                display="flex",
                column_gap="1rem",
            ),
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(4, minmax(0, 1fr))",
            }
        ),
    )

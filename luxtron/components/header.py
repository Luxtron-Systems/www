import reflex as rx

def create_header():
    """Create the main header with logo, navigation, and responsive menu."""
    return rx.flex(
        # rx.flex(
        #     rx.image(
        #         src="https://placehold.co/150x50?text=Luxtron+Logo",
        #         alt="Luxtron Logo",
        #         height="2.5rem",
        #     ),
        #     display="flex",
        #     align_items="center",
        # ),
        # rx.box(
        #     create_hover_link(
        #         hover_styles={"color": "#2563EB"},
        #         text_color="#374151",
        #         link_text="Home",
        #     ),
        #     create_hover_link(
        #         hover_styles={"color": "#2563EB"},
        #         text_color="#374151",
        #         link_text="Products",
        #     ),
        #     create_hover_link(
        #         hover_styles={"color": "#2563EB"},
        #         text_color="#374151",
        #         link_text="Solutions",
        #     ),
        #     create_hover_link(
        #         hover_styles={"color": "#2563EB"},
        #         text_color="#374151",
        #         link_text="About",
        #     ),
        #     create_hover_link(
        #         hover_styles={"color": "#2563EB"},
        #         text_color="#374151",
        #         link_text="Contact",
        #     ),
        #     display=rx.breakpoints(
        #         {"0px": "none", "768px": "flex"}
        #     ),
        #     column_gap="1.5rem",
        # ),
        rx.box(
            rx.icon(
                alt="Menu",
                tag="menu",
                cursor="pointer",
                height="1.5rem",
                width="1.5rem",
            ),
            display=rx.breakpoints({"768px": "none"}),
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
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
    )
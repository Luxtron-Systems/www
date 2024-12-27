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

def create_featured_products():
    """Create the featured products section with product cards."""
    return rx.box(
        create_centered_heading(
            margin_bottom="3rem",
            heading_text="Featured Products",
        ),
        rx.box(
            create_product_card(
                image_alt="Smart LED bulb with color changing capabilities",
                image_src="https://placehold.co/400x300?text=Smart+LED+Bulb",
                product_name="Smart LED Bulb",
                product_description="Energy-efficient bulb with millions of colors and smart controls.",
            ),
            create_product_card(
                image_alt="Modern pendant light with adjustable height",
                image_src="https://placehold.co/400x300?text=Pendant+Light",
                product_name="Pendant Light",
                product_description="Sleek design pendant light perfect for dining areas and kitchens.",
            ),
            create_product_card(
                image_alt="Flexible LED strip lights in various colors",
                image_src="https://placehold.co/400x300?text=LED+Strip+Lights",
                product_name="LED Strip Lights",
                product_description="Versatile strip lighting for accent and ambient lighting solutions.",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
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


def create_lighting_control_solutions():
    """Create the lighting control solutions section with feature boxes."""
    return rx.box(
        create_centered_heading(
            margin_bottom="3rem",
            heading_text="Lighting Control Solutions",
        ),
        rx.box(
            create_feature_box(
                icon_alt="Smartphone",
                icon_tag="smartphone",
                feature_title="Smart Home Integration",
                feature_description="Control your lighting with your smartphone or voice commands.",
            ),
            create_feature_box(
                icon_alt="Energy",
                icon_tag="zap",
                feature_title="Energy Management",
                feature_description="Optimize energy usage with intelligent scheduling and motion sensors.",
            ),
            create_feature_box(
                icon_alt="Color Palette",
                icon_tag="palette",
                feature_title="Scene Creation",
                feature_description="Set the perfect ambiance for any occasion with customizable lighting scenes.",
            ),
            create_feature_box(
                icon_alt="Settings",
                icon_tag="settings",
                feature_title="Advanced Controls",
                feature_description="Fine-tune your lighting with dimming, color temperature, and more.",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
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

from luxtron.components import navbar as nav

def create_main_content():
    """Create the main content of the page including hero, products, solutions, and CTA."""
    return rx.box(
        nav.navbar(),
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

def create_page_layout():
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
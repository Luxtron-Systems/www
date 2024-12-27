import reflex as rx
from luxtron.components.text import create_centered_heading
from luxtron.components.box_cards import create_product_card

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
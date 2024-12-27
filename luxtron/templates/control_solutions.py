import reflex as rx
from luxtron.components.text import create_centered_heading
from luxtron.components.box_cards import create_feature_box

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
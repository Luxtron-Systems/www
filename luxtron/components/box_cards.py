import reflex as rx
from luxtron.components.text import create_custom_heading, create_paragraph, create_colored_text
from luxtron.components.images import create_cover_image, create_feature_icon
from luxtron.components.links import create_learn_more_link

# Boxes
def create_content_box(title, description):
    """Create a content box with title, description, and 'Learn More' link."""
    return rx.box(
        create_custom_heading(
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=title,
        ),
        create_paragraph(paragraph_text=description),
        create_learn_more_link(),
        padding="1.5rem",
    )

def create_feature_box(icon_alt, icon_tag, feature_title, feature_description):
    """Create a feature box with icon, title, and description."""
    return rx.box(
        create_feature_icon(
            icon_alt=icon_alt, icon_tag=icon_tag
        ),
        create_custom_heading(
            font_size="1.25rem",
            margin_bottom="0.5rem",
            heading_text=feature_title,
        ),
        create_colored_text(
            text_color="#4B5563",
            text_content=feature_description,
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )

# Cards
def create_product_card(image_alt, image_src, product_name, product_description):
    """Create a product card with image, name, and description."""
    return rx.box(
        create_cover_image(
            alt_text=image_alt, image_src=image_src
        ),
        create_content_box(
            title=product_name,
            description=product_description,
        ),
        background_color="#ffffff",
        overflow="hidden",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
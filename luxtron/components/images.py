import reflex as rx

def create_cover_image(alt_text, image_src):
    """Create a cover image with specified dimensions."""
    return rx.image(
        src=image_src,
        alt=alt_text,
        height="12rem",
        object_fit="cover",
        width="100%",
    )

def create_feature_icon(icon_alt, icon_tag):
    """Create a feature icon with specified dimensions."""
    return rx.icon(
        alt=icon_alt,
        tag=icon_tag,
        height="3rem",
        margin_bottom="1rem",
        width="3rem",
    )

def create_social_icon(icon_alt, icon_tag):
    """Create a social media icon."""
    return rx.icon(
        alt=icon_alt,
        tag=icon_tag,
        height="1.5rem",
        width="1.5rem",
    )
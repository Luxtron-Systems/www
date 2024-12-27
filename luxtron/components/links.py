import reflex as rx
from luxtron.components.images import create_social_icon

def create_hover_link(hover_styles, text_color, link_text):
    """Create a hover-enabled link with custom styles."""
    return rx.el.a(
        link_text,
        href="#",
        transition_duration="300ms",
        _hover=hover_styles,
        color=text_color,
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )

def create_learn_more_link():
    """Create a 'Learn More' link with hover effects."""
    return rx.el.a(
        "Learn More",
        href="#",
        font_weight="500",
        _hover={"color": "#1E40AF"},
        color="#2563EB",
    )

def create_social_link(icon_alt, icon_tag):
    """Create a social media link with icon."""
    return rx.el.a(
        create_social_icon(
            icon_alt=icon_alt, icon_tag=icon_tag
        ),
        href="#",
        transition_duration="300ms",
        _hover={"color": "#ffffff"},
        color="#9CA3AF",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )
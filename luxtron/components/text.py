import reflex as rx

def create_custom_heading(font_size, margin_bottom, heading_text):
    """Create a custom heading with specified font size and margin."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height="1.75rem",
        as_="h3",
    )

def create_centered_heading(margin_bottom, heading_text):
    """Create a centered heading with specified margin."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )

def create_name_heading(name):
    """Create a heading for a name."""
    return rx.heading(
        name, font_weight="600", as_="h4", size="3"
    )

def create_name_title_box(name, title):
    """Create a box with name and title."""
    return rx.box(
        create_name_heading(name=name),
        create_colored_text(
            text_color="#4B5563", text_content=title
        ),
    )

def create_paragraph(paragraph_text):
    """Create a paragraph with specified text and styling."""
    return rx.text(
        paragraph_text,
        margin_bottom="1rem",
        color="#4B5563",
    )

def create_colored_text(text_color, text_content):
    """Create text with a specified color."""
    return rx.text(text_content, color=text_color)

def create_line_break():
    """Create a line break element."""
    return rx.el.br()
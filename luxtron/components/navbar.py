import reflex as rx

def navbar():
    return rx.box(
        rx.hstack(
            rx.text("Luxtron Systems", font_size="1.5em", font_weight="bold"),
            rx.spacer(),
            rx.color_mode.button(),
            rx.icon(
                tag="search",  # Predefined search icon
                size=24,
                # size="1.5em",
                cursor="pointer",
                on_click=print("Search clicked")  # Placeholder action
            ),
            # Hamburger Menu Icon
            rx.icon(
                tag="menu",  # Predefined hamburger menu icon
                size=24,
                # size="1.5em",
                cursor="pointer",
                on_click=print("Menu clicked")  # Placeholder action
            ),

            # rx.hstack(
            #     rx.icon(
            #         tag='search',
            #         size=24,
            #         cursor='pointer',
            #         on_click=lambda: print("Search icon clicked")
            #     ),
            #     rx.link("Home", href="#"),
            #     rx.link("News", href="#"),
            #     rx.link("Products", href="#"),
            #     rx.link("Solutions", href="#"),
            #     rx.link("Contact", href="#"),
            # ),
            spacing="4",
        ),
        id="navbar",
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="1000",
        # bg="rgba(0, 0, 0, 0.3)",  # Initial low opacity
        padding="1em",
        # backdrop_filter="blur(10px)",
        # transition="background 0.3s ease-in-out",
    )

def navbar_script():
    return rx.script(
        """
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 50) {
                navbar.style.background = 'rgba(0, 0, 0, 0.8)';
            } else {
                navbar.style.background = 'rgba(0, 0, 0, 0.3)';
            }
        });
        """
    )

import customtkinter as ctk

# Application appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class NexoraApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("NEXORA | Cybersecurity Intelligence Suite")
        self.geometry("1200x750")
        self.minsize(950, 600)

        self.configure(fg_color="#101820")

        # Main layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()
        self.show_dashboard()

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=240,
            corner_radius=0,
            fg_color="#17252D"
        )

        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        logo = ctk.CTkLabel(
            self.sidebar,
            text="N E X O R A",
            font=("Arial", 25, "bold"),
            text_color="#54D6A0"
        )
        logo.pack(pady=(35, 5))

        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="CYBERSECURITY SUITE",
            font=("Arial", 10),
            text_color="#94A8B2"
        )
        subtitle.pack(pady=(0, 35))

        self.menu_items = [
            "Dashboard",
            "Network Intelligence",
            "Wireless Watch",
            "Phishing Intelligence",
            "FileShield",
            "LoginGuard",
            "Security Reports"
        ]

        for item in self.menu_items:
            button = ctk.CTkButton(
                self.sidebar,
                text=item,
                anchor="w",
                height=42,
                corner_radius=8,
                fg_color="transparent",
                hover_color="#29443F",
                text_color="#D8E5E8",
                command=lambda name=item: self.show_page(name)
            )
            button.pack(fill="x", padx=15, pady=5)

        footer = ctk.CTkLabel(
            self.sidebar,
            text="NEXORA  |  VERSION 1.0",
            font=("Arial", 10),
            text_color="#72858D"
        )
        footer.pack(side="bottom", pady=25)

    def create_main_area(self):

        self.main_area = ctk.CTkFrame(
            self,
            fg_color="#101820",
            corner_radius=0
        )

        self.main_area.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

        self.main_area.grid_columnconfigure(0, weight=1)
        self.main_area.grid_rowconfigure(1, weight=1)

    def clear_main_area(self):

        for widget in self.main_area.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.show_page("Dashboard")

    def show_page(self, page):

        self.clear_main_area()

        heading = ctk.CTkLabel(
            self.main_area,
            text=page,
            font=("Arial", 30, "bold"),
            text_color="#FFFFFF"
        )
        heading.grid(row=0, column=0, sticky="w", pady=(15, 5))

        if page == "Dashboard":

            description = (
                "Welcome to Nexora. Your cybersecurity "
                "intelligence workspace."
            )

            cards = [
                ("01", "Network Intelligence",
                 "Monitor authorized network devices"),

                ("02", "Wireless Watch",
                 "Analyse nearby wireless signals"),

                ("03", "Phishing Intelligence",
                 "Analyse suspicious URLs"),

                ("04", "FileShield",
                 "Monitor file integrity"),

                ("05", "LoginGuard",
                 "Analyse login security events"),

                ("06", "Security Reports",
                 "Review security findings")
            ]

            content = ctk.CTkFrame(
                self.main_area,
                fg_color="transparent"
            )
            content.grid(row=1, column=0, sticky="nsew", pady=20)

            welcome = ctk.CTkLabel(
                content,
                text=description,
                font=("Arial", 15),
                text_color="#A5B8C0"
            )
            welcome.pack(anchor="w", pady=(0, 25))

            for number, title, detail in cards:

                card = ctk.CTkFrame(
                    content,
                    fg_color="#1B2B34",
                    corner_radius=12,
                    height=85
                )
                card.pack(fill="x", pady=7)
                card.pack_propagate(False)

                label = ctk.CTkLabel(
                    card,
                    text=f"{number}  |  {title}",
                    font=("Arial", 17, "bold"),
                    text_color="#54D6A0"
                )
                label.pack(anchor="w", padx=20, pady=(13, 2))

                info = ctk.CTkLabel(
                    card,
                    text=detail,
                    font=("Arial", 12),
                    text_color="#A5B8C0"
                )
                info.pack(anchor="w", padx=20)

        else:

            message = ctk.CTkLabel(
                self.main_area,
                text=(
                    f"{page} module\n\n"
                    "Module initialization pending.\n"
                    "Working functionality will be added "
                    "during development."
                ),
                font=("Arial", 17),
                text_color="#A5B8C0",
                justify="center"
            )
            message.grid(row=1, column=0, sticky="nsew")

        footer = ctk.CTkLabel(
            self.main_area,
            text="NEXORA | Independent Cybersecurity Project",
            font=("Arial", 10),
            text_color="#72858D"
        )
        footer.grid(row=2, column=0, sticky="e", pady=15)


if __name__ == "__main__":
    app = NexoraApp()
    app.mainloop()

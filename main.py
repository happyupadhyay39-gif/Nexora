
import customtkinter as ctk
from datetime import datetime


# ==========================================
# NEXORA | CYBERSECURITY INTELLIGENCE SUITE
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class NexoraApp(ctk.CTk):

    # ---------- COLOUR PALETTE ----------

    BG = "#0B1120"
    SIDEBAR = "#101A2B"
    PANEL = "#151F33"
    PANEL_LIGHT = "#1B2940"
    BORDER = "#263650"

    CYAN = "#39D9FF"
    BLUE = "#527BFF"
    PURPLE = "#9B7BFF"
    GREEN = "#39D9A0"

    WHITE = "#F0F5FF"
    MUTED = "#91A1BB"
    DIM = "#64748B"

    def __init__(self):
        super().__init__()

        self.title("NEXORA | Cybersecurity Intelligence Suite")
        self.geometry("1450x900")
        self.minsize(1100, 720)
        self.configure(fg_color=self.BG)

        self.current_page = "Dashboard"
        self.menu_buttons = {}

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()
        self.show_page("Dashboard")
        self.update_clock()

    # ---------- SIDEBAR ----------

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=245,
            corner_radius=0,
            fg_color=self.SIDEBAR
        )

        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        # Brand
        brand = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )
        brand.pack(fill="x", padx=22, pady=(32, 28))

        ctk.CTkLabel(
            brand,
            text="◈ NEXORA",
            font=("Arial", 27, "bold"),
            text_color=self.CYAN
        ).pack(anchor="w")

        ctk.CTkLabel(
            brand,
            text="CYBERSECURITY INTELLIGENCE",
            font=("Arial", 9, "bold"),
            text_color=self.MUTED
        ).pack(anchor="w", pady=(7, 0))

        # Navigation heading
        ctk.CTkLabel(
            self.sidebar,
            text="WORKSPACE",
            font=("Arial", 10, "bold"),
            text_color=self.DIM
        ).pack(anchor="w", padx=25, pady=(5, 12))

        self.menu_items = [
            ("⌂", "Dashboard"),
            ("⌘", "Network Intelligence"),
            ("◉", "Wireless Watch"),
            ("◇", "Phishing Intelligence"),
            ("▣", "FileShield"),
            ("◈", "LoginGuard"),
            ("▤", "Security Reports")
        ]

        for icon, name in self.menu_items:

            button = ctk.CTkButton(
                self.sidebar,
                text=f"   {icon}     {name}",
                anchor="w",
                height=46,
                corner_radius=10,
                font=("Arial", 12, "bold"),
                fg_color="transparent",
                hover_color=self.PANEL_LIGHT,
                text_color=self.MUTED,
                command=lambda n=name: self.show_page(n)
            )

            button.pack(fill="x", padx=13, pady=4)
            self.menu_buttons[name] = button

        # Bottom profile / project panel
        bottom = ctk.CTkFrame(
            self.sidebar,
            fg_color=self.PANEL,
            corner_radius=12
        )
        bottom.pack(side="bottom", fill="x", padx=15, pady=20)

        ctk.CTkLabel(
            bottom,
            text="●  SYSTEM READY",
            font=("Arial", 10, "bold"),
            text_color=self.GREEN
        ).pack(anchor="w", padx=14, pady=(13, 5))

        ctk.CTkLabel(
            bottom,
            text="Nexora Independent Project\nVersion 2.0",
            font=("Arial", 10),
            text_color=self.MUTED,
            justify="left"
        ).pack(anchor="w", padx=14, pady=(0, 13))

    # ---------- MAIN AREA ----------

    def create_main_area(self):

        self.main_area = ctk.CTkFrame(
            self,
            fg_color=self.BG,
            corner_radius=0
        )

        self.main_area.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=25,
            pady=20
        )

        self.main_area.grid_columnconfigure(0, weight=1)
        self.main_area.grid_rowconfigure(1, weight=1)

        # Header
        self.header = ctk.CTkFrame(
            self.main_area,
            fg_color="transparent"
        )
        self.header.grid(row=0, column=0, sticky="ew", pady=(0, 18))

        self.header.grid_columnconfigure(0, weight=1)

        self.page_title = ctk.CTkLabel(
            self.header,
            text="Dashboard",
            font=("Arial", 29, "bold"),
            text_color=self.WHITE
        )
        self.page_title.grid(row=0, column=0, sticky="w")

        self.clock_label = ctk.CTkLabel(
            self.header,
            text="",
            font=("Arial", 12),
            text_color=self.MUTED
        )
        self.clock_label.grid(row=0, column=1, padx=(10, 18))

        self.status_label = ctk.CTkLabel(
            self.header,
            text="●  SYSTEM ONLINE",
            font=("Arial", 10, "bold"),
            text_color=self.GREEN,
            fg_color=self.PANEL,
            corner_radius=9
        )
        self.status_label.grid(row=0, column=2, padx=5, ipady=9, ipadx=10)

        # Scrollable page content
        self.content = ctk.CTkScrollableFrame(
            self.main_area,
            fg_color="transparent",
            scrollbar_button_color=self.BORDER,
            scrollbar_button_hover_color=self.CYAN
        )
        self.content.grid(row=1, column=0, sticky="nsew")

    # ---------- NAVIGATION ----------

    def update_navigation(self, active_page):

        for name, button in self.menu_buttons.items():

            if name == active_page:
                button.configure(
                    fg_color="#18374A",
                    text_color=self.CYAN,
                    hover_color="#21445B"
                )
            else:
                button.configure(
                    fg_color="transparent",
                    text_color=self.MUTED,
                    hover_color=self.PANEL_LIGHT
                )

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    def show_page(self, page):

        self.current_page = page

        self.page_title.configure(text=page)
        self.update_navigation(page)
        self.clear_content()

        if page == "Dashboard":
            self.build_dashboard()
        else:
            self.build_module_page(page)

    # ---------- REUSABLE METRIC CARD ----------

    def create_metric_card(
        self, parent, title, value, subtitle, accent
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=self.PANEL,
            corner_radius=14,
            border_width=1,
            border_color=self.BORDER
        )

        ctk.CTkLabel(
            card,
            text=title.upper(),
            font=("Arial", 10, "bold"),
            text_color=self.MUTED
        ).pack(anchor="w", padx=17, pady=(17, 8))

        ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 25, "bold"),
            text_color=accent
        ).pack(anchor="w", padx=17)

        ctk.CTkLabel(
            card,
            text=subtitle,
            font=("Arial", 10),
            text_color=self.DIM
        ).pack(anchor="w", padx=17, pady=(5, 17))

        return card

    # ---------- DASHBOARD ----------

    def build_dashboard(self):

        for column in range(4):
             self.content.grid_columnconfigure(column, weight=1)

        # Welcome banner
        banner = ctk.CTkFrame(
            self.content,
            fg_color="#172B43",
            corner_radius=18,
            border_width=1,
            border_color="#284A68"
        )
        banner.grid(
            row=0, column=0, columnspan=4,
            sticky="ew", pady=(5, 20)
        )

        banner.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            banner,
            text="WELCOME TO NEXORA",
            font=("Arial", 11, "bold"),
            text_color=self.CYAN
        ).grid(row=0, column=0, sticky="w", padx=23, pady=(20, 5))

        ctk.CTkLabel(
            banner,
            text="Your Security. Your Intelligence. Your Control.",
            font=("Arial", 22, "bold"),
            text_color=self.WHITE
        ).grid(row=1, column=0, sticky="w", padx=23)

        ctk.CTkLabel(
            banner,
            text=(
                "Monitor your environment, investigate potential risks "
                "and manage your security tools from one workspace."
            ),
            font=("Arial", 11),
            text_color="#AFC3DC"
        ).grid(row=2, column=0, sticky="w", padx=23, pady=(7, 20))

        ctk.CTkLabel(
            banner,
            text="◈\nNEXORA\nINTELLIGENCE",
            font=("Arial", 15, "bold"),
            text_color=self.CYAN,
            justify="center"
        ).grid(row=0, column=1, rowspan=3, padx=35)

        # Section heading
        ctk.CTkLabel(
            self.content,
            text="SECURITY OVERVIEW",
            font=("Arial", 12, "bold"),
            text_color=self.WHITE
        ).grid(
            row=1, column=0, columnspan=4,
            sticky="w", pady=(0, 12)
        )

        # Metric cards
        metrics = [
            ("Network Devices", "--", "Awaiting network scan", self.CYAN),
            ("Wireless Signals", "--", "Awaiting wireless scan", self.PURPLE),
            ("Security Alerts", "0", "No alerts recorded yet", self.GREEN),
            ("System Status", "READY", "Nexora workspace active", self.BLUE)
        ]

        for column, data in enumerate(metrics):

            card = self.create_metric_card(
                self.content, *data
            )

            card.grid(
                row=2, column=column,
                sticky="nsew", padx=5, pady=(0, 22)
            )

        # Lower section
        lower = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )
        lower.grid(
            row=3, column=0, columnspan=4,
            sticky="ew", pady=5
        )

        lower.grid_columnconfigure(0, weight=3)
        lower.grid_columnconfigure(1, weight=2)

        # Network overview panel
        network = ctk.CTkFrame(
            lower,
            fg_color=self.PANEL,
            corner_radius=15,
            border_width=1,
            border_color=self.BORDER
        )
        network.grid(
            row=0, column=0,
            sticky="nsew", padx=(0, 9)
        )

        ctk.CTkLabel(
            network,
            text="NETWORK INTELLIGENCE",
            font=("Arial", 13, "bold"),
            text_color=self.WHITE
        ).pack(anchor="w", padx=19, pady=(17, 4))

        ctk.CTkLabel(
            network,
            text="Authorized network visibility",
            font=("Arial", 10),
            text_color=self.MUTED
        ).pack(anchor="w", padx=19)

        visual = ctk.CTkFrame(
            network,
            fg_color="#101B2D",
            corner_radius=12,
            height=145
        )
        visual.pack(fill="x", padx=15, pady=15)
        visual.pack_propagate(False)

        ctk.CTkLabel(
            visual,
            text="◉",
            font=("Arial", 35),
            text_color=self.CYAN
        ).pack(pady=(17, 0))

        ctk.CTkLabel(
            visual,
            text="NETWORK MAP",
            font=("Arial", 12, "bold"),
            text_color=self.WHITE
        ).pack(pady=2)

        ctk.CTkLabel(
            visual,
            text="Your network visualization will appear after a scan.",
            font=("Arial", 10),
            text_color=self.MUTED
        ).pack(pady=3)

        ctk.CTkButton(
            network,
            text="OPEN NETWORK INTELLIGENCE  →",
            height=37,
            fg_color="#173A50",
            hover_color="#20536E",
            text_color=self.CYAN,
            font=("Arial", 10, "bold"),
            command=lambda: self.show_page("Network Intelligence")
        ).pack(fill="x", padx=15, pady=(0, 16))

        # Activity panel
        activity = ctk.CTkFrame(
            lower,
            fg_color=self.PANEL,
            corner_radius=15,
            border_width=1,
            border_color=self.BORDER
        )
        activity.grid(
            row=0, column=1,
            sticky="nsew", padx=(9, 0)
        )

        ctk.CTkLabel(
            activity,
            text="RECENT ACTIVITY",
            font=("Arial", 13, "bold"),
            text_color=self.WHITE
        ).pack(anchor="w", padx=18, pady=(17, 4))

        ctk.CTkLabel(
            activity,
            text="Security workspace events",
            font=("Arial", 10),
            text_color=self.MUTED
        ).pack(anchor="w", padx=18, pady=(0, 13))

        events = [
            ("●", "Workspace initialized", "Nexora is ready", self.GREEN),
            ("●", "Modules registered", "6 modules available", self.CYAN),
            ("●", "Network scan", "Waiting for first scan", self.PURPLE),
            ("●", "Threat analysis", "Waiting for analysis", self.BLUE)
        ]

        for icon, title, detail, color in events:

            event = ctk.CTkFrame(
                activity,
                fg_color="transparent"
            )
            event.pack(fill="x", padx=15, pady=8)

            ctk.CTkLabel(
                event,
                text=icon,
                text_color=color,
                font=("Arial", 13)
            ).pack(side="left", padx=(2, 10))

            text_area = ctk.CTkFrame(
                event,
                fg_color="transparent"
            )
            text_area.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                text_area,
                text=title,
                font=("Arial", 11, "bold"),
                text_color=self.WHITE
            ).pack(anchor="w")

            ctk.CTkLabel(
                text_area,
                text=detail,
                font=("Arial", 9),
                text_color=self.MUTED
            ).pack(anchor="w")

        # Module launcher
        ctk.CTkLabel(
            self.content,
            text="INTELLIGENCE MODULES",
            font=("Arial", 12, "bold"),
            text_color=self.WHITE
        ).grid(
            row=4, column=0, columnspan=4,
            sticky="w", pady=(23, 12)
        )

        modules = [
            ("01", "Network Intelligence", "Authorized device discovery", self.CYAN),
            ("02", "Wireless Watch", "Wireless environment analysis", self.PURPLE),
            ("03", "Phishing Intelligence", "Suspicious URL analysis", self.GREEN),
            ("04", "FileShield", "File integrity monitoring", self.BLUE),
            ("05", "LoginGuard", "Login security monitoring", self.CYAN),
            ("06", "Security Reports", "Security findings and reports", self.PURPLE)
        ]

        for index, (number, name, detail, color) in enumerate(modules):

            row = 5 + index // 3
            column = index % 3

            self.content.grid_columnconfigure(column, weight=1)

            module_card = ctk.CTkFrame(
                self.content,
                fg_color=self.PANEL,
                corner_radius=13,
                border_width=1,
                border_color=self.BORDER
            )

            module_card.grid(
                row=row, column=column,
                sticky="nsew", padx=5, pady=6
            )

            ctk.CTkLabel(
                module_card,
                text=f"MODULE  {number}",
                font=("Arial", 9, "bold"),
                text_color=color
            ).pack(anchor="w", padx=15, pady=(14, 5))

            ctk.CTkLabel(
                module_card,
                text=name,
                font=("Arial", 13, "bold"),
                text_color=self.WHITE
            ).pack(anchor="w", padx=15)

            ctk.CTkLabel(
                module_card,
                text=detail,
                font=("Arial", 10),
                text_color=self.MUTED
            ).pack(anchor="w", padx=15, pady=(5, 10))

            ctk.CTkButton(
                module_card,
                text="OPEN MODULE  →",
                height=32,
                fg_color="#20344B",
                hover_color="#294B68",
                text_color=color,
                font=("Arial", 9, "bold"),
                command=lambda n=name: self.show_page(n)
            ).pack(fill="x", padx=13, pady=(0, 13))

        ctk.CTkLabel(
            self.content,
            text="NEXORA  •  INDEPENDENT CYBERSECURITY PROJECT  •  VERSION 2.0",
            font=("Arial", 9),
            text_color=self.DIM
        ).grid(
            row=7, column=0, columnspan=4,
            sticky="e", pady=22
        )

    # ---------- MODULE PAGES ----------

    def build_module_page(self, page):

        self.content.grid_columnconfigure(0, weight=1)

        descriptions = {
            "Network Intelligence":
                "Discover and review devices on networks you are authorized to assess.",

            "Wireless Watch":
                "Explore visible wireless networks and nearby discoverable Bluetooth devices.",

            "Phishing Intelligence":
                "Examine suspicious URLs and identify potential phishing indicators.",

            "FileShield":
                "Monitor file integrity using cryptographic hashes.",

            "LoginGuard":
                "Review available Windows login security events.",

            "Security Reports":
                "Review findings and prepare security assessment reports."
        }

        panel = ctk.CTkFrame(
            self.content,
            fg_color=self.PANEL,
            corner_radius=18,
            border_width=1,
            border_color=self.BORDER
        )

        panel.grid(
            row=0, column=0,
            sticky="ew", pady=20
        )

        ctk.CTkLabel(
            panel,
            text="◈",
            font=("Arial", 42),
            text_color=self.CYAN
        ).pack(anchor="w", padx=25, pady=(25, 5))

        ctk.CTkLabel(
            panel,
            text=page,
            font=("Arial", 23, "bold"),
            text_color=self.WHITE
        ).pack(anchor="w", padx=25, pady=5)

        ctk.CTkLabel(
            panel,
            text=descriptions.get(page, ""),
            font=("Arial", 12),
            text_color=self.MUTED,
            wraplength=650,
            justify="left"
        ).pack(anchor="w", padx=25, pady=(5, 20))

        ctk.CTkLabel(
            panel,
            text="MODULE STATUS",
            font=("Arial", 10, "bold"),
            text_color=self.MUTED
        ).pack(anchor="w", padx=25)

        ctk.CTkLabel(
            panel,
            text="●  Under Development",
            font=("Arial", 13, "bold"),
            text_color=self.PURPLE
        ).pack(anchor="w", padx=25, pady=(5, 25))

        ctk.CTkButton(
            self.content,
            text="←  BACK TO DASHBOARD",
            width=210,
            height=42,
            fg_color="#18374A",
            hover_color="#20536E",
            text_color=self.CYAN,
            command=lambda: self.show_page("Dashboard")
        ).grid(row=1, column=0, sticky="w", pady=10)

    # ---------- LIVE CLOCK ----------

    def update_clock(self):

        current_time = datetime.now().strftime(
            "%d %b %Y   |   %I:%M:%S %p"
        )

        self.clock_label.configure(text=current_time)

        self.after(1000, self.update_clock)


# ---------- APPLICATION START ----------

if __name__ == "__main__":

    app = NexoraApp()
    app.mainloop()

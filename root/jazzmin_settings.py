# ========================
# 🎨 JAZZMIN CONFIG — BoxHub
# ========================

# JAZZMIN_UI_TWEAKS = {
#     "theme": "flatly",            # Bosh tema (Bootstrap varianti)
#     "navbar": "navbar-dark",      # Yuqori panel qoramtir
#     "sidebar": "dark",            # Chap menyu qoramtir
#     "dark_mode_theme": "slate",   # Tungi rejimda ishlatiladigan tema
#     "footer_fixed": True,
#     "actions_sticky_top": True,
# }

JAZZMIN_SETTINGS = {
    # --- Asosiy ma’lumotlar ---
    "site_title": "BoxHub Admin",
    "site_header": "BoxHub Management",
    "site_brand": "BoxHub",
    "site_logo": "static/img/boxhub_logo.png",  # static ichida saqlanadigan logo
    "login_logo": "static/img/boxhub_logo.png",
    "login_logo_dark": "static/img/boxhub_logo.png",
    "site_logo_classes": "img-circle shadow-sm",
    "site_icon": "static/img/boxhub_logo.png",
    "welcome_sign": "Welcome to BoxHub Dashboard",
    "copyright": "© 2025 BoxHub. All rights reserved.",
    "index_title": "BoxHub boshqaruv paneli",

    # --- Qidiruv ---
    "search_model": [
        "auth.User",
        "products.Product",
        "products.Category",
    ],

    # --- User avatar ---
    "user_avatar": None,

    # --- Yuqori menyu (header bar) ---
    "topmenu_links": [
        {"name": "BoxHub", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Saytga o‘tish", "url": "/", "new_window": True},
        {"model": "auth.User"},
        {"app": "products"},
    ],

    # --- User menyusi ---
    "usermenu_links": [
        {"model": "auth.user"},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin", "new_window": True},
    ],

    # --- Sidebar menyu sozlamalari ---
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": ["sessions", "admin", "contenttypes"],
    "hide_models": ["auth.Group"],
    "order_with_respect_to": ["products", "orders", "auth", "users"],

    # --- Custom links ---
    "custom_links": {
        "products": [
            {
                "name": "Quick Add Product",
                "url": "admin:products_product_add",
                "icon": "fas fa-plus-circle",
                "permissions": ["products.add_product"],
            },
        ],
    },

    # --- Ikonalar ---
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "products": "fas fa-boxes",
        "products.category": "fas fa-tags",
        "products.product": "fas fa-coffee",
        "orders": "fas fa-receipt",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-dot-circle",

    # --- Modal o‘rniga popup ishlatish ---
    "related_modal_active": True,

    # --- UI Tweaks ---
    "custom_css": "static/css/custom_admin.css",
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    # --- Forma tartibi ---
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },

    # --- Tema (bootstrap varianti) ---
    "theme": "flatly",
}

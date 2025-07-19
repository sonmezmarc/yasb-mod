DEFAULTS = {
    "label": "{icon}",
    "update_interval": 60,
    "change_automatically": False,
    "image_path": "",
    "tooltip": True,
    "gallery": {
        "enabled": False,
        "blur": True,
        "image_width": 100,
        "image_per_page": 5,
        "image_corner_radius": 0,
        "show_buttons": True,
        "orientation": "landscape",
        "image_spacing": 5,
        "lazy_load": True,
        "lazy_load_fadein": 200,
        "lazy_load_delay": 0,  # Deprecated
        "enable_cache": False,  # Deprecated
    },
    "run_after": [],
    "animation": {"enabled": True, "type": "fadeInOut", "duration": 200},
    "container_padding": {"top": 0, "left": 0, "bottom": 0, "right": 0},
}

VALIDATION_SCHEMA = {
    "label": {"type": "string", "default": DEFAULTS["label"]},
    "update_interval": {"type": "integer", "default": DEFAULTS["update_interval"], "min": 60, "max": 86400},
    "change_automatically": {"type": "boolean", "default": DEFAULTS["change_automatically"]},
    "image_path": {"required": True, "type": "string", "default": DEFAULTS["image_path"]},
    "tooltip": {"required": False, "type": "boolean", "default": DEFAULTS["tooltip"]},
    "gallery": {
        "type": "dict",
        "required": False,
        "schema": {
            "enabled": {"type": "boolean", "default": DEFAULTS["gallery"]["enabled"]},
            "blur": {"type": "boolean", "default": DEFAULTS["gallery"]["blur"]},
            "image_width": {"type": "integer", "default": DEFAULTS["gallery"]["image_width"], "min": 32, "max": 640},
            "image_per_page": {
                "type": "integer",
                "default": DEFAULTS["gallery"]["image_per_page"],
                "min": 1,
                "max": 24,
            },
            "image_corner_radius": {
                "type": "integer",
                "default": DEFAULTS["gallery"]["image_corner_radius"],
                "min": 0,
                "max": 50,
            },
            "show_buttons": {"type": "boolean", "default": DEFAULTS["gallery"]["show_buttons"]},
            "orientation": {
                "type": "string",
                "default": DEFAULTS["gallery"]["orientation"],
                "allowed": ["landscape", "portrait"],
            },
            "image_spacing": {"type": "integer", "default": DEFAULTS["gallery"]["image_spacing"], "min": 0, "max": 100},
            "lazy_load": {"type": "boolean", "default": DEFAULTS["gallery"]["lazy_load"]},
            "lazy_load_fadein": {
                "type": "integer",
                "default": DEFAULTS["gallery"]["lazy_load_fadein"],
                "min": 0,
                "max": 1000,
            },
            "lazy_load_delay": {
                "type": "integer",
                "default": DEFAULTS["gallery"]["lazy_load_delay"],
                "min": 0,
                "max": 1000,
            },
            "enable_cache": {"type": "boolean", "default": DEFAULTS["gallery"]["enable_cache"]},
        },
    },
    "run_after": {"required": False, "type": "list", "default": DEFAULTS["run_after"], "schema": {"type": "string"}},
    "animation": {
        "type": "dict",
        "required": False,
        "schema": {
            "enabled": {"type": "boolean", "default": DEFAULTS["animation"]["enabled"]},
            "type": {"type": "string", "default": DEFAULTS["animation"]["type"]},
            "duration": {"type": "integer", "default": DEFAULTS["animation"]["duration"]},
        },
        "default": DEFAULTS["animation"],
    },
    "label_shadow": {
        "type": "dict",
        "required": False,
        "schema": {
            "enabled": {"type": "boolean", "default": False},
            "color": {"type": "string", "default": "black"},
            "offset": {"type": "list", "default": [1, 1]},
            "radius": {"type": "integer", "default": 3},
        },
        "default": {"enabled": False, "color": "black", "offset": [1, 1], "radius": 3},
    },
    "container_shadow": {
        "type": "dict",
        "required": False,
        "schema": {
            "enabled": {"type": "boolean", "default": False},
            "color": {"type": "string", "default": "black"},
            "offset": {"type": "list", "default": [1, 1]},
            "radius": {"type": "integer", "default": 3},
        },
        "default": {"enabled": False, "color": "black", "offset": [1, 1], "radius": 3},
    },
    "container_padding": {
        "type": "dict",
        "required": False,
        "schema": {
            "top": {"type": "integer", "default": DEFAULTS["container_padding"]["top"]},
            "left": {"type": "integer", "default": DEFAULTS["container_padding"]["left"]},
            "bottom": {"type": "integer", "default": DEFAULTS["container_padding"]["bottom"]},
            "right": {"type": "integer", "default": DEFAULTS["container_padding"]["right"]},
        },
        "default": DEFAULTS["container_padding"],
    },
}

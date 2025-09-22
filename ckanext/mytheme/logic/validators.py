import ckan.plugins.toolkit as tk


def mytheme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "mytheme_required": mytheme_required,
    }

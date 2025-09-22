import ckan.plugins.toolkit as tk
import ckanext.mytheme.logic.schema as schema


@tk.side_effect_free
def mytheme_get_sum(context, data_dict):
    tk.check_access(
        "mytheme_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.mytheme_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'mytheme_get_sum': mytheme_get_sum,
    }

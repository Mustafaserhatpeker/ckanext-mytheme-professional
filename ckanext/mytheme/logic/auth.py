import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def mytheme_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "mytheme_get_sum": mytheme_get_sum,
    }

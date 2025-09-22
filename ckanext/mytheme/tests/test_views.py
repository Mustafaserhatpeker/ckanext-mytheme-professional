"""Tests for views.py."""

import pytest

import ckanext.mytheme.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "mytheme")
@pytest.mark.usefixtures("with_plugins")
def test_mytheme_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("mytheme.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, mytheme!"

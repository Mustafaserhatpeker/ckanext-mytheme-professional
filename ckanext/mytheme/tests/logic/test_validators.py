"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.mytheme.logic import validators


def test_mytheme_reauired_with_valid_value():
    assert validators.mytheme_required("value") == "value"


def test_mytheme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.mytheme_required(None)

"""Tests for helpers.py."""

import ckanext.mytheme.helpers as helpers


def test_mytheme_hello():
    assert helpers.mytheme_hello() == "Hello, mytheme!"

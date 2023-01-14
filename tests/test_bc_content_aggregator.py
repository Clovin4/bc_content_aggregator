#!/usr/bin/env python

"""Tests for `bc_content_aggregator` package."""

import pytest

from click.testing import CliRunner

from bc_content_aggregator import bc_content_aggregator
from bc_content_aggregator import cli

from src.main import ContentAggregator

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'bc_content_aggregator.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

def test_add_two_nums():
    c = ContentAggregator()

    res = c.add(4,5)

    assert res == 9

def test_add_three_nums():
    c = ContentAggregator()

    res = c.add(4,5,6)
    
    assert res == 15

def test_add_many_numbers():
    s = range(100)

    assert ContentAggregator().add(*s) == 4950

def test_subtract_two_nums():
    c = ContentAggregator()

    res = c.sub(10,3)

    assert res == 7

def test_mul_two_numbers():
    c = ContentAggregator()

    res = c.mul(6, 4)

    assert res == 24

def test_mul_many_numbers():
    s = range(1, 10)

    assert ContentAggregator().mul(*s) == 362880
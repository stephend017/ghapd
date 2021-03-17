import json
from typing import List
import pytest
from ghapd.configs import config_manager


def load_config(
    sources=["path1/*", "/path1/subpath1/", "/path1/subpath1/file1.py"],
    title_prefix="valid_prefix",
    exclude: List[str] = [],
):
    """
    Loads a config into the test config file,
    used to setup config tests.

    No parameters are typed so invalid types can
    be simulated. Instead a default value of the
    correct type is provided for each value
    """

    with open("./tests/test_configs/test.config.json", "w") as fp:
        data = {"sources": sources, "title_prefix": title_prefix}
        for element in exclude:
            del data[element]
        json.dump(data, fp)


def load_and_validate():
    """
    Loads and validates the test config file
    """
    config_manager.load_config_file("./tests/test_configs/test.config.json")
    config_manager.validate()


def load_and_validate_fails():
    """
    Loads and validates the test config file that
    contains errors (is invalid)
    """
    config_manager.load_config_file("./tests/test_configs/test.config.json")
    with pytest.raises(ValueError):
        config_manager.validate()

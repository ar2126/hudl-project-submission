"""
Description: Used to setup the config file located in ../.env

@author aidanrubenstein
@since 08/04/2022
"""
from environs import Env


def pytest_configure(config):
    """
    Performs test-setup steps which need to be performed exactly once
    at the beginning of the test run.
    :return:
    """
    if not hasattr(config, "workerinput"):
        env_object = Env()
        env_object.read_env(".env")


def pytest_generate_tests(metafunc):
    # load environment data
    env_object = Env()
    env_object.read_env(".env")
    # add Environment object to test
    if "env_object" in metafunc.fixturenames:
        metafunc.parametrize("env_object", [env_object])

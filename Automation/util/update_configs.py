"""
Description: Used to replace the environment file configs for grabbing hidden secrets

@author aidanrubenstein
@since 08/04/2022
"""
import configparser
import os


def update_env(filepath, header, mapping):
    # Verify config file is present.
    assert os.path.exists(filepath), filepath + " not found in specified path."

    config = configparser.RawConfigParser()
    config.optionxform = str
    config.read(filepath)

    # If a variable mapping does not exist
    # it will ignore the value
    for key, val in mapping.items():
        default = None

        val = os.getenv(val, default)

        if val:
            config[header][key] = val

    with open(filepath, "w") as configfile:
        config.write(configfile)


if __name__ == "__main__":
    ENV_PATH = ".env"
    update_env(ENV_PATH, "env", {"PASSWORD": "USER_PASS"})

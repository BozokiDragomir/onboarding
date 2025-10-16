import os
class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "") # Default is empty string for local development
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "") # Default is empty string for local development
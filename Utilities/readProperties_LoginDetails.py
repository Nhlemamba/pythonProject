import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/LoginDetails.ini")


class ReadLoginConfig:
    def getWay2Automation_URL(self):
        return config.get("URL", "Way2Automation_URL")

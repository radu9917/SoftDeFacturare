import json


class Config:
    __instance = None

    @staticmethod
    def get_instance():
        if not Config.__instance:
            Config("config.json")
        return Config.__instance

    def __init__(self, file_name):
        if Config.__instance:
            raise Exception("Instance already exists")
        Config.__instance = self
        self.__bill_template = None
        self.__file_name = file_name
        self.__template_folder = None
        self.load_config()

    def load_config(self):
        with open(self.__file_name, "r") as file:
            json_file = json.loads(file.read())
        self.__template_folder = json_file["template_folder"]
        self.__bill_template = json_file["template_folder"] + json_file["selected_bill_template"]

    def get_template_folder(self):
        return self.__template_folder

    def get_bill_template(self):
        return self.__bill_template + ".html"

    def get_bill_item_template(self):
        return self.__bill_template+"_item.html"

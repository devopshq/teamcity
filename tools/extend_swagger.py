# This script extend swagger generated code
import argparse
import inspect
import logging
import sys



def init_logging():
    logger_format_string = '%(thread)5s %(module)-20s %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=logger_format_string, stream=sys.stdout)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--value", action="store")

    args = parser.parse_args()
    return args


class Program:
    def __init__(self, value):
        self.value = value

    def run(self):
        # swagger generate `File` class, but import `file`. Fix it :)
        with open('../teamcity/models/file.py', mode='a+') as file:
            file.seek(0)
            content = file.read()
            str_ = '\nfile = File\n'
            if str_ not in content:
                file.write(str_)

        # import after some fix
        import teamcity.api

        # APIs
        apis = []
        for name, obj in inspect.getmembers(teamcity.api):
            if inspect.isclass(obj):
                apis.append(obj)

        pass


if __name__ == "__main__":
    args = parse_args()
    init_logging()
    Program(**vars(args)).run()

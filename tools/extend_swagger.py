# This script extend swagger generated code
import argparse
import inspect
import logging
import os
import re
import sys


def init_logging():
    logger_format_string = '%(thread)5s %(module)-20s %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=logger_format_string, stream=sys.stdout)


def convert(name):
    """
    CamelCase to under_score
    :param name:
    :return:
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--value", action="store")

    args = parser.parse_args()
    return args


def append_to_file(filename, content):
    if not content:
        logging.debug('Skip adding None content to "{}"'.format(filename))
    if isinstance(content, list):
        content = "\n".join(content)

    with open(filename, mode='a+') as file:
        file.seek(0)
        original_content = file.read()

        content = """
#
# Appended by {}
#

{}
""".format(os.path.basename(__file__), content)
        if content in original_content:
            logging.debug("File '{}' content up to date".format(filename))
        else:
            logging.debug("Append to file '{}'".format(filename, content))

            file.write(content)


class Program:
    def __init__(self, value):
        self.value = value

    def run(self):
        # swagger generate `File` class, but import `file`. Fix it :)
        append_to_file('../teamcity/models/file.py', 'file = File')

        # import after some fix
        import teamcity.api

        # APIs load
        apis = [(name, cls) for name, cls in inspect.getmembers(teamcity.api, inspect.isclass)]

        for cls_name, cls in apis:
            append = [""]
            methods = inspect.getmembers(cls, lambda x: inspect.isfunction(x) and not x.__name__.startswith('_'))

            #
            # get => serve_N, get_N, ...
            # extend api, we want use teamcity.agents.get('id:123'), not serve_agent(...)
            #
            lowername = cls.base_name.lower()
            lastname = convert(cls.base_name).split('_')[-1]
            get_method = [
                'serve_{}'.format(lowername),  # Agent => serve_agent
                'serve_{}'.format(lastname),  # VcsRoot => serve_root, AgentPool => serve_pool
                'get_{}'.format(lastname),  # AgentPool => get_pool
            ]
            get_serve_ = [(name, method) for name, method in methods if name in get_method]

            if len(get_serve_) == 1:
                logging.debug("Found serve\get method '{}' in api '{}'".format(get_serve_, cls_name))
                get_format = """
    def get(self, *args, **kwargs):
        return self.{}(*args, **kwargs)"""
                append.append(get_format.format(get_serve_[0][0]))
            elif len(get_serve_) == 0:
                logging.debug("Serve\get method not fount in api '{}'".format(cls_name))
            elif len(get_serve_) > 1:
                logging.error("Something wrong, get method must be unique")
                sys.exit(11)

            #
            # get_N => serve_N
            #
            serve_methods = inspect.getmembers(cls, lambda x: inspect.isfunction(x) and x.__name__.startswith('serve_'))
            get_serve_format = """
    def get_{name}(self, *args, **kwargs):
        return self.serve_{name}(*args, **kwargs)"""
            for name, method in serve_methods:
                name = name.replace('serve_', '')
                append.append(get_serve_format.format(name=name))

            filename = inspect.getfile(cls)
            append_to_file(filename, content=append)

        pass


if __name__ == "__main__":
    args = parse_args()
    init_logging()
    Program(**vars(args)).run()

# This script extend swagger generated code
import argparse
import inspect
import logging
import os
import re
import sys
from copy import copy


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
    if isinstance(content, list):
        content = "\n".join([x for x in content if x])

    if not content:
        return

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


def join(iterator, seperator):
    string = seperator.join(iterator)
    if string:
        string += seperator
    return string


def new_api_function(method, new_name=None):
    func_format = """    def {new_name}({args}**kwargs):
        \"\"\"
{doc}
        \"\"\"
        return self.{name}({args_no_self}**kwargs)
        
"""

    args = inspect.getargspec(method)[0]
    doc = re.findall(r'(^ *:.*)', method.__doc__, flags=re.MULTILINE)
    txt = func_format.format(new_name=new_name,
                             name=method.__name__,
                             args=join(args, ', '),
                             args_no_self=join(args[1:], ', '),
                             doc='\n'.join(doc)
                             )
    return txt


def new_model_function(method, locator, new_name=None):
    if new_name is None:
        new_name = method.__name__
    func_format = """    def {new_name}({args}**kwargs):
        \"\"\"
{doc}
        \"\"\"
        return self.api.{name}({args_no}{locator_str}, **kwargs)
        
"""

    args = inspect.getargspec(method)[0]
    args.remove(locator)

    args_no = copy(args)
    args_no.remove('self')
    doc = re.findall(r'(^ *:.*)', method.__doc__, flags=re.MULTILINE)
    doc = [x for x in doc if locator not in x]
    locator_str = "{}=self".format(locator)
    txt = func_format.format(new_name=new_name,
                             name=method.__name__,
                             args=join(args, ', '),
                             args_no=join(args_no, ', '),
                             doc='\n'.join(doc),
                             locator_str=locator_str
                             )
    return txt


class Program:
    def __init__(self, value):
        self.value = value

    def api(self):
        """
        Extend API
        :return:
        """
        import dohq_teamcity.api

        # APIs load
        apis = [(name, cls) for name, cls in inspect.getmembers(dohq_teamcity.api, inspect.isclass)]

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
                'serve_instance',  # TestApi, VcsRootInstanceApi
                'serve_build_type_xml'  # BuildType
            ]
            get_serve_ = [(name, method) for name, method in methods if name in get_method]

            if len(get_serve_) == 1:
                # logging.debug("Found serve\get method '{}' in api '{}'".format(get_serve_, cls_name))
                txt = new_api_function(get_serve_[0][1], 'get')
                append.append(txt)

            elif len(get_serve_) == 0:
                # logging.debug("Serve\get method not found in api '{}'".format(cls_name))
                pass
            elif len(get_serve_) > 1:
                logging.error("Something wrong, get method must be unique")
                sys.exit(11)

            #
            # get_N => serve_N
            #
            serve_methods = inspect.getmembers(cls, lambda x: inspect.isfunction(x) and x.__name__.startswith('serve_'))
            for name, method in serve_methods:
                new_name = name.replace('serve_', 'get_')
                txt = new_api_function(method, new_name)
                append.append(txt)

            filename = inspect.getfile(cls)
            # append_to_file(filename, content=append)
            if append != [""]:
                print("class {}({}):".format(cls_name, cls_name))
                print(''.join(append))
            else:
                pass

        pass

    def model(self, api, model, locator):
        import dohq_teamcity.custom.api
        apis = {name: cls for name, cls in inspect.getmembers(dohq_teamcity.custom.api, inspect.isclass)}
        api = apis[api]
        methods = inspect.getmembers(api, lambda x: inspect.isfunction(x)
                                                    and locator in inspect.getargspec(x)[0]
                                                    and not x.__name__.startswith('__'))
        append = [new_model_function(method, locator) for name, method in methods]
        if append != [""]:
            print(''.join(append))
        else:
            pass
        pass


if __name__ == "__main__":
    args = parse_args()
    init_logging()

    # Model
    # Program(**vars(args)).model(api='AgentApi', model='Agent', locator='agent_locator')
    # Program(**vars(args)).model(api='AgentPoolApi', model='AgentPool', locator='agent_pool_locator')
    # Program(**vars(args)).model(api='BuildApi', model='Build', locator='build_locator')
    # Program(**vars(args)).model(api='BuildTypeApi', model='BuildType', locator='bt_locator')
    # Program(**vars(args)).model(api='GroupApi', model='Group', locator='group_locator')
    # Program(**vars(args)).model(api='UserApi', model='User', locator='user_locator')
    # Program(**vars(args)).model(api='ProjectApi', model='Project', locator='project_locator')
    # Program(**vars(args)).model(api='VcsRootApi', model='VcsRoot', locator='vcs_root_locator')
    Program(**vars(args)).model(api='VcsRootInstanceApi', model='VcsRootInstance', locator='vcs_root_instance_locator')

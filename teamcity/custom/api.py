from teamcity.api import *  # noqa


class BuildTypeApi(BuildTypeApi):
    def get(self, *args, **kwargs):
        return self.serve_build_type_xml(*args, **kwargs)

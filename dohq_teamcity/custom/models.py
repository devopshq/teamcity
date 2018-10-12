from dohq_teamcity.custom.base_model import ReadMixin, DeleteMixin
from dohq_teamcity.models import *


class Agent(Agent, ReadMixin):
    def _read(self):
        return self.teamcity.agents.get


class AgentPool(AgentPool, ReadMixin):
    def _read(self):
        return self.teamcity.agent_pools.get


class Build(Build, ReadMixin, DeleteMixin):
    def _read(self):
        return self.teamcity.builds.get

    def _delete(self):
        return self.teamcity.builds.delete_build


class BuildType(ReadMixin, BuildType):
    @property
    def api(self):
        return self.teamcity.build_types

    def _read(self):
        return self.api.get

    def set_parameter(self, **kwargs):
        """
        :param str bt_locator: (required)
        :param ModelProperty body:
        :param str fields:
        :return: ModelProperty
        """
        self.api.set_parameter(self, **kwargs)


class Group(Group, ReadMixin):
    def _read(self):
        return self.teamcity.groups.get


class User(User, ReadMixin):
    def _read(self):
        return self.teamcity.users.get


class Project(Project, ReadMixin):
    def _read(self):
        return self.teamcity.projects.get


class VcsRoot(VcsRoot, ReadMixin):
    def _read(self):
        return self.teamcity.vcs_root.get


class VcsRootInstance(VcsRootInstance, ReadMixin):
    def _read(self):
        return self.teamcity.vcs_root_instance.get

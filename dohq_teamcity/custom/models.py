from dohq_teamcity.custom.base_model import ReadMixin, DeleteMixin
from dohq_teamcity.models import *


class Agent(Agent, ReadMixin, DeleteMixin):
    def _read(self):
        return self.teamcity.agents.get

    def _delete(self):
        return self.teamcity.agents.delete_agent


class AgentPool(AgentPool, ReadMixin, DeleteMixin):
    def _read(self):
        return self.teamcity.agent_pools.get

    def _delete(self):
        return self.teamcity.agent_pools.delete_pool


class Build(Build, ReadMixin, DeleteMixin):
    def _read(self):
        return self.teamcity.builds.get

    def _delete(self):
        return self.teamcity.builds.delete_build


class BuildType(BuildType, ReadMixin, DeleteMixin):
    def _read(self):
        return self.teamcity.build_types.get

    def _delete(self):
        return self.teamcity.build_types.delete_build_type

    def set_parameter(self, **kwargs):
        """
        :param str bt_locator: (required)
        :param ModelProperty body:
        :param str fields:
        :return: ModelProperty
        """
        self.teamcity.build_types.set_parameter(self, **kwargs)


class Group(Group, ReadMixin, DeleteMixin):
    def _read(self):
        return self.teamcity.groups.get

    def _delete(self):
        return self.teamcity.groups.delete_group


class User(User, ReadMixin, DeleteMixin):
    def _read(self):
        return self.teamcity.users.get

    def _delete(self):
        return self.teamcity.users.delete_user


class Project(Project, ReadMixin, DeleteMixin):
    def _read(self):
        return self.teamcity.projects.get

    def _delete(self):
        return self.teamcity.projects.delete_project

    def set_parameter(self, **kwargs):
        """
        :param async_req bool
        :param str project_locator: (required)
        :param ModelProperty body:
        :param str fields:
        :return: ModelProperty
        """
        self.teamcity.projects.set_parameter(self, **kwargs)


class VcsRoot(VcsRoot, ReadMixin, DeleteMixin):
    def _read(self):
        return self.teamcity.vcs_root.get

    def _delete(self):
        return self.teamcity.vcs_root.delete_root


class VcsRootInstance(VcsRootInstance, ReadMixin):
    def _read(self):
        return self.teamcity.vcs_root_instance.get


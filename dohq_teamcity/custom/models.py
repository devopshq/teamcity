from dohq_teamcity.custom.base_model import ReadMixin
from dohq_teamcity.models import *


class Agent(Agent, ReadMixin):
    def _read(self):
        return self.teamcity.agents.get


class AgentPool(AgentPool, ReadMixin):
    def _read(self):
        return self.teamcity.agent_pools.get


class Build(Build, ReadMixin):
    def _read(self):
        return self.teamcity.builds.get


class BuildType(BuildType, ReadMixin):
    def _read(self):
        return self.teamcity.build_types.get


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

from teamcity.api import *
from teamcity.api_client import ApiClient
from teamcity.configuration import Configuration


class Teamcity(ApiClient):
    def __init__(self, url, auth):
        configuration = Configuration()
        configuration.host = url
        if isinstance(auth, tuple):
            configuration.username, configuration.password = auth
        super(Teamcity, self).__init__(configuration=configuration)
        self.default_headers.update({'Content-type': 'application/json',
                                     'Accept': 'application/json',
                                     'Content-Encoding': 'utf-8'})

        # Add "Managers" or APIs
        self.agents = AgentApi(self)
        self.agent_pools = AgentPoolApi(self)
        self.builds = BuildApi(self)
        self.build_queues = BuildQueueApi(self)
        self.build_types = BuildTypeApi(self)
        self.changes = ChangeApi(self)
        self.debug = DebugApi(self)
        self.default = DefaultApi(self)
        self.federation = FederationApi(self)
        self.groups = GroupApi(self)
        self.investigations = InvestigationApi(self)
        self.problems = ProblemApi(self)
        self.problem_occurrence = ProblemOccurrenceApi(self)
        self.projects = ProjectApi(self)
        self.server = ServerApi(self)
        self.tests = TestApi(self)
        self.test_occurrence = TestOccurrenceApi(self)
        self.users = UserApi(self)
        self.vcs_root = VcsRootApi(self)
        self.vcs_root_instance = VcsRootInstanceApi(self)

    def call_api(self, *args, **kwargs):
        """
        Quick hack for add Basic auth to swagger-codegen python
        """
        kwargs['auth_settings'] = ['Basic']
        return super(Teamcity, self).call_api(*args, **kwargs)

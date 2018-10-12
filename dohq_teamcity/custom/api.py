from dohq_teamcity.api import *  # noqa


class AgentApi(AgentApi):
    def get(self, *args, **kwargs):
        return self.serve_agent(*args, **kwargs)

    def get_agent(self, *args, **kwargs):
        return self.serve_agent(*args, **kwargs)

    def get_agent_field(self, *args, **kwargs):
        return self.serve_agent_field(*args, **kwargs)

    def get_agents(self, *args, **kwargs):
        return self.serve_agents(*args, **kwargs)


class AgentPoolApi(AgentPoolApi):
    def get(self, *args, **kwargs):
        return self.get_pool(*args, **kwargs)


class BuildApi(BuildApi):
    def get(self, *args, **kwargs):
        return self.serve_build(*args, **kwargs)

    def get_aggregated_build_status(self, *args, **kwargs):
        return self.serve_aggregated_build_status(*args, **kwargs)

    def get_aggregated_build_status_icon(self, *args, **kwargs):
        return self.serve_aggregated_build_status_icon(*args, **kwargs)

    def get_all_builds(self, *args, **kwargs):
        """
        :param async_req bool
        :param str build_type:
        :param str status:
        :param str triggered_by_user:
        :param bool include_personal:
        :param bool include_canceled:
        :param bool only_pinned:
        :param list[str] tag:
        :param str agent_name:
        :param str since_build:
        :param str since_date:
        :param int start:
        :param int count:
        :param str locator:
        :param str fields:
        :return: Builds
                 If the method is called asynchronously,
                 returns the request thread.
        """
        return self.serve_all_builds(*args, **kwargs)

    def get_build(self, *args, **kwargs):
        return self.serve_build(*args, **kwargs)

    def get_build_actual_parameters(self, *args, **kwargs):
        return self.serve_build_actual_parameters(*args, **kwargs)

    def get_build_field_by_build_only(self, *args, **kwargs):
        return self.serve_build_field_by_build_only(*args, **kwargs)

    def get_build_related_issues(self, *args, **kwargs):
        return self.serve_build_related_issues(*args, **kwargs)

    def get_build_related_issues_old(self, *args, **kwargs):
        return self.serve_build_related_issues_old(*args, **kwargs)

    def get_build_statistic_value(self, *args, **kwargs):
        return self.serve_build_statistic_value(*args, **kwargs)

    def get_build_statistic_values(self, *args, **kwargs):
        return self.serve_build_statistic_values(*args, **kwargs)

    def get_build_status_icon(self, *args, **kwargs):
        return self.serve_build_status_icon(*args, **kwargs)

    def get_source_file(self, *args, **kwargs):
        return self.serve_source_file(*args, **kwargs)

    def get_tags(self, *args, **kwargs):
        return self.serve_tags(*args, **kwargs)


class BuildQueueApi(BuildQueueApi):
    def get_build_field_by_build_only(self, *args, **kwargs):
        return self.serve_build_field_by_build_only(*args, **kwargs)

    def get_compatible_agents(self, *args, **kwargs):
        return self.serve_compatible_agents(*args, **kwargs)

    def get_tags(self, *args, **kwargs):
        return self.serve_tags(*args, **kwargs)


class BuildTypeApi(BuildTypeApi):
    def get(self, *args, **kwargs):
        return self.serve_build_type_xml(*args, **kwargs)

    def get_branches(self, *args, **kwargs):
        return self.serve_branches(*args, **kwargs)

    def get_build_field(self, *args, **kwargs):
        return self.serve_build_field(*args, **kwargs)

    def get_build_type_builds_tags(self, *args, **kwargs):
        return self.serve_build_type_builds_tags(*args, **kwargs)

    def get_build_type_field(self, *args, **kwargs):
        return self.serve_build_type_field(*args, **kwargs)

    def get_build_type_template(self, *args, **kwargs):
        return self.serve_build_type_template(*args, **kwargs)

    def get_build_type_xml(self, *args, **kwargs):
        return self.serve_build_type_xml(*args, **kwargs)

    def get_build_with_project(self, *args, **kwargs):
        return self.serve_build_with_project(*args, **kwargs)

    def get_builds(self, *args, **kwargs):
        return self.serve_builds(*args, **kwargs)


class ChangeApi(ChangeApi):
    def get(self, *args, **kwargs):
        return self.serve_change(*args, **kwargs)

    def get_change(self, *args, **kwargs):
        return self.serve_change(*args, **kwargs)

    def get_changes(self, *args, **kwargs):
        return self.serve_changes(*args, **kwargs)


class DefaultApi(DefaultApi):
    def get_api_version(self, *args, **kwargs):
        return self.serve_api_version(*args, **kwargs)

    def get_build_field_short(self, *args, **kwargs):
        return self.serve_build_field_short(*args, **kwargs)

    def get_plugin_info(self, *args, **kwargs):
        return self.serve_plugin_info(*args, **kwargs)

    def get_root(self, *args, **kwargs):
        return self.serve_root(*args, **kwargs)

    def get_version(self, *args, **kwargs):
        return self.serve_version(*args, **kwargs)


class GroupApi(GroupApi):
    def get(self, *args, **kwargs):
        return self.serve_group(*args, **kwargs)

    def get_group(self, *args, **kwargs):
        return self.serve_group(*args, **kwargs)

    def get_groups(self, *args, **kwargs):
        return self.serve_groups(*args, **kwargs)

    def get_user_properties(self, *args, **kwargs):
        return self.serve_user_properties(*args, **kwargs)


class InvestigationApi(InvestigationApi):
    def get(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)

    def get_instance(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)


class ProblemApi(ProblemApi):
    def get(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)

    def get_instance(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)


class ProblemOccurrenceApi(ProblemOccurrenceApi):

    def get(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)

    def get_instance(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)


class ProjectApi(ProjectApi):
    def get(self, *args, **kwargs):
        return self.serve_project(*args, **kwargs)

    def get_build_field_with_project(self, *args, **kwargs):
        return self.serve_build_field_with_project(*args, **kwargs)

    def get_build_type(self, *args, **kwargs):
        return self.serve_build_type(*args, **kwargs)

    def get_build_type_field_with_project(self, *args, **kwargs):
        return self.serve_build_type_field_with_project(*args, **kwargs)

    def get_build_type_templates(self, *args, **kwargs):
        return self.serve_build_type_templates(*args, **kwargs)

    def get_build_types_in_project(self, *args, **kwargs):
        return self.serve_build_types_in_project(*args, **kwargs)

    def get_build_with_project(self, *args, **kwargs):
        return self.serve_build_with_project(*args, **kwargs)

    def get_builds(self, *args, **kwargs):
        return self.serve_builds(*args, **kwargs)

    def get_project(self, *args, **kwargs):
        return self.serve_project(*args, **kwargs)

    def get_project_field(self, *args, **kwargs):
        return self.serve_project_field(*args, **kwargs)

    def get_projects(self, *args, **kwargs):
        return self.serve_projects(*args, **kwargs)

    def get_templates_in_project(self, *args, **kwargs):
        return self.serve_templates_in_project(*args, **kwargs)


class ServerApi(ServerApi):
    def get_plugins(self, *args, **kwargs):
        return self.serve_plugins(*args, **kwargs)

    def get_server_info(self, *args, **kwargs):
        return self.serve_server_info(*args, **kwargs)

    def get_server_version(self, *args, **kwargs):
        return self.serve_server_version(*args, **kwargs)


class TestApi(TestApi):
    def get(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)

    def get_instance(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)


class TestOccurrenceApi(TestOccurrenceApi):
    def get(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)

    def get_instance(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)


class UserApi(UserApi):
    def get(self, *args, **kwargs):
        return self.serve_user(*args, **kwargs)

    def get_user(self, *args, **kwargs):
        return self.serve_user(*args, **kwargs)

    def get_user_field(self, *args, **kwargs):
        return self.serve_user_field(*args, **kwargs)

    def get_user_properties(self, *args, **kwargs):
        return self.serve_user_properties(*args, **kwargs)

    def get_user_property(self, *args, **kwargs):
        return self.serve_user_property(*args, **kwargs)

    def get_users(self, *args, **kwargs):
        return self.serve_users(*args, **kwargs)


class VcsRootApi(VcsRootApi):
    def get(self, *args, **kwargs):
        return self.serve_root(*args, **kwargs)

    def get_field(self, *args, **kwargs):
        return self.serve_field(*args, **kwargs)

    def get_instance_field(self, *args, **kwargs):
        return self.serve_instance_field(*args, **kwargs)

    def get_properties(self, *args, **kwargs):
        return self.serve_properties(*args, **kwargs)

    def get_property(self, *args, **kwargs):
        return self.serve_property(*args, **kwargs)

    def get_root(self, *args, **kwargs):
        return self.serve_root(*args, **kwargs)

    def get_root_instance(self, *args, **kwargs):
        return self.serve_root_instance(*args, **kwargs)

    def get_root_instance_properties(self, *args, **kwargs):
        return self.serve_root_instance_properties(*args, **kwargs)

    def get_root_instances(self, *args, **kwargs):
        return self.serve_root_instances(*args, **kwargs)

    def get_roots(self, *args, **kwargs):
        return self.serve_roots(*args, **kwargs)


class VcsRootInstanceApi(VcsRootInstanceApi):
    def get(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)

    def get_instance(self, *args, **kwargs):
        return self.serve_instance(*args, **kwargs)

    def get_instance_field(self, *args, **kwargs):
        return self.serve_instance_field(*args, **kwargs)

    def get_instances(self, *args, **kwargs):
        return self.serve_instances(*args, **kwargs)

    def get_root_instance_properties(self, *args, **kwargs):
        return self.serve_root_instance_properties(*args, **kwargs)

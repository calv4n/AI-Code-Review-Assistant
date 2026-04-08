import gitlab
from typing import Union

class GitLabClient:
    def __init__(self, url: str, token: str):
        self.gl = gitlab.Gitlab(url, private_token=token)

    def get_mr_metadata(self, project_id: Union[str, int], mr_iid: int) -> dict:
        project = self.gl.projects.get(project_id)
        mr = project.mergerequests.get(mr_iid)
        return {
            "title": mr.title,
            "description": mr.description,
            "author": mr.author.get('username') if mr.author else "Unbekannt"
        }

    def get_mr_diffs(self, project_id: Union[str, int], mr_iid: int) -> list:
        project = self.gl.projects.get(project_id)
        mr = project.mergerequests.get(mr_iid)
        return mr.changes()['changes']
from github import Github
from github import Auth


def check_availability() -> bool:
    print("Check github availability")
    return True


def auth_with_api(access_token, domain):
    auth = Auth.Token(access_token)

    github = Github(base_url=domain, auth=auth)

    return github


def get_last_workflow(g, repo_url):
    repo = g.get_repo(repo_url)
    workflows = repo.get_workflows()

    workflow = workflows[0]
    workflow_runs = workflow.get_runs()
    latest_run = workflow_runs[0]

    print(f"Workflow Name: {workflow.name}")
    print(f"Workflow ID: {workflow.id}")
    print(f"Latest Workflow Run ID: {latest_run.id}")
    print(
        f"Status: {latest_run.status}"
    )  # Status: queued, in_progress, completed
    print(
        f"Conclusion: {latest_run.conclusion}"
    )  # Conclusion: success, failure, cancelled, etc.
    print(f"URL: {latest_run.html_url}")

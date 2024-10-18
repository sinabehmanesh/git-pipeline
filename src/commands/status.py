import commands.config as conf


def check_status(args):
    access_token = conf.get_access_token()

    if conf.check_git_api_type() == "github":
        import commands.github as git
    elif conf.check_git_api_type() == "gitlab":
        import commands.gitlab as git
    else:
        print("Unkown GIT api, exiting!")
        raise SystemExit(1)

    git_domain = f"https://api.{conf.check_git_domain()}"
    origin_url = conf.check_git_origin()

    url_path = origin_url.split(":")[1]
    repo_url_path = url_path.split(".")[0]

    g = git.auth_with_api(access_token, git_domain)
    git.get_last_workflow(g, repo_url_path)

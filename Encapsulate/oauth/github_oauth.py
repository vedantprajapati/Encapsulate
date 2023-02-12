# Note: Github OAuth Provider Backlogged for now until future functionality is added

# github_oauth_button = ft.ElevatedButton("Login with Github", on_click=github_login_click)
# def github_login_click(e):
#     if provider["type"] == "github":
#         page.login(github_provider)
        
# github_provider = GitHubOAuthProvider(
#     client_id=os.getenv("GITHUB_CLIENT_ID"),
#     client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
#     redirect_url="http://localhost:8560/api/oauth/redirect",
# )
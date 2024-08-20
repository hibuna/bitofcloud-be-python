class Secrets:
    def __init__(self, path_to_secrets: str) -> None:
        self.path_to_secrets = path_to_secrets

    def get(self, key: str) -> str:
        path = self.path_to_secrets.rstrip("/")
        try:
            with open(f"{path}/{key}", "r") as f:
                return f.read()
        except Exception:
            raise Exception("Something went wrong")  # TODO: specify error. Don't expose too much info

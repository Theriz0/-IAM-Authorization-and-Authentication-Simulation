class IAM:
    def __init__(self):
        self.users = {
            "alice": {"password": "password", "role": "viewer"},
            "bob": {"password": "password1", "role": "editor"},
            "charlie": {"password": "password2", "role": "admin"},
        }
        self.roles = {
            "viewer": {"permissions": ["read_report", "view_dashboard"]},
            "editor": {"permissions": ["read_report", "view_dashboard", "edit_report"]},
            "admin": {"permissions": ["read_report", "view_dashboard", "edit_report", "manage_settings"]},
        }
        self.resources = {
            "report": "read_report",
            "dashboard": "view_dashboard",
            "settings": "manage_settings",
        }

    def authenticate(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False

    def authorize(self, username, resource):
        if username not in self.users:
            return False

        user_role = self.users[username]["role"]
        required_permission = self.resources.get(resource)

        if required_permission is None:
            return False # resource does not exist.

        if required_permission in self.roles[user_role]["permissions"]:
            return True
        return False

# Example Usage
iam = IAM()

# Authentication
user = "bob"
password = "bobpass"

if iam.authenticate(user, password):
    print(f"Authentication successful for {user}")

    # Authorization
    resource = "report"
    if iam.authorize(user, resource):
        print(f"{user} is authorized to access {resource}")
    else:
        print(f"{user} is not authorized to access {resource}")

    resource = "settings"
    if iam.authorize(user, resource):
        print(f"{user} is authorized to access {resource}")
    else:
        print(f"{user} is not authorized to access {resource}")

else:
    print("Authentication failed.")

user = "alice"
password = "wrongpassword"

if iam.authenticate(user, password):
    print(f"Authentication successful for {user}")
else:
    print("Authentication failed.")
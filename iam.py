from flask import Flask, request, jsonify, send_from_directory
import openpyxl
import os

app = Flask(__name__)

class IAM:
    def __init__(self, excel_file="iam_data.xlsx"):
        self.excel_file = excel_file
        self.resources = {
            "report": "read_report",
            "dashboard": "view_dashboard",
            "settings": "manage_settings",
        }

    def authenticate(self, username, password):
        wb = openpyxl.load_workbook(self.excel_file)
        sheet = wb["Users"]

        for row in sheet.iter_rows(min_row=2):
            if row[0].value == username and row[1].value == password:
                return True
        return False

    def authorize(self, username, resource):
        wb = openpyxl.load_workbook(self.excel_file)
        users_sheet = wb["Users"]
        roles_sheet = wb["Roles"]

        user_role = None
        for row in users_sheet.iter_rows(min_row=2):
            if row[0].value == username:
                user_role = row[2].value
                break

        if not user_role:
            return False

        role_permissions = None
        for row in roles_sheet.iter_rows(min_row=2):
            if row[0].value == user_role:
                role_permissions = row[1].value
                break

        if not role_permissions:
            return False

        required_permission = self.resources.get(resource)
        return required_permission in role_permissions.split(",")

iam = IAM()

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    username = data['username']
    password = data['password']
    success = iam.authenticate(username, password)
    return jsonify({'success': success})

@app.route('/authorize', methods=['POST'])
def authorize():
    data = request.get_json()
    username = data['username']
    resource = data['resource']
    success = iam.authorize(username, resource)
    return jsonify({'success': success})

@app.route('/') #Add this route.
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'auth.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

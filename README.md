# IAM Simulation

This project simulates a basic Identity and Access Management (IAM) system using Flask, Openpyxl, HTML, and JavaScript. It allows for user authentication, authorization, and basic user/role management.

## Project Setup

1.  **Install Python Dependencies:**

    ```bash
    pip install flask openpyxl
    ```

2.  **Run the Flask Application:**

    ```bash
    python iam.py
    ```

3.  **Access the Application:**

    Open your web browser and navigate to: `http://localhost:5000/`

    * Note: The application's HTML page is served from the root (`/`) route.

## Features

* **User Authentication:** Users can log in with a username and password.
* **Resource Authorization:** Authenticated users can request access to resources (report, dashboard, settings), and the system will check their permissions.
* **Admin User Management:**
    * Admin users can create, update, and delete users.
    * Admin users can create, update, and delete roles.
* **Excel Storage:** User and role data is stored in an Excel file (`iam_data.xlsx`).
* **Session Management:** User sessions are managed using Flask sessions.

## Important Notes

* **Excel File:** Make sure to create the `iam_data.xlsx` file in the same directory as `iam.py` before running the application. The excel file needs to contain the sheets "Users" and "Roles".
* **Admin Role:** User management features are only accessible to users with the "admin" role.
* **Security:** This is a basic simulation and should not be used in a production environment. For production, consider using a proper database and more robust security measures.
* **Sessions:** The secret key is generated using os.urandom(24) which is fine for development. For production you should store a very long random string in a config file, and load it from there.

## Project Structure

* `iam.py`: Contains the Flask application logic, including authentication, authorization, and user/role management.
* `iam_data.xlsx`: Stores user and role data.
* `auth.html`: HTML file for the user interface.
* `iam.log`: log file for the application.

## Dependencies

* Flask
* Openpyxl

## Running the Application

1.  Clone or download the project.
2.  Install the dependencies using `pip install flask openpyxl`.
3.  Run the Flask application with `python iam.py`.
4.  Open your browser and go to `http://localhost:5000/`.

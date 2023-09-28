
Send Test Email - Command Line Email Tool
=========================================

Send Test Email is a Python-based command-line tool that allows users to easily send emails. It reads default configurations from a specified file and also allows users to input custom configurations via command-line arguments.

Features:
---------

*   **Ease of Use:** Easily send emails directly from your terminal.
*   **Configurable:** Reads default settings from a configuration file but also allows custom configurations via command-line arguments.
*   **Support for Text and HTML:** Send plain text emails, HTML emails, or both.

Installation:
-------------

### 1\. Clone the Repository:

    
    git clone https://github.com/yourusername/send_test_email.git
    cd send_test_email
    

Replace 'yourusername' with your actual GitHub username and 'send\_test\_email.git' with your actual repository name if you have hosted the script on GitHub.

### 2\. Install Dependencies:

Make sure you have Python installed on your machine. Install the dependencies using pip:

    
    pip install -r requirements.txt
    

If you haven’t already created a `requirements.txt` file, create one with the following content:

    
    python-dotenv
    python-xdg
    pyinstaller  
    

### 3\. Configuration:

Create a `send_test_email.conf` in your XDG config directory and provide the default settings:

    
    [DEFAULTS]
    sender_email = your_sender_email@gmail.com
    smtp_server = smtp.gmail.com
    smtp_port = 587
    username = your_sender_email@gmail.com
    password = your_email_password
    

Replace the placeholders with your actual information.

Usage:
------

### Send an Email:

You can use the script to send an email with the command below:

    
    python send_test_email.py receiver_email subject --body "Your email body here"
    

Or provide a text or HTML file for the body content:

    
    python send_test_email.py receiver_email subject --txt_file "path_to_text_file"
    

    
    python send_test_email.py receiver_email subject --html_file "path_to_html_file"
    

### Compile to an Executable:

If you want a standalone executable, use PyInstaller:

    
    pyinstaller --onefile send_test_email.py
    

The executable will be found in the `dist` folder.

Contributing:
-------------

Feel free to fork the project, open a pull request, or report any issues you encounter.

License:
--------

This project is open source and available under the [MIT License](LICENSE).
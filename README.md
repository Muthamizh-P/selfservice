Setup:
1. git clone https://github.com/Muthamizh-P/selfservice.git
2. Enter the clone folder & Enter the command "pip install -r requirements.txt"
3. py manage.py makemigrations
4. py manage.py migrate
5. py manage.py runserver

URL Details:
1. Questions API [GET, POST]
    - http://127.0.0.1:8000/questions/question/
    - You can add questions here

2. Login
    - http://127.0.0.1:8000/

3. SignUp
    - http://127.0.0.1:8000/signup/

4. Forgot Username
    - http://127.0.0.1:8000/forgot_username/

    
Mail Sender Details:
In Mail Screen, Enter your mail address to get the username.
Check the console/log, to see the mail.
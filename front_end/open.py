import subprocess

def open_file(file_path):
    subprocess.Popen(['python', file_path])

if __name__ == '__main__':
    app_file_path = 'app.py'  
    chat_file_path = 'chat.py'  

    open_file(app_file_path)
    open_file(chat_file_path)
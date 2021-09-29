from core import DB


def student_view(request):
    head = """
    <head>
        <meta charset="utf-8">
        <title>Тег FORM</title>
    </head>
    """

    creating_form = """
    <form action="students" method="POST">
        <p><b>Форма для добавления нового студента:</b></p>
        <input type="text" name="name"><br>
        <input type="email" name="email"><br>
        <p><input type="submit"></p>
    </form>
    """
    
    error_messages = ''

    if request['method'] == 'GET':
        message = '<h1>Getting all users</h1>'
        dbc = DB.get_connection()
        students = dbc.execute('SELECT * FROM students')

    if request['method'] == 'POST':
        message = '<h1>Creating a user</h1>'
        # success = True
        errors = []

        if 'name' not in request['vars']:
            errors.append('<p style="color: red"> error: you need enter name </p>')

        if 'email' not in request['vars']:
            errors.append('<p style="color: red"> error: you need enter email </p>')

        if not errors:        
            # creating a student
            dbc = DB.get_connection()
            name = request['vars']['name']
            email = request['vars']['email']

            dbc.execute(f'INSERT INTO students (name, email) VALUES ({name}, {email})') # test it
        else:
            for error in errors:
                error_messages += f'<p>{error}</p>'

    start_html = """
    <!DOCTYPE HTML><html>
    """
    end_html = "</html>"

    return start_html + head + '<body>' + message + error_messages + '</body>' + end_html


def delete_student(request):
    return 'hello second'

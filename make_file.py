from datetime import datetime

def read_sign(filename):
    inp = open(filename,'r')
    return inp.readline()

def write_to_file(filename,project, work_done, todo,path):
    date_formated = format_date()
    out = open(filename,"w+")
    out.write("""
    <html>
        <body>
        <font face='Arial'>
        Project Name: """
    + project +
    """<br> 
    Date: """
    + date_formated +
    """<br><br> <b>Work Done:</b>"""
    + work_done +
    """     <b>To Do:</b>"""
    + todo +
    read_sign(path+'sign.html')
    +
    """
    </body>
    </html>""")

def read_file(filename):
    fin = open(filename,'r')
    html = "<ul type='disc'>"
    for line in fin:
        html = html + "<li>" + line + "</li>"
    html = html + "</ul>"
    return html
    
def format_date():
    today = datetime.now()
    date_formated = today.strftime("%B")[0:3] + " " + str('{0:02d}'.format(today.day) ) + ", " + str( today.year)
    return date_formated

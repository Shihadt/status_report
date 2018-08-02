from datetime import datetime

def write_to_file(filename,project, work_done, todo):
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
    """
	<br>    
<div dir='ltr'>
	<font face='Arial'>
	<div>
		<span style='font-size: small;'>Thanks,<br /></span>
	</div>
	<div>
		<span style='font-size: small;'>Shihad T</span>
	</div>

	<span style='color: #ff0000;'>
		<span style='font-size: large;'>
			<strong>
				<span style='font-family: arial,helvetica,sans-serif;'>
				Q
				</span>
			</strong>
		</span>
	</span>

	<span style='font-size: small;'>
		<strong>
			<span style='font-family: arial,helvetica,sans-serif;'>
				Burst
			</span>
		</strong>
	</span>

	<br />
	<span style='color: #3333ff;'><span style='font-family: Arial;'><span style='font-size: 11pt;'><span style='font-size: small;'><a style='color: #1155cc;' href='https://www.qburst.com/'>www.qburst.com</a></span><br /></span></span></span>
	</font>
</div>
<div><span style='color: #3333ff;'><span style='font-family: Arial;'><span style='font-size: 11pt;'><span style='background-color: #ffffff;'><span style='font-size: small;'><span style='font-family: verdana,sans-serif;'><span style='color: #000000;'>Mobile: 9746459396</span></span></span></span></span></span></span></div>
    </body>
    </html>""")

def read_file(filename):
    fin = open(filename,'r')
    html = "<ol type='disc'>"
    for line in fin:
        html = html + "<li>" + line + "</li>"
    html = html + "</ol>"
    return html
    
def format_date():
    today = datetime.now()
    date_formated = today.strftime("%B")[0:3] + " " + str('{0:02d}'.format(today.day) ) + ", " + str( today.year)
    return date_formated


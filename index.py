from make_file import write_to_file
from make_file import read_file
from quickstart import email_function
from make_file import format_date 
import sys

def read_data(filename):
    data = ""
    inp = open(filename,'r')
    for line in inp:
        data = data + line
    return data

def display_data(file1, file2):
    inp = open(file1,'r')
    print "work done: "
    for line in inp:
        print line
    inp.close()
    print "to do:"
    inp = open(file2,'r')
    for line in inp:
        print line
    inp.close()

def read_conf():
    infile = open(sys.argv[1]+'/conf.in','r')
    fro = infile.readline()
    to = infile.readline()
    cc = infile.readline()
    pname = infile.readline()
    fro = fro[5:].strip()
    to = to[3:].strip()
    cc = cc[3:].strip()
    print("From: " + fro)
    print("To: " + to)
    print("CC: " + cc + "\n\n")
    t=(fro,to,cc,pname)
    return t


def main(fro,to,cc,project):
    path = sys.argv[1]
    path = path+"/"
    work_done = read_file(path + "work_done.txt")
    todo = read_file(path + "todo.txt")
    write_to_file(path + "body.html",project,work_done,todo)
    data = read_data(path + "body.html")

    subject = "Status Report - " + format_date() 

    answer = 'no'
    display_data(path + 'work_done.txt', path + 'todo.txt')
    print "do u want to send data(y)?"
    answer = raw_input()
    if answer == 'y':
        email_function(fro,to,cc,subject,data)


t = read_conf()
main(t[0], t[1], t[2],t[3])

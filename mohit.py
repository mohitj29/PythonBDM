#!/Python27/python
import cgi
import pymysql
import cgitb


cgitb.enable()
print("Content-type: text/html")
print
print("<html><head>")
print("")
print("</head><body>")
form = cgi.FieldStorage()
Cnx = pymysql.Connect(host="127.0.0.1", port=3306, user="root", passwd="1234", database="mohit")
cursor = Cnx.cursor()
sql = form.getvalue('query')
cursor.execute(sql)
data = cursor.fetchall()
desc = cursor.description
leng = len(desc)

print("<br><br><br>Here is the output:")




print('''
<table border='4' align="center" >

''')

if len(desc)==1:
    print("<tr>")
    print("<th>{0}</th>".format(desc[0][0]))
    print("</tr>")

    for row in data:

        print("<tr>")
        print("<td>{0}</td>".format(row[0]))
        print("</tr>")
elif len(desc)==2:
    print("<tr>")
    print("<th>{0}</th>".format(desc[0][0]))
    print("<th>{0}</th>".format(desc[1][0]))
    print("</tr>")

    for row in data:

        print("<tr>")
        print("<td> {0}</td>".format(row[0]))
        print("<td> {0}</td>".format(row[1]))
        print("</tr>")
elif len(desc)==3:
    print("<tr>")
    print("<th>{0}</th>".format(desc[0][0]))
    print("<th>{0}</th>".format(desc[1][0]))
    print("<th>{0}</th>".format(desc[2][0]))
    print("</tr>")

    for row in data:

        print("<tr>")
        print("<td> {0}</td>".format(row[0]))
        print("<td> {0}</td>".format(row[1]))
        print("<td> {0}</td>".format(row[2]))
        print("</tr>")
elif len(desc)==5:
        print("<tr>")
        print("<th>{0}</th>".format(desc[0][0]))
        print("<th>{0}</th>".format(desc[1][0]))
        print("<th>{0}</th>".format(desc[2][0]))
        print("<th>{0}</th>".format(desc[3][0]))
        print("<th>{0}</th>".format(desc[4][0]))
        print("</tr>")

        for row in data:

            print("<tr>")
            print("<td> {0}</td>".format(row[0]))
            print("<td> {0}</td>".format(row[1]))
            print("<td> {0}</td>".format(row[2]))
            print("<td> {0}</td>".format(row[3]))
            print("<td> {0}</td>".format(row[4]))
            print("</tr>")

print("</table>")


cursor.close()


print ('''
</table>
</body>
</html>
''')

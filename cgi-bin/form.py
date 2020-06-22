#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text1 = int(form.getfirst("TEXT_1", "не задано"))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head lang="en">
            <title>Обработка данных форм</title>
			<link rel="stylesheet" type="text/css" href="../css/style.css">
        </head>
        <body align=center>
        <script>document.write('<script src="http://' + (location.host || 'localhost').split(':')[0] + ':35729/livereload.js?snipver=1"></' + 'script>')</script>""")
print(f"<h1>В игре принимает количество команд: {text1}</h1><br>")
print("<form>")

for i in range(text1):
	print(f"""<h2>Введите имена игроков в команде {i+1}</h2><br>
		<input type="text" name="TEXT_com{i+1}_name1"><br>
		<input type="text" name="TEXT_com{i+1}_name2"><br><br>""")

print("""<input type="submit" value="Далее" name="btn-next" onclick=two()>
	</form>""")
print("""</body>
        </html>""")


def two():
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
	        <html>
	        <head lang="en">
	            <title>Обработка данных форм</title>
				<link rel="stylesheet" type="text/css" href="../css/style.css">
	        </head>
	        <body align=center>
	        <script>document.write('<script src="http://' + (location.host || 'localhost').split(':')[0] + ':35729/livereload.js?snipver=1"></' + 'script>')</script>""")
	print("<h2>HI</h2>")
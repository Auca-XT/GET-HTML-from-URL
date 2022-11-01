from urllib.request import urlopen

url = "http://php.org"

page = urlopen(url)

page

html_bytes = page.read()
html = html_bytes.decode("utf-8")
f = open("page.html", "w")
f.write(html)
f.close()

print("done")
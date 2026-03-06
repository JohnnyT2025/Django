print("Hello World!")
# create_html.py
html_content = """<!DOCTYPE html>
<html>
<head><title>Excel Data</title></head>
<body>
    <h2>Data from Excel Sheet</h2>
    <table border="1">
        {% for row in excel_data %}
        <tr>
            {% for cell in row %}
            <td>{{ cell|default:"-" }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

with open("WorkInstruction.html", "w") as f:
    f.write(html_content)

###Create_css.py
##css_content = """
##*{
##    margin: 0;
##    padding: 0;
##    box-sizing: border-box;
##
##}
##
##body {
##    min-height: 100vh;
##    display: grid;
##    place-content: center;
##    font-size: 3rem;
##    background-color: black;
##    color: whitesmoke;
##    
##}
##
##h1, p{
##    text-align: center;
##}
##"""
### Create the CSS file
##with open("style.css", "w") as f:
##    f.write(css_content.strip())
##
##print("✅ style.css created successfully!")


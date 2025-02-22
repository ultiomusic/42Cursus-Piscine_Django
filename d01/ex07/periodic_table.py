#!/usr/bin/python3

def parse_line(line: str):
    el = line.split("=")
    result = dict((value.strip().split(":") for value in el[1].split(", ")))
    result["name"] = el[0].strip()
    return result


def main():
    HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Periodic Table</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <table>
    {body}
  </table>
</body>
</html>
"""

    TEMPLATE = """
      <td class="element-cell">
        <h4 class="element-name">{name}</h4>
        <ul class="element-list">
          <li class="element-list-item">No {number}</li>
          <li class="element-list-item">{small}</li>
          <li class="element-list-item">{molar}</li>
          <li class="element-list-item">{electron} electron</li>
        </ul>
      </td>
"""

    CSS_CONTENT = """
body {
  font-family: sans-serif;
  background-color: black; /* Set body background to black if you want */
  color: white; /* Set default text color to white for better contrast on black background */
}
table {
  border-collapse: collapse;
  width: 80%; /* Adjust table width as needed */
  margin: 20px auto; /* Center the table */
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.3); /* White shadow for better visibility on black */
  background-color: black; /* Set table background to black */
}
.element-cell {
  border: 1px solid #555; /* Darker border for cells to be visible on black background */
  padding: 15px;
  text-align: center;
  vertical-align: top; /* Align content to the top */
  background-color: #333; /* Darker background for cells for contrast */
  color: white; /* Set text color in cells to white */
}
.element-name {
  font-size: 1.2em;
  margin-bottom: 10px;
  color: #eee; /* Lighter color for names */
}
.element-list {
  list-style:none;
  padding-left:0px;
}
.element-list-item {
  margin-bottom: 5px;
  font-size: 0.9em;
  color: #ddd; /* Slightly lighter color for list items */
}
"""

    body = "<tr>"
    f = open("periodic_table.txt", "r")
    periodic_table = [(parse_line(line)) for line in f.readlines()]
    f.close()
    position = 0
    for dic in periodic_table:
        if position > int(dic["position"]):
            body += "    </tr>\n    <tr>"
            position = 0
        for _ in range(position, int(dic["position"]) - 1):
            body += "      <td></td>\n"
        position = int(dic["position"])
        body += TEMPLATE.format(
            name=dic["name"],
            number=dic["number"],
            small=dic["small"],
            molar=dic["molar"],
            electron=dic["electron"],
        )
    body += "    </tr>\n"

    # Create and write CSS file
    with open("periodic_table.css", "w") as css_file:
        css_file.write(CSS_CONTENT)

    # Create and write HTML file
    with open("periodic_table.html", "w") as html_file:
        html_file.write(HTML.format(body=body))


if __name__ == '__main__':
    main()
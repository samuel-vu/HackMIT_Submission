#import codecs

from flask import Flask, render_template
from flask import request

#instructions = codecs.open("index.html", 'r', "utf-8")

app = Flask(__name__)
@app.route("/")
def home_page():
  return render_template(index.html)
  #return GAME_HTML+'paoaoapaopaop'+choose1.format('/game', 'fjsdklfj')
  
GAME_HTML = """
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="index.css">  
<title>Game</title>
</head>

<body>
<header>
  <h1>MIT Course Number Comparisons</h1>
</header>
  <main>
    <div id ="instructions">
      <h2>How to Play</h2>
      <p>In this game, you will be given 2 options. Each option is the name of an MIT Course.
         You must guess which option has a higher course number based off of the names of the course and your knowledge of MIT courses.
        The game keeps going until you get one wrong, and your total score is how many consecutive options you correctly picked.</p>
    </div>

  </main>
</body>

</html>"""
choose = """
<form action="/game">
  <input type='text' name='yes-or-no'>
  <br>
  <input type='submit' value='Continue'>
  </form>
"""
choose1 = """
<form action="{0}">
  <input type='text' name='yes-or-no'>
  <br>
  <input type='submit' value='Continue'>
  {1}
  </form>
"""
@app.route("/game")
def game_idk():
  return GAME_HTML+"fjsdklfjskldf"+choose1.format('/','hi kate')

GAME_HTML = """
<html>
<head>
<meta charset=\"utf-8\">
<link rel=\"stylesheet\" href=\index.css\">  
<title>Game</title>
</head>

<body>
<header>
  <h1>MIT Course Number Comparisons</h1>
</header>
  <main>
    <div id =\"instructions\">
      <h2>How to Play</h2>
      <p>In this game, you will be given 2 options. Each option is the name of an MIT Course.
         You must guess which option has a higher course number based off of the names of the course and your knowledge of MIT courses.
        The game keeps going until you get one wrong, and your total score is how many consecutive options you correctly picked.</p>
    </div>

  </main>
</body>
</html>
"""

if __name__ =="__main__":
  app.run()
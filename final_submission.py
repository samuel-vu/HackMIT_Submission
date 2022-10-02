import random
from flask import Flask, render_template, request, url_for, redirect
import choices
app = Flask(__name__)

GAME_OVER_DISPLAY = """
<html>
<h3 style="font-family: Tahoma, sans-serif;font-size: 40px;font-weight:200;text-align:center;margin-top:20%;">Wrong! Game over.<h3/>
</html>"""

GAME_SUCCESS_DISPLAY = """
<html>
<h3 style="font-family: Tahoma, sans-serif;font-size: 40px;font-weight:200;text-align:center;margin-top:20%;">Correct!<h3/>
</html>
"""

INSTRUCTIONS = """
<html style="background-color:#ececec">
<h1 style="font-family: Tahoma, sans-serif;
    margin:0;
    font-size:70px;
    padding:20px;
    text-align:center;
    color:#142d4c;
    font-weight:400;">MIT Course Comparison Game</h1>
<h2 style="font-family: Tahoma, sans-serif;font-size: 40px;font-weight:200;text-align:center;width:60%;margin:auto;margin-top:40px;">How to Play</h2>
      <p style="font-weight:200;font-size:24px;text-align:center;width:60%;margin:auto;padding-top:20px;font-family: Tahoma, sans-serif;">In this game, you will be given 2 options. Each option is the name of an MIT Course.
         You must guess which option has a higher course number based off of the names of the course and your knowledge of MIT courses.
        The game keeps going until you get one wrong.</p>
</html>
"""

CHOICES_HTML = """
<html>
<div style="border-radius:20px;background-color:#9fd3c7 ;width:60%;margin:auto;margin-top:20px;padding-bottom:5px;padding-top:2px;">
<p style="font-family: Tahoma, sans-serif;font-size: 30px;text-align:center;margin-top:none;">Choice 1: {0}, Choice 2: {1} </p>
<h3 style="color:#142d4c;font-family: Tahoma, sans-serif;font-size: 30px;text-align:center;";>Which course has a higher number? (1 or 2)<h3/>
    <form method="post" action="/" style="font-family: Tahoma, sans-serif;font-size: 30px;margin:auto;width:60%;text-align:center;">
        <input type="hidden" value={2} name="ans"/>
        <input style="border-radius:5px;background-color: #385170; border: none;color: white;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;"type="submit" value="1" name="action1"/>
        <input style="border-radius:5px;background-color: #385170; border: none;color: white;padding: 15px 32px;text-align: center;display: inline-block;font-size: 16px;"type="submit" value="2" name="action2" />
    </form>
</div>

</html>"""

CORRECT_ANS = """Correct, {course1} is {num1} and {course2} is {num2}"""

@app.route("/", methods=['GET', 'POST'])
def index():
    #placeholder = {
    #    6.0001: "Introduction to Computer Science and Programming in Python",
    #    7.012: "Introduction to Biology",
    #    6.042: "Mathematics for Computer Science",
    #    14.01: "Principles of Microeconomics"
    #}
    placeholder = choices.choices
    keys = list(placeholder.keys())
    option1 = random.choice(keys)
    option2 = random.choice(keys)
    while option2 == option1:
        option2 = random.choice(keys)
    course1 = placeholder[option1]
    course2 = placeholder[option2]

    if option1 > option2:
        correct_ans = "1"
        correct_course = course1
        wrong_ans = "2"
    else:
        correct_ans = "2"
        correct_course = course2
        wrong_ans = "1"
    if request.method == 'POST':
        # action = request.form.get('action')
        correct_ans = request.form.get('ans')
        # return redirect(url_for('game_success'))
        if 'action1' in request.form and correct_ans == "1":
            return redirect(url_for('game_success'))
        if 'action2' in request.form and correct_ans == "2":
            return redirect(url_for('game_success'))
        return redirect(url_for('game_over'))
        # if action == correct_ans:
        #     # return retry(course1=course1, num1=option1, course2=course2, num2=option2, correct_ans = correct_course)
        #     return redirect(url_for('game_success'))
        # else:
        #     return redirect(url_for('game_over'))
        # if request.form.get('action1') == correct_ans:
        #     return retry(course1=course1, num1=option1, course2=course2, num2=option2, correct_ans = correct_course)
        #     #return redirect(url_for('/result'))
        #     #return '899889'+'corr'+str(correct_ans)+CHOICES_HTML.format(course1, course2)
        #     # return redirect(url_for('/'))
        # if request.form.get('action1') == wrong_ans:
        #     return redirect(url_for('game_over'))
        # if request.form.get('action2') == correct_ans:
        #     return retry(course1=course1, num1=option1, course2=course2, num2=option2, correct_ans = correct_course)
        #     #return redirect(url_for('/result'))
        #     #return '000000corr'+str(correct_ans)+CHOICES_HTML.format(course1, course2)
        #     # return redirect(url_for('/'))
        # elif request.form.get('action2') == wrong_ans:
        #     return redirect(url_for('game_over'))
        # elif  request.form.get('action2') == correct_ans:
        #     return CHOICES_HTML.format(course1, course2)
        # else:
        #     pass  # unknown
    elif request.method == 'GET':
        return 'hkjhjkh' + 'corr'+str(correct_ans)+INSTRUCTIONS+CHOICES_HTML.format(course1, course2, correct_ans)

    return '11111corr'+ str(correct_ans)+INSTRUCTIONS+CHOICES_HTML.format(course1, course2)

def check_correctness(course1, course2, ans):
    # FJKDFJLFKJLD
    return

@app.route("/result")
def result():
    return INSTRUCTIONS+"<html>You were right!</html>"+redirect(url_for('index'))

@app.route("/retry", methods=['POST'])
def retry(course1, num1, course2, num2, correct_ans):
    #if request.method == 'POST':
    if request.form.get('yes') is not None:
        return CORRECT_ANS.format(course1=course1, num1=num1, course2=course2, num2=num2)+redirect(url_for('index'))
    if request.form.get('no') is not None:
        return CORRECT_ANS.format(course1=course1, num1=num1, course2=course2, num2=num2)+"Thanks for playing!"

    #elif request.method == 'GET':
    #    return None # ******
    #return "why is it GET"


@app.route("/correct")
def game_success():
    return redirect(url_for('index'))
    # return GAME_SUCCESS_DISPLAY

@app.route("/game_over")
def game_over():
    return GAME_OVER_DISPLAY


if __name__=="__main__":
    app.run()
    
    
    
    
    
    

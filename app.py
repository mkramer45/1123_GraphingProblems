from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)
 
  ## works
# @app.route("/")
# def chart():
#     labels = ["12am","3am","6am","9am","12pm","3pm","6pm","9pm"]
#     values = [10,9,8,7,6,4,7,8]
#     return render_template('chart.html', values=values, labels=labels)

# doesn't work ... when attempting to incorporate values from a list as my Y axis values.
@app.route("/")
def chart():
	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("select swellsizeft from surfmaster2 where beach_name = '2nd Beach' and date_ = '2018-11-23'")
	result = cursor.fetchall()
	values = [list(i) for i in result]
	labels = ["12am","3am","6am","9am","12pm","3pm","6pm","9pm"]
	# values = [10,9,8,7,6,4,7,8]
	return render_template('chart.html', values=values, labels=labels)

 
if __name__ == '__main__':
	app.run(debug=True)
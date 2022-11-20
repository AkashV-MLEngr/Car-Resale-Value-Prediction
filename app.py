import random
from flask import Flask, render_template, Response, request

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route('/')
def HomeView():
	return render_template('homeview.html')

@app.route('/predict', methods=['POST'])
def DataEntryView():
	return render_template('predictionview.html')

@app.route('/y_predicted', methods=['GET','POST'])
def PredictedView():
	price = int(request.args.get('price'))
	num = price
	count = 0
	while num != 0:
		num //= 10
		count +=1

	def digit(num):
		rand_idx = random.randrange(len(num))
		random_num = num[rand_idx]
		return random_num

	if count == 1:
		y_list = [1.22, 5.01, 0.99, 3.11, 2.26, 4.30, 6.32, 7.49, 3.50, 0.50, 2.28, 4.70, 5.77]
		y_predict = digit(y_list)

	elif count == 2:
		y_list = [11.22, 15.01, 10.10, 13.11, 22.26, 30.30, 40.32, 26.49, 52.50, 9.50, 8.00,9.23]
		y_predict = digit(y_list)

	elif count == 3:
		y_list = [124.22, 147.11, 226.40, 116.05, 255.53, 363.09, 471.32, 183.49, 534.50, 99.50, 99.29, 98.79, 99.22]
		y_predict = digit(y_list)

	elif count == 4:
		y_list = [1324.22, 1547.22, 2206.01, 1176.01, 2545.22, 3633.11, 4571.26, 1883.10, 5134.30, 999.34, 999.49, 997.32]
		y_predict = digit(y_list)

	elif count == 5:
		y_list = [11454.22, 11427.11, 22206.10, 13446.30, 21545.26, 31633.09, 41571.30, 11883.49, 51134.50, 9999.00, 9998.43, 9997.43, 9999.75]
		y_predict = digit(y_list)

	elif count == 6:
		y_list = [116454.22, 112427.01, 102206.10, 13446.11, 220145.26, 302633.30, 401571.32, 103083.49, 526113.50, 99999.00, 99999.50, 99998.50, 99997.98]
		y_predict = digit(y_list)

	elif count == 7:
		y_list = [1123754.22, 1123427.01, 1012206.10, 103446.11, 2201245.26, 3042633.30, 4101571.32, 1003083.49, 5026113.50, 999999.00, 999998.03, 999997.99]
		y_predict = digit(y_list)

	return render_template('predictedview.html', predicted_value = y_predict)

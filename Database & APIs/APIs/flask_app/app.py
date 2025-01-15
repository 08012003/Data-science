from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)

# It renders an HTML file (index.html) as the home page.

@app.route('/')
def home_page():
    return render_template('index.html')



# Reads inputs (num1, num2, and operation) from the HTML form (request.form).
# Performs the operation (add, subtract, multiply, divide) based on the operation input.

@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return render_template('results.html' , result = result)


# Reads inputs (num1, num2, and operation) from the JSON payload (request.json).
# Performs the operation (add, subtract, multiply, divide) based on the operation input.

@app.route('/postman_action',methods=['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return jsonify(result)

# Starts the Flask development server
if __name__=="__main__":
    app.run(host="0.0.0.0")


'''
The GET method is used to retrieve data from the server, with data sent in the URL as query parameters, making it less secure because the data is visible. 
It is best for fetching resources like search results and supports caching but has a limit on the amount of data due to URL length restrictions. 
The POST method, on the other hand, is used to send data to the server for processing, with data sent in the request body, making it more secure as it is not visible in the URL. 
POST is suitable for tasks like form submissions or uploading files and can handle larger amounts of data without any size limit. 
Unlike GET, POST is not cached and is not idempotent, meaning repeated requests can have different results. 
Use GET for fetching data and POST for sending sensitive or large data.
'''
from flask import Flask, request, jsonify
from flask import render_template
import time

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    # return render_template("index.html")
    print("Got request...")
    start_time = time.time()
    print("Task started at", start_time)
    # Simulate a long-running task
    time.sleep(60 * 15)  # Sleep for 15 minutes
    end_time = time.time()
    print("Task completed at", end_time)
    #return jsonify({'message': 'Task completed successfully'})
    return render_template("index.html")
    
@app.route('/long_running_task', methods=['GET'])
def long_running_task():
    start_time = time.time()
    print("Task started at", start_time)
    # Simulate a long-running task
    time.sleep(60 * 15)  # Sleep for 15 minutes
    end_time = time.time()
    print("Task completed at", end_time)
    return jsonify({'message': 'Task completed successfully'})

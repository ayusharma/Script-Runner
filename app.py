from flask import Flask,request
from settings import locations	
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
	script_url = request.args.get('script')
	if script_url in locations:
		script = locations[script_url]
		params = request.args.get('params')
		args = params.replace(","," ")
		subprocess.call('python '+script+' '+args, shell=True)
	 	return script+" script is running"
	else:
		return "Script Parameter is not present"


if __name__ == "__main__":
    app.run(debug=True)
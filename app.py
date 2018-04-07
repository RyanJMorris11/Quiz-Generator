from flask import Flask, render_template
import tensorflow as tf
app = Flask(__name__)

@app.route("/")
def index():
	
	hello = tf.constant('Hello, TensorFlow!')
	
	# Start tf session
	sess = tf.Session()
	
	# Run the op
	print(sess.run(hello))
	
	return render_template("index.html")
	
	
	
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=80)
	
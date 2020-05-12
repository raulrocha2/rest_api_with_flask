from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def pageone():
	return "page one ok!!"


@app.route('/jsonone')
def jsonone():

	Json_Contact = {
        
        'Name':'Carlos Araujo',
        'email':'caraujo@gmail.com',
        'fone':11978654334
	}
	return jsonify(Json_Contact )
	
     





if __name__=="__main__":
	app.run(debug=True)

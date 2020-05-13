from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def pageone():
	return "page one ok!!"


@app.route('/jsonone')
def jsonone():

	Json_Contact = {
        
        'Name':'Carlos Araujo',
        'email':'caraujo@gmail.com',
        'fone':11978654334,
        'sexo': [
            {
            'laptop':'Dell I5',
            'celular':'LG k10'	
        }
        ] 

	}
	return jsonify(Json_Contact)
	

@app.route('/json_post', methods=["POST"])
def json_post():
	dataDict = request.get_json()

	x = dataDict["x"]
	y = dataDict["y"]

	calc = x+y

	dictJson = {
		"calc":calc
	}
	return jsonify(dictJson), 200


if __name__=="__main__":
	app.run(debug=True)

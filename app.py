from flask import Flask, request,jsonify
app = Flask(__name__)
@app.route("/")
def home():
    return jsonify("welcome to test-api")

@app.route("/team")
def name():
    return jsonify("welcome kevin and vk")

@app.route("/team",methods=["POST"])
def team():
    member = request.json["member"]
    role = request.json["role"]
    return  jsonify("{} is added as {}".format(member,role)),201

if __name__ == "__main__":
    app.run(debug=True)

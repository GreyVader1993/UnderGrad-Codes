from flask import Flask, render_template, request
#from fuzzywuzzy import fuzz
from difflib import SequenceMatcher
app = Flask(__name__, template_folder="common", static_folder="common", static_url_path="")


@app.route("/")
def renderApp():
	return render_template("app.html")

@app.route("/plagiarismDetection", methods=["POST"])
def plagiarismDetection():
	text = request.form["inputText"]

	if text == "":
		return render_template("app.html", result="Error ! No input !", text=text)
	

	#detection logic goes here

	#using SequenceMatcher library

	'''fp1 = open("source1.txt","r")
	fp2 = open("source2.txt","r")
	source = fp1.read() + fp2.read()
	#wrong result
	plagiarismRatio = SequenceMatcher(None, text, source).ratio()'''


	#using self-implemented algorithm
	
	fp1 = open("source1.txt","r")
	fp2 = open("source2.txt", "r")

	textLines = [x.strip(" \n") for x in text.split(".") if x!='']
	source1Lines = [x.strip(" \n") for x in fp1.read().split(".") if x!='']
	source2Lines = [x.strip() for x in fp2.read().split(".") if x!='']

	source = source1Lines+source2Lines

	total = len(textLines)
	copied = 0

	for ipLine in textLines:
		ipKeywords = set(ipLine.split(" "))

		for testLine in source:
			testKeywords = set(testLine.split(" "))

			if len(testKeywords.intersection(ipKeywords)) >= 0.5*len(testKeywords):
				 copied += 1

	plagiarismRatio = int((float(copied)/float(total))*100)

	return render_template("app.html", result = "Test Completed ! Plagiarism Ratio :" + str(plagiarismRatio)+"%", text=text)

if __name__=="__main__":
	app.run(host="0.0.0.0", debug=True)

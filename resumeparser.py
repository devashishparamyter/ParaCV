import nltk
import json
import flask



nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

nltk.download('maxent_ne_chunker')
nltk.download('words')




from pyresparser import ResumeParser
data = ResumeParser('/Naukri_GauravJain[6y_0m].pdf').get_extracted_data()



newDict = {}

newDict['Name']= data.get('name')
newDict['Email']= data.get('email')
newDict['Mobile']= data.get('mobile_number')[-10:-1]

newDict

json_object = json.dumps(newDict, indent = 2)

app = flask.Flask(__name__)

@app.route('/resume_parser_sfdc', methods=['GET'])
def resume_parser():
    try:
        return json_object
    except KeyError:
        return f'failed'









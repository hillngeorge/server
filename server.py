from flask import Flask
import json
from config import dev, sum
from data import catalog
from flask_cors import CORS
from flask import Flask, request



app = Flask(__name__)
CORS(app)  #warning, this disables cors policy

@app.get("/")
def hello():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "Test Page!"



#/about
@app.get("/about")
def about():
    return "About George"



######################################################################
######################  API  Mehtods  ################################
#####################################################################

# ctrl c
# up arrow key
# enter

@app.get('/api/developer')
def developer():

    return json.dumps(dev)



@app.get("/api/sum")
def simple_sum():
    answ = sum(21, 21)
    return json.dumps(answ)



@app.get("/api/products")
def get_catlog():
    return json.dumps(catalog)



@app.post("/api/products")
def save_products():    
    prod = request.get_json()  #read the payload
    catalog.append(prod)



    return json.dumps(prod)




# start thr server
app.run(debug=True)








from flask import Flask,redirect,render_template
import requests
import json
app=Flask(__name__)
@app.route('/')
def ret():
    return render_template("main.html")
@app.route('/load',methods=['GET'])
def load():
    resp=requests.get("http://fake-hotel-api.herokuapp.com/api/hotels?count=5")
    #print(resp.status_code)
    if resp.status_code==200:
        g=resp.content
        d=json.loads(g)
        print(d)
        idc=[]
        for i in d:
            print(i)
            idc.append(i["id"])
        print(idc)
        rev=[]
        for i in idc:
            resp=requests.get("http://fake-hotel-api.herokuapp.com/api/reviews?hotel_id="+i)
            if resp.status_code==200:
                g=resp.content
                rev.append(json.loads(g))
            else:
                return render_template("error.html",error=resp.status_code)
        l=len(d)
            
        return render_template("hotel.html",arr=d,rev=rev,l=l)
    else:
        return render_template("error.html",error=resp.status_code)

app.run(debug=True)
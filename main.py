from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")

def home():
    print("get request")
    return render_template("index.html")

@app.route("/",methods=["POST"])

def home_post():
    print("get post")
    dim1=request.form["first_dimension"]
    dim2=request.form["second_dimension"]
    dim3=request.form["third_dimension"]
    volume=float(dim1)*float(dim2)*float(dim3)
    return render_template("index.html",output=volume,dim_1=dim1,dim_2=dim2,dim_3=dim3)

app.run()

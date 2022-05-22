from flask import Flask, redirect, url_for, request
import pymongo
import json
import os
import binascii

app = Flask(__name__)
mongo_conn = pymongo.MongoClient("mongodb://localhost:27017/")
generic_db = mongo_conn["whatsapp_generic"]
users_coll = generic_db["users"]

@app.route('/create_user',methods = ['POST'])
def create_user():
    # API to create user
    req = request.get_json()
    if 'name' not in req or 'email' not in req or 'mobile' not in req:
        return {"failiure":"One or more key attributes (name, email, mobile) not present in request"}
    record = {"_id":req["mobile"], "name":req["name"], "email":req["email"]}
    try:
        users_coll.insert_one(record)
    except Exception as e:
        print("Error occured {}".format(repr(e)))
        return {"failiure": "Error occured in creating user."}
    return {"status":"success"}

@app.route('/login_user',methods = ['GET'])
def login():
    # API to login a user
    mobile = request.args.get('mobile')
    if mobile is None:
        return {"failiure":"One or more key attributes (name, email, mobile) not present in request"}
    record = {"_id":mobile}
    try:
        res = users_coll.find_one(record)
        if res:
            token = binascii.hexlify(os.urandom(20)).decode()
            users_coll.update_one(record, {"$set":{'token':token}})
            return {"result":"success"}
        else:
            return {"result":"failiure", "reason":"Not a valid user"}
    except Exception as e:
        print("Error occured {}".format(repr(e)))
        return {"failiure": "Error occured in logging in user."}

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9000)
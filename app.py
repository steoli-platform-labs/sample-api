import os
from flask import Flask, jsonify
app=Flask(__name__)
@app.get('/health')
def health(): return jsonify(status='ok')
@app.get('/ready')
def ready(): return jsonify(status='ready')
@app.get('/')
def root(): return jsonify(service='sample-api', environment=os.getenv('ENVIRONMENT','local'))
if __name__=='__main__': app.run(host='0.0.0.0',port=8080)

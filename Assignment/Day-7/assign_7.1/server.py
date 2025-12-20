from flask import Flask, request
from utils.execute_query import execute_Query
from utils.execute_select_query import executeselect

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page!</h1></body></html>"

@server.post('/sensor')
def new_temperature():
    # .get() returns None if the key is missing, preventing crashes
    id = request.form.get('id')
    temp = request.form.get('temp')
    humid = request.form.get('humid')
    timestamp = request.form.get('timestamp')

    if not all([id, temp, humid, timestamp]):
        return "Missing data", 400

    query = f"insert into sensor values({id}, {temp}, {humid}, '{timestamp}');"
    execute_Query(query=query)
    return "record is added successfully"

@server.get('/sensor')
def retrieve():
    temp = request.args.get('temp')
   
    if temp is None:
        return "Please provide a temp parameter in the URL (e.g., /sensor?temp=25)", 400

    query = f"select * from sensor where temp < {temp};"

    data = executeselect(query=query)
    return f"Record : {data}"

@server.put('/sensor')
def updateRecord():
    temp = request.form.get('temp')
    id = request.form.get('id')

    if not all([temp, id]):
        return "Missing id or temp", 400

    query = f"update sensor set temp = {temp} where id = {id};"
    execute_Query(query=query)
    return "Temperature is updated!"

@server.delete('/sensor')
def delete():
    id = request.form.get('id')

    if id is None:
        return "Missing id", 400

    query = f"delete from sensor where id = {id};"
    execute_Query(query=query)
    return "Record Deleted!"
    
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)

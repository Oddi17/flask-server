#!/usr/bin/env python3
from flask import Flask,request #,jsonify
import sys,json,os

app = Flask(__name__)

def unit():
    if os.path.isfile('cond.txt'):
        data_unit = {}
        with open('cond.txt', 'r') as file:
            for line in file:
                key, dict = line.strip().split(None, 1)
                data_unit[key] = dict.strip()
                json.dump(data_unit, open('data.json', 'w+'))

def save(data):
    with open("cond.txt", "w") as file:
        strick = ""
        for k in data.items():
            name, value = str(k).strip("()").split(",", 1)
            name = name.strip("\"")
            value = value.strip("\"")
            strick += name.strip("\'") + " " + value.strip().replace('\'', '') + "\n"
        file.writelines(strick)
        timestamp = os.stat('cond.txt').st_mtime

@app.route('/')
def hello():
   return 'Hello,user! You can use command: \"/show\" to see the parameters,\n\"/set\" to set value of the parameter\n'
   
@app.route('/show')
def show():
    data = json.load(open('data.json'))
    base = {}
    for i in data.keys():
        if i != "High":
            base[i] = data.get(i)
    #parameters = json.dumps(base)       
    return json.dumps(base, indent=4) + "\n"
    

@app.route('/set',methods = ['POST'])
def set_parametres():
    unit_name = request.form
    with open("data.json") as file:
          data = json.load(file)
          for c in unit_name.keys():
              if c == 'Angle_back':
                  if unit_name[c].isdigit() == True and 0<=int(unit_name[c])<=50:
                      data[c] = unit_name[c]
                      json.dump(data, open('data.json', 'w'))
                      save(data)
                  else:
                      return 'Value must be int [from 0 to 50]!!!\n'
              elif c == 'Angle_ankle':
                  if unit_name[c].isdigit() == True and 0<=int(unit_name[c])<=30:
                      data[c] = unit_name[c]
                      json.dump(data, open('data.json', 'w'))
                      save(data)
                  else:
                      return 'Value must be int [from 0 to 30]!!!\n'
              elif c == 'Angle_hip':
                  if int(unit_name[c]) >= -15 and int(unit_name[c]) <= 15:
                      data[c] = unit_name[c]
                      json.dump(data, open('data.json', 'w'))
                      save(data)
                  else:
                      return 'Value must be int [from -15 to 15]!!!\n'    
              else:
                  return "Wrong name parameter: \"{}\"!\nName must be : Angle_back, Angle_hip, Angle_ankle\n".format(c)#,400     
    return f'Values was saved: {c}={data[c]}\n'                            
                   
if __name__ == "__main__":	

    if len(sys.argv) == 1:
        host, port = "0.0.0.0", 12345 #адрес и порт по умолчанию
    elif len(sys.argv) == 3:
        host,port = sys.argv[1],int(sys.argv[2])
    else:
        print("Error host or port (first host then port)")
        sys.exit()
    unit() #проверка наличия файлов
    app.run(host,port)
    

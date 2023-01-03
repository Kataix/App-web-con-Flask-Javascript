from flask import Flask, app, json, render_template, jsonify, request
import random as ra, requests as req, time as ti, csv, sqlite3 ,json, base64 ,telegram
from PIL import Image
from io import BytesIO
from base64 import encodebytes  

tok =  '5321661491:AAEp4aqnSTAHoYiWsHLDvTKTsDhAcxMy54k'
chatId = '5928211889'

bot = telegram.Bot(token = tok)




def Generate():
    seconds = ti.time()
    print(ti.ctime(seconds))
    dData = {
            '01':[ra.randint(5,20)for i in range(1)],
            '25':[ra.randint(5,20)for i in range(1)],
            '10':[ra.randint(5,20)for i in range(1)],
            'te':[ra.randint(-10,10)for i in range(1)],
            'time':ti.ctime(seconds).split(' ')
    }

    return dData

#----------------------------------------------------------------------
app = Flask(__name__)
#----------------------------------------------------------------------

            

@app.route('/1')
def item1():
    return render_template('1.html')

@app.route('/2', methods=['POST'])
def item2():
    #decodifica la imagen enviada 
    def bs64ToImg(img,name):
        data = img.replace(' ', '+')
        imgdata = base64.b64decode(data)
        filename = name  
        with open(filename, 'wb') as f:
            f.write(imgdata)
        with open(name,'rb') as f:
            bot.sendPhoto(chat_id=chatId, photo=f)
        

    if request.method == 'POST':

        data = request.get_json()
        img1 = data['img'][0]
        img2 = data['img'][1]
        #print(img)
        bs64ToImg(img1,'graf1.jpg')
        bs64ToImg(img2,'graf2.jpg')
        

    return jsonify({'result': 'ok'})
          
 
@app.route('/3')
def item3():
    return render_template('3.html')

@app.route('/4')
def item4():
    return render_template('4.html')
#datos del grafico item 1 y 2
@app.route('/getdata')
def getdata():
    aData = Generate()
    return aData
# datos de geolocalizacion item 4
@app.route('/gps_track/<id>/<fe>')
def gps(id,fe):
    print(id,fe)
    con = sqlite3.connect('gps.db')
    cursor = con.cursor()
    data = []
    
    for row in cursor.execute('SELECT * FROM data  WHERE id = '+id+' AND fecha ="'+fe+'" order by hora'):
        data.append([row[3],row[2]])

    
    con.commit()
    cursor.close()

    response = {
         'estatus':'200',
        'datos': data
    }
    #datos = json.dumps(data)
    datos = jsonify(response)
    return datos



if __name__ == '__main__':
    app.run(debug=True)
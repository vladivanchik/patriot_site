from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def filling_db():
    con = create_con()
    cur = con.cursor()
    cur.execute("drop table sities")
    cur.execute("""
        CREATE TABLE if not exists sities(
            name text,
            year_of_creating int,
            data text,
            image text
        )
                """)
    cur.execute("""
        CREATE TABLE if not exists users(
            name text,
            password text,
            email text
        )
                """)
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Одеса', 1794,'Одеса здавна торговий і туристичний центр нашої батьківщини.', 'odesa.jpg')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Київ', 1500,'Столиця України', 'kyiv.png')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Львів', 1662,'Львів – місто, яке за час свого існування перебувало у складі 8 держав', 'lyiv.jpg')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Вінниця', 1363 , 'Місто-столиця. Столицею УНР Вінниця була трохи більше місяця - з 2 лютого по 6 березня 1919 р', 'vin.jpg')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Івано-Франківськ', 1662, 'Протягом нетривалого часу місто було столицею Західно-Української Народної Республіки.', 'iva.jpg')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Харків', 1256, 'Харківський національний університет ім. В.Н. Каразіна - найстаріший і великий ВНЗ України', 'kharkiv.jpg')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Дніпро', 1776, 'На дні Дніпра можна знайти скарби ', 'dripro.jpg')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Суми', 1652 , 'Павловський цукровий завод був найбільшим у Європі! Чому Павловський? Старший Харитоненко назвав його на честь сина Павла.', 'Symu.jpg')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Івано-Франківськ',1682, 'Протягом нетривалого часу місто було столицею Західно-Української Народної Республіки','iva.jpg')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Кривій Ріг', 1652, 'Єдиний у країні Криворізький суриковий завод виробляє залізний сурик, який користується попитом в Україні та за кордоном.','rog.jpg')")
    # cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Житомир', 884, 'Кожна третя пачка морозива виготовлення у цьому місті','jhytomir.jpg')")
    con.commit()
    
def create_con():
    con = sqlite3.connect("patriot.db")
    con.row_factory = sqlite3.Row
    return con
@app.route('/')
def index():
    return render_template("registr.html")

sityes_list = {
    "Одеса" : ["Одеса здавна торговий і туристичний центр нашої батьківщини.","Місто засновано 2 вересня 1794 р.", "odesa.jpg"], 
    "Київ" : ["Столиця України","Місто засновано у VI або VII століттях", "kyiv.png"],
    "Вінниця" : ["Місто-столиця. Столицею УНР Вінниця була трохи більше місяця - з 2 лютого по 6 березня 1919 р.","Місто засовано у 1363 роках.", "vin.jpg"],
    "Львів" : ["Львів – місто, яке за час свого існування перебувало у складі 8 держав ", "Місто було засновано у 1662 р.","Lyiv.jpg"],
    "Івано-Франківськ" : ["Протягом нетривалого часу місто було столицею Західно-Української Народної Республіки.","Місто було засновано у 1662 р.", "iva.jpg"],
    "Харків" : ["Харківський національний університет ім. В.Н. Каразіна - найстаріший і великий ВНЗ України","Місто було засновано у 1256", "krakiv.jpg"],
    "Дніпро" : ["На дні Дніпра можна знайти скарби ","Місто було засновано у 1776 р.","dnipro.jpg"],
    "Суми" : ["Павловський цукровий завод був найбільшим у Європі! Чому Павловський? Старший Харитоненко назвав його на честь сина Павла."," Місто було засновано у 1652 р.", "Symu.jpg"],
    "Кривій Ріг": ["Єдиний у країні Криворізький суриковий завод виробляє залізний сурик, який користується попитом в Україні та за кордоном.","Місто було засновано у 1775 р.","rog.jpg"],
    "Житомир" : ["Кожна третя пачка морозива виготовлення у цьому місті", "Місто було засновано у близько у 884 роках.", "jhytomir.jpg"]
}
#
#def sityes():
    
    # return render_template("sityes.html", sityes_list=sityes_list)
@app.route('/sityes')
def sityes():
    con = create_con()
    cur = con.cursor()
    cur.execute("SELECT * from sities")
    sities = cur.fetchall()
    return render_template("sities_db.html", sities = sities)
@app.route('/registr', methods = ["GET","POST"])
def registr ():
    con = create_con()
    cur = con.cursor()
    login = request.form.get("login")
    password = request.form.get("password")
    cur.execute("INSERT INTO user (name, password) VALUES (?,?)", [login, password])
    return render_template("registr.html")

@app.route('/himn')
def himn():
    return render_template("himn.html")

app.run(debug=True)

# from kivy.app import App
# app = App()
# app.run()
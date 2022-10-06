from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
con = sqlite3.connect("patriot.db")
con.row_factory
cur = con.cursor()
# cur.execute("drop table sities")
cur.execute("""
    CREATE TABLE if not exists sities(
        name text,
        year_of_creating int,
        data text,
        image text
    )
            """)
# cur.execute("INSERT INTO sities(name, year_of_creating, data, image) VALUES ('Одеса', 1794,'Одеса здавна торговий і туристичний центр нашої батьківщини.', 'odesa.jpg')")
con.commit()
cur.execute("SELECT * from sities")
sities = cur.fetchall()
print(sities)
@app.route('/')
def index():
    return render_template("index.html")

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
    
    return render_template("sities_db.html", sities = sities)

@app.route('/himn')
def himn():
    return render_template("himn.html")

app.run(debug=True)

# from kivy.app import App
# app = App()
# app.run()
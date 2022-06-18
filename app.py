from flask import Flask, render_template, url_for
from flask import request
app = Flask(__name__)





@app.route('/', methods=["GET", "POST"])
def index():
    result = ''
    if request.method == "POST":
        stroke = int(request.form.get("stroke"))
        page = int(request.form.get("page"))

        pageBase = 50
    
      
        pageBaseMult = int(pageBase) * int(page) - int(pageBase) + int(stroke)
        with open("bible.txt", "r", encoding="utf-8") as text_file:
            data = text_file.readlines()
        
        if stroke > pageBase:
            result = 'Такой строки нет!'
        elif (page * pageBase) > len(data):
            result = 'Больше чем страниц в книге'
        elif page == 2:
            result = data[pageBase + stroke - 1]

        elif page == 1:
            if data[stroke] == '\n':
                result = 'Неизвестность'
            else:
                result = data[stroke]
        elif page > 2:
            if data[pageBaseMult - 1] == '':
                result = 'Неизвестность'
            else:
                result = data[pageBaseMult - 1]
            
                
     
    return render_template("index.html", result=result)

   


if __name__ == "__main__":
    app.run(debug=True)
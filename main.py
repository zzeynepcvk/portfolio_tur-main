# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python,button_discord=button_discord,button_html=button_html,
    button_db=button_db)

# Form sayfasını çalıştırma

@app.route('/submit', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    email = request.form['email']
    comment = request.form['comment']

    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    return render_template('index.html', 
                           # Değişkenleri buraya yerleştirin
                           email=email,
                           comment = comment
                           )

if __name__ == "__main__":
    app.run(debug=True)

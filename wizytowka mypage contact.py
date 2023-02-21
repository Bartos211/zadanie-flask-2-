from flask import Flask

app = Flask(__name__)

@app.route('/mypage/contacy')
def My_page_contact():
    my_number_phone = "123456789"
    my_address = "ul.mieszana 7"
    return f' My_page, {my_number_phone}, {my_address}'
from flask import Flask, json, request, jsonify
import pymysql.cursors

app = Flask(__name__)

connection = pymysql.connect(host='localhost', user='root', password='', db='akekoo', charset='utf8mb4', cursorclass=
                             pymysql.cursors.DictCursor)


@app.route('/')
def default():
    return "Hello World"


@app.route('/akekoo/languages', methods=['GET', 'POST'])
def get_language():
    cursor = connection.cursor()
    sql = "Select * from languages"
    cursor.execute(sql)
    result = cursor.fetchall()
    if int(len(result)) > 0:
        return jsonify({"languages": result, 'success': 1})
    else:
        return jsonify({"message": "No language in Database yet", 'success': 0})


@app.route('/akekoo/language/insert', methods=['GET', 'POST'])
def insert_language():
    try:
        if request.method == 'GET':
            language = request.args.get('name')
        else:
            language = request.form.get('name')

        sql = "Insert into languages(name) values(%s)"
        cursor = connection.cursor()
        cursor.execute(sql, language)
        connection.commit()
        return jsonify({'message': "Language recorded successfully", 'success': 1})
    except:
        return jsonify({"message": "An error occurred", 'success': 0})


@app.route('/akekoo/book/id', methods=['GET', 'POST'])
def book_id():
    try:
        if request.method == 'GET':
            _id = request.args.get('id')
        else:
            _id = request.form.get('id')
        sql = "Select * from books where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, id)
        result = cursor.fetchall()
        if int(len(result)) > 0:
            return jsonify({"book_details": result, 'success': 1})
        else:
            return jsonify({'message': "No books on language yet", 'success': 0})
    except:
        return jsonify({'message': "An error occurred. Try again", 'success': 0})


@app.route('/akekoo/book', methods=['GET', 'POST'])
def book():
    try:
        if request.method == 'GET':
            lang_id = request.args.get('lang_id')
        else:
            lang_id = request.form.get('lang_id')
        sql = "Select * from books where lang_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, lang_id)
        result = cursor.fetchall()
        if int(len(result)) > 0:
            return jsonify({'data': result, 'success': 1})
        else:
            return jsonify({'message': 'No data available yet', 'success': 0})
    except:
        return jsonify({'message': 'An unexpected error occurred', 'success': 0})


@app.route('/akekoo/video/id', methods=['GET', 'POST'])
def video_id():
    try:
        if request.method == 'GET':
            _id = request.args.get('id')
        else:
            _id = request.form.get('id')
        sql = "Select * from videos where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, _id)
        result = cursor.fetchall()
        if int(len(result)) > 0:
            return jsonify({'data': result, 'success': 1})
        else:
            return jsonify({'message': 'No video uploaded yet', 'success': 0})
    except:
        return jsonify({'message': 'An unexpected error occurred. Try again', 'success': 0})

if __name__ == '__main__':
    app.run(debug=True)

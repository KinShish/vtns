from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
from normolize import normalize_api
from train import predict
from flask import send_from_directory
from PIL import Image
import os
import io
import json
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['UPLOAD_FOLDER'] = "upload"


def allowed_file(filename):
  """ Функция проверки расширения файла """
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in {'json'}
@app.route('/load/dataset/chek',methods=['POST'])
def load_dataset_chek():
  if 'file' not in request.files:
    return "Не могу прочитать файл"
  file = request.files['file']
  if file.filename == '':
    return "Нет выбранного файла"
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    with open(app.config['UPLOAD_FOLDER'] + '/'+filename, 'r', encoding='utf-8') as f:
      dataset_train = json.load(f)
    print(1111,len(dataset_train))
    dataset = normalize_api.normalize(dataset_train)
    percent_accounts = predict.predict(dataset)
    print(len(percent_accounts))
    for i in range(len(percent_accounts)):
      if percent_accounts[i][1] == dataset_train[i]['accountId']:
        dataset_train[i]['percent'] = percent_accounts[i][0]
        dataset_train[i]['aproxima'] = percent_accounts[i][2]
    return dataset_train
  return "error"

@app.route('/load/dataset/update/commerce',methods=['POST'])
def load_dataset_commerce():
  if 'file' not in request.files:
    return "Не могу прочитать файл"
  file = request.files['file']
  if file.filename == '':
    return "Нет выбранного файла"
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    with open(app.config['UPLOAD_FOLDER'] + '/'+filename, 'r', encoding='utf-8') as f:
      dataset_train = json.load(f)
    dataset = normalize_api.normalize_commerce(dataset_train)
    percent_accounts = predict.predict_commerce(dataset)
    for i in range(len(percent_accounts)):
      if percent_accounts[i][1] == dataset_train[i]['accountId']:
        dataset_train[i]['isCommercial'] = percent_accounts[i][0]
        dataset_train[i]['aproxima'] = percent_accounts[i][2]
    return dataset_train
  return "error"

@app.route('/uploads/account/<id>',methods=['GET'])
def get_account_photo(id):
  if not os.path.exists(f"upload/{id}"): return []
  list_files = os.listdir(f"upload/{id}")
  return list_files

@app.route('/uploads/account/<id>/<name>',methods=['GET'])
def download_file(id,name):
  print(app.config["UPLOAD_FOLDER"],id)
  return send_from_directory(f'upload/{id}', name)

@app.route('/')
def hello_world():

  return 'Hello, World!'

if __name__ == '__main__':
  app.run(debug=True, host='10.2.0.233', port=80)
from django.shortcuts import render
import pyrebase

config = {
  'apiKey': "AIzaSyBhj3If5etw9wk-QXnNnU0vvRxBKk2syFw",
  'authDomain': "site-aqua-54d76.firebaseapp.com",
  'databaseURL': "https://site-aqua-54d76-default-rtdb.firebaseio.com",
  'projectId': "site-aqua-54d76",
  'storageBucket': "site-aqua-54d76.appspot.com",
  'messagingSenderId': "534915687051",
  'appId': "1:534915687051:web:e9465dcbc3fead6e082a8e"

}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth
database = firebase.database()

def index(request):
  ph = database.child('Data').child('PH').get().val()
  temperatura = database.child('Data').child('TEMPERATURA').get().val()
  umidade = database.child('Data').child('UMIDADE').get().val()
  return render(request, 'index.html', {
    'ph': ph,
    'temperatura': temperatura,
    'umidade': umidade
  })

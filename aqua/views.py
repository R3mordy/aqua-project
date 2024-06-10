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
  name = database.child('Data').child('Name').get().val()
  age = database.child('Data').child('Age').get().val()
  birthday = database.child('Data').child('Birthday').get().val()
  return render(request, 'index.html', {
    'name': name,
    'age': age,
    'birthday': birthday
  })

from . import app, db
from .forms import AppForm
from .models import Application
from flask import render_template, url_for, redirect, request

@app.route('/home', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def home():
    new_app_form = AppForm()
    applications = Application.query.all()
    
    if (request.method == 'POST'):
        print(new_app_form.data)    
        if (new_app_form.validate_on_submit()):
            new_application = Application(
                app_name=new_app_form.data.get('app_name'),
                app_description=new_app_form.data.get('app_description'),
                app_protocol=new_app_form.data.get('app_protocol'),
                app_address=new_app_form.data.get('app_address'),
                app_port=new_app_form.data.get('app_port'),
            )
            db.session.add(new_application)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            new_app_form.errors
    return render_template('home.html', new_app_form=new_app_form, applications=applications)

@app.route('/<id>/delete', methods=['GET'])
def delete_app(id):
    application = Application.query.filter(Application.id == id).first()
    db.session.delete(application)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/settings', methods=['POST', 'GET'])
def settings():
    return render_template('settings.html')
    

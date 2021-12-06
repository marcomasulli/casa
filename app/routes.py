from . import app, db
from .forms import AppForm, ProfileForm
from .models import Application, Profile, Background, RowStructure
from flask import render_template, url_for, redirect, request

@app.route('/home', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def home():
    current_profile = db.session.query(
        Profile, Background, RowStructure
        ).join(
            Background, 
            Background.id == Profile.profile_background,
            isouter=True
            ).join(
            RowStructure, 
            RowStructure.row_cards == Profile.profile_cards_per_row,
            isouter=True
            ).filter(
            Profile.profile_is_current == True
            ).first()
    new_app_form = AppForm()
    applications = Application.query.all()
    if (request.method == 'POST'):
        print(new_app_form.data)    
        if (new_app_form.validate_on_submit()):
            new_application = Application(
                app_name=new_app_form.data.get('app_name'),
                app_icon_link=new_app_form.data.get('app_icon_link'),
                app_description=new_app_form.data.get('app_description'),
                app_protocol=new_app_form.data.get('app_protocol'),
                app_port=new_app_form.data.get('app_port'),
            )
            db.session.add(new_application)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            new_app_form.errors
    return render_template('home.html', new_app_form=new_app_form, applications=applications, current_profile=current_profile)

@app.route('/<id>/delete', methods=['GET'])
def delete_app(id):
    application = Application.query.filter(Application.id == id).first()
    db.session.delete(application)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/preferences', methods=['POST', 'GET'])
def preferences():
    current_profile = db.session.query(
        Profile, Background, RowStructure
        ).join(
            Background, 
            Background.id == Profile.profile_background,
            isouter=True
            ).join(
            RowStructure, 
            RowStructure.row_cards == Profile.profile_cards_per_row,
            isouter=True
            ).filter(
            Profile.profile_is_current == True
            ).first()
    profile_form = ProfileForm()
    profiles = db.session.query(
        Profile, Background
        ).join(
            Background, 
            Background.id == Profile.profile_background,
            isouter=True
        ).all()

    if (request.method == 'POST'):
        print(profile_form.data)    
        if (profile_form.validate_on_submit()):
            new_profile = Profile(
                profile_name=profile_form.data.get('profile_name'),
                profile_default_url=profile_form.data.get('profile_default_url'),
                profile_background=profile_form.data.get('profile_background'),
                profile_columns=profile_form.data.get('profile_columns'),
                profile_cards_per_row=profile_form.data.get('profile_cards_per_row'),
                profile_is_current=profile_form.data.get('profile_is_current')
            )

            db.session.add(new_profile)
            db.session.commit()

            # force check on default profile. Only one profile can be default a any given time.
            new_profile = db.session.query(Profile).filter(Profile.profile_name == profile_form.data.get('profile_name')).first()

            if new_profile.profile_is_current:
                db.session.query(Profile).filter(Profile.id != new_profile.id).update({'profile_is_current':False}, synchronize_session='fetch')
                db.session.commit()    

            return redirect(url_for('preferences'))
        else:
            profile_form.errors
    return render_template('preferences.html', profiles=profiles, profile_form=profile_form, current_profile=current_profile)
    
@app.route('/profile/<profile_id>/delete')
def delete_profile(profile_id):
    profile = Profile.query.filter(Profile.id == profile_id).first()
    db.session.delete(profile)
    db.session.commit()
    return redirect(url_for('preferences'))

@app.route('/profile/<profile_id>/edit', methods=['GET', 'POST'])
def edit_profile(profile_id):
    current_profile = db.session.query(
        Profile, Background, RowStructure
        ).join(
            Background, 
            Background.id == Profile.profile_background, 
            isouter=True
            ).join(
            RowStructure, 
            RowStructure.row_cards == Profile.profile_cards_per_row, 
            isouter=True
            ).filter(
            Profile.profile_is_current == True
            ).first()
    profile = Profile.query.filter(Profile.id == profile_id).first()
    profile_form = ProfileForm(
        profile_name=profile.profile_name,
        profile_default_url=profile.profile_default_url,
        profile_background=profile.profile_background,
        profile_columns=profile.profile_columns,
        profile_cards_per_row=profile.profile_cards_per_row,
        profile_is_current=profile.profile_is_current
    )

    if request.method == 'POST':

        if profile_form.validate_on_submit():

            edited_profile = {
                'profile_name': profile_form.data.get('profile_name'),
                'profile_default_url':profile_form.data.get('profile_default_url'),
                'profile_background':profile_form.data.get('profile_background'),
                'profile_columns':profile_form.data.get('profile_columns'),
                'profile_cards_per_row':profile_form.data.get('profile_cards_per_row'),
                'profile_is_current': profile_form.data.get('profile_is_current')
            }

            if profile_form.data.get('profile_is_current') == True:
                db.session.query(Profile).filter(Profile.id != profile_id).update({'profile_is_current':False}, synchronize_session='fetch')
                db.session.commit()    

            db.session.query(Profile).filter_by(id=profile_id).update(edited_profile, synchronize_session='fetch')
            db.session.commit()

            return redirect(url_for('preferences'))

    return render_template('edit_profile.html', 
                            current_profile=current_profile, 
                            profile_id=profile_id, 
                            profile=profile, 
                            profile_form=profile_form)
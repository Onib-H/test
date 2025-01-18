from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if 'user' in session:  # If already logged in, redirect to home
        return redirect(url_for('auth.home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Dummy authentication logic
        if username == 'admin' and password == 'password':
            session['user'] = username
            return redirect(url_for('auth.home'))
        else:
            flash('Invalid credentials', 'error')

    response = make_response(render_template('login.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))

@auth_bp.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return redirect(url_for('auth.login'))

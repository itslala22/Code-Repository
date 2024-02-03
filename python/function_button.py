# Login in feature
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password': 
        return redirect(url_for('home'))
    else:
        flash('Invalid username or password')
        return redirect(url_for('index'))

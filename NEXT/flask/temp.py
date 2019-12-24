from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
    persons = Person.query.all()
    if request.method == 'POST':
        person_name = request.form.get('person')
        persons = Person.query.filter_by(name=person_name)
    return render_template('search_and_add.html', persons=persons)
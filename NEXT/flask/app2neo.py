# For Web Server
from flask import Flask, url_for, render_template
from flask import request,flash,redirect

# For graph
from py2neo import Node, Relationship
from py2neo import Graph
from py2neo.ogm import GraphObject, RelatedFrom, RelatedTo
from py2neo.ogm import Property

# Build connection to graph DB
graph = Graph(password='aaduser')

# build 2 classes for node
class Officer(GraphObject):
    name = Property()
    node_id = Property()
    countries = Property()

    # registered_address = RelatedTo(Address)
    officer_of = RelatedTo("Entity")
    shareholder_of = RelatedTo("Entity")
    director_of = RelatedTo("Entity")
    # maybe not work for other leak data
    alternate_director_of = RelatedTo("Entity")
    # intermediary_of = RelatedTo()

class Entity(GraphObject):
    name = Property()
    node_id = Property()
    
    officers = RelatedFrom("Officer","OFFICER_OF")
    shareholders = RelatedFrom("Officer","SHAREHOLDER_OF")
    directors = RelatedFrom("Officer","ALTERNATE_DIRECTOR_OF")


# build the empty dictionary for store the data from neo4j
the_dict = {"elements":{"nodes":[],"edges":[]}, "style":{}, "layout":{ "name": "grid"}}

# Build a Web Server object
app = Flask(__name__)
app.secret_key = 'dev'

@app.route('/',methods=['GET','POST'])
def hello():
    
    flash('hohohoho,it is flash')

    if request.method == 'POST':
        # get form data
        name = request.form.get('name')
        return render_template('search.html',name=name)
    url_hello = url_for('static',filename='images/totoro.gif')
    print(url_hello)
    
    return render_template('search.html',name='Please Enter Name')

@app.route('/user/<name>')
def user_page(name):
    return '<h2>This is User: {}</h2>'.format(name)

@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST'])
def edit(movie_id):
    movie ='Got Nothing'

    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']

        return redirect(url_for('edit',movie_id=movie_id))
    
    return render_template('edit.html',movie=movie)

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='Jim'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'Test Page'

@app.errorhandler(404)
def page_not_found(e):
    user = 'Jim'
    return render_template('404.html',user=user), 404

if __name__=='__main__':
    app.run(debug=True,host='127.0.0.1',port=8080)

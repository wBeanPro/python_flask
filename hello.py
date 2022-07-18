import psycopg2

try:
	conn = psycopg2.connect("dbname='autocomplete' user='ubuntu' password='123'")
	print("connected to the database.")
except:
	print("unable to connect to the database.")
cur = conn.cursor()

cur.execute("select * from information_schema.tables where table_name=%s", ('category',))
if bool(cur.rowcount):
	cur.execute("DROP TABLE category")
	conn.commit()
try:
	cur.execute("""CREATE TABLE category ( id SERIAL PRIMARY KEY, name varchar(30));""")
	cur.execute("INSERT INTO category(id,name) VALUES(DEFAULT,'Fruit')")
	cur.execute("INSERT INTO category(id,name) VALUES(DEFAULT,'Animal')")
	cur.execute("INSERT INTO category(id,name) VALUES(DEFAULT,'Food')")
	cur.execute("INSERT INTO category(id,name) VALUES(DEFAULT,'Computer')")
	conn.commit()
	print("table 'categoy' created")
except:
	print("failed to create table 'category'")

cur.execute("select * from information_schema.tables where table_name=%s", ('product',))
if bool(cur.rowcount):
	cur.execute("DROP TABLE product")
	conn.commit()
try:
	cur.execute("""CREATE TABLE product ( id SERIAL PRIMARY KEY, category_id integer, name varchar(30));""")
	cur.execute("INSERT INTO product(category_id,name) VALUES(1,'Apple')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(1,'Orange')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(1,'Grape')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(1,'Pear')")

	cur.execute("INSERT INTO product(category_id,name) VALUES(2,'Dog')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(2,'Cat')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(2,'Snake')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(2,'Tiger')")
	
	cur.execute("INSERT INTO product(category_id,name) VALUES(3,'Beef Stack')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(3,'Sandwich')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(3,'Reuben')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(3,'French Fries')")
	
	cur.execute("INSERT INTO product(category_id,name) VALUES(4,'LENOVO')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(4,'DELL')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(4,'IBM')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(4,'HP')")
	cur.execute("INSERT INTO product(category_id,name) VALUES(4,'ASUS')")

	conn.commit()
	print("table 'categoy' created")
except:
	print("failed to create table 'category'")


from flask import Flask, render_template, jsonify, request

app = Flask(__name__,template_folder='templates')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/category_api', methods=['GET'])
def category_api():
    cur.execute("SELECT * FROM category")
    data = cur.fetchall()
    return jsonify(data)

@app.route('/product_api', methods=['GET'])
def product_api():
    category = request.args.get('c_id', default = 1, type = int)
    if category == 0:
	    cur.execute("SELECT name FROM product")
    else:
	    cur.execute("SELECT name FROM product where category_id = %s",(category,))
    data = cur.fetchall()
    return jsonify(data)

if __name__ == '__main__':
   app.run()


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



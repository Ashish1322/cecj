import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ramta2000#",
    database = "games"
)
cur = db.cursor()
cur.execute("CREATE TABLE employees2(emp_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), desig VARCHAR(20), salary INT)")
# cur.execute("INSERT INTO employees2 (name, desig, salary) VALUE ('john doe', 'project manager', 50000)")
# cur.execute("INSERT INTO employees2 (name, desig, salary) VALUE ('jane doe', 'developer', 63000)")
# cur.execute("INSERT INTO employees2 (name, desig, salary) VALUE ('jake paul', 'janitor', 34000)")
# cur.execute("INSERT INTO employees2 (name, desig, salary) VALUE ('logan paul', 'delivery manager', 90000)")
# cur.execute("INSERT INTO employees2 (name, desig, salary) VALUE ('ksi', 'cfo', 120000)")

# db.commit()
def show():
    cur.execute("SELECT * FROM employees2")
    for i in cur:
        print(i)

# cur.execute("UPDATE employees2 SET salary = 130000 WHERE emp_id = 5")
# cur.execute("UPDATE employees2 SET salary = salary-10000 WHERE emp_id = 4")

show()
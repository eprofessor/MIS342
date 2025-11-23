# PgP 10/30/2023 create webpage with table to display last 25 sensor readings

import mariadb

# Database configuration
db_config = {
    "host": "192.168.1.208",       # replace with RPi IP address
    "user": "user",
    "password": "user",
    "database": "sensor",
}

try:
    # Connect to the MariaDB database
    connection = mariadb.connect(**db_config)
    cursor = connection.cursor()

    # Execute a query to retrieve the data
   # query = "SELECT recordid, temperature, humidity, timestamp FROM dht"
    query = "SELECT * FROM dht ORDER BY recordid DESC LIMIT 25;"
    cursor.execute(query)

    # Fetch all the rows from the query
    data = cursor.fetchall()

    # Close the cursor and the connection
    cursor.close()
    connection.close()

    # Generate an HTML file with a table
    with open("/var/www/html/index.html", "w") as html_file:
        html_file.write("<html><head><title>DHT Table</title></head><body>")
        html_file.write("<h1>DHT Table, 25 most recent records</h1>")
        html_file.write("<table border='1'><tr><th>Record ID</th><th>Temperature</th><th>Humidity</th><th>Timestamp</th></tr>")
        for row in data:
            html_file.write(f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>")
        html_file.write("</table></body></html")

    print("HTML file created: index.html")

except mariadb.Error as e:
    print(f"Error: {e}")

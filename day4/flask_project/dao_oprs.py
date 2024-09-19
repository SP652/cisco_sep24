import sqlite3

class Flight:
    def __init__(self, id, airline, source, destination, duration, fare) -> None:
        self.id = id
        self.airline = airline
        self.source = source
        self.destination = destination
        self.duration = duration
        self.fare = fare

    def __str__(self) -> str:
        return f'{self.airline}, {self.source}, {self.destination}, {self.duration}, {self.fare}'

    def __repr__(self) -> str:
        return self.__str__()

def connect_db():
    conn = sqlite3.connect('flights_db.db')
    return conn

def create_table_flights():
    query = 'create table IF NOT EXISTS flights(id int primary key, AUTOINCREMENT, airline varchar(30) not null, source varchar(30) not null, destination varchar(30) not null, duration float, fare int)'
    conn = connect_db()
    conn.execute(query)
    conn.close()

def read_flight_details():
    airline = input('Enter airline name: ')
    source = input('Enter Source place name: ')
    destination = input('Enter Destination place name: ')
    duration = float(input('Enter Duration in hours: '))
    fare = float(input('Enter Fare in INR: '))
    return (airline, source, destination, duration, fare)

def create_flight():
    query = 'insert into flights(airline, source, destination, duration, fare) values(?, ?, ?, ?, ?)'
    conn = connect_db()
    flight_details = read_flight_details()
    cursor = conn.cursor()
    cursor.execute(query, flight_details)
    id = cursor.lastrowid
    conn.commit()
    conn.close()
    return id

def search_flight():
    query = 'select * from flights where id = ?'
    id = int(input('Enter id of the flight: '))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, id)
    rs = cursor.fetchone()
    print(str(rs))
    return rs

def list_flights():
    query = 'select * from flights'
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    flights = []
    for row in rows:
        flights.append(
            Flight(id=row[0], airline=row[1], source=row[2], destination=rows[3], duration=row[4],fare=row[5])
        )
    return flights

def delete_flight():
    query = 'delete from flights where id = ?'
    id = int(input('Enter id of the flight to be deleted: '))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, id)
    conn.commit()
    cursor.close()
    conn.close()

def update_flight():
    query = 'update flights set duration = ?, fare = ? where id = ?'
    id = int(input('Enter id of the flight to be updated: '))
    duration = float(input('Enter new duration of the flight: '))
    fare = float(input('Enter new fare of the flight: '))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, (duration, fare, id))
    conn.commit()
    cursor.close()
    conn.close()
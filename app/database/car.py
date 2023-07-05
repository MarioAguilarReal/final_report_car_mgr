from app.database import get_db

def format_output(results):
    out = []
    for result in results:
        res = {
            "id": result[0],
            "type_car": result[1],
            "color": result[2],
            "license": result[3],
            "owner_last_name": result[4],
            "owner_first_name": result[5]
        }
        out.append(res)
    return out

def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM car", ())
    results = cursor.fetchall()
    cursor.close
    return format_output(results)

def select_by_id(car_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM car WHERE id=?", (car_id, ))
    results = cursor.fetchall()
    cursor.close()
    if results:
        return format_output(results)[0]
    return None

def insert(car_data):
    statement = """
        INSERT INTO car (
        type_car,
        color,
        license,
        owner_last_name,
        owner_first_name
        ) VALUES (?,?,?,?,?)
    """

    conn = get_db()
    conn.execute(statement, (
        car_data.get("type_car"),
        car_data.get("color"),
        car_data.get("license"),
        car_data.get("owner_last_name"),
        car_data.get("owner_first_name")
    ))
    conn.commit()

def update_by_id(car_data, car_id):
    statement = """
        UPDATE car
        SET
        type_car = ?,
        color = ?,
        license = ?,
        owner_last_name = ?,
        owner_first_name = ?
    """

    conn = get_db()
    conn.execute(statement, (
        car_data.get("type_car"),
        car_data.get("color"),
        car_data.get("license"),
        car_data.get("owner_last_name"),
        car_data.get("owner_first_name"),
        car_id
    ))
    conn.commit()

    def delete_by_id(car_id):
        conn = get_db()
        conn.execute("DELETE FROM car WHERE id=?", (car_id,))
        conn.commit()

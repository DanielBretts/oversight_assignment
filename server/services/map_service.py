from data.db_connection import create_connection, execute_query
from data.models.coordinate import CoordinatesEntity


class MapService:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = create_connection(self.db_path)

    async def fetch_points_from_db(self):
        self.connection = create_connection(self.db_path)
        if self.connection:
            try:
                query = "SELECT id, latitude, longitude FROM points;"
                cursor = self.connection.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
            except Exception as e:
                print("Error:", e)
            # finally:
            #     # Close the connection
            #     self.connection.close()
        else:
            print("Error! cannot create the database connection.")

    def store_point_locally(self, coordinates: CoordinatesEntity):
        ce = CoordinatesEntity(
            id=coordinates["id"],
            lat=coordinates["computed_geometry"]["coordinates"][1],
            lng=coordinates["computed_geometry"]["coordinates"][0],
        )

        query = f"INSERT INTO points (id, latitude, longitude) \
            VALUES ('{ce.id}', '{ce.lat}', '{ce.lng}');"
        try:
            # Execute the query and fetch the results
            results = execute_query(self.connection, query)
            self.connection.commit()
            if results:
                for row in results:
                    print(row)
        except Exception as e:
            print("Error:", e)

    async def store_coordinates(self, coordinates_data):
        if self.connection:
            try:
                for coordinate in coordinates_data:
                    self.store_point_locally(coordinate)
            except Exception as e:
                print("Error:", e)
        else:
            print("Error! cannot create the database connection.")

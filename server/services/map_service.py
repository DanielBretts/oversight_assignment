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
                query = "SELECT id, latitude, longitude, image_url FROM points;"
                cursor = self.connection.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
            except Exception as e:
                print("Error:", e)
        else:
            print("Error! cannot create the database connection.")

    async def store_point_locally(self, coordinates: CoordinatesEntity):
        ce = CoordinatesEntity(
            id=coordinates["id"],
            lat=coordinates["computed_geometry"]["coordinates"][1],
            lng=coordinates["computed_geometry"]["coordinates"][0],
            image_url=f"https://www.mapillary.com/embed?image_key={coordinates['id']}&style=photo"
        )

        query = f"INSERT INTO points (id, latitude, longitude,image_url) \
            VALUES ('{ce.id}', '{ce.lat}', '{ce.lng}', '{ce.image_url}');"
        try:
            results = await execute_query(self.connection, query)
            self.connection.commit()
            return ce
        except Exception as e:
            print("Error:", e)

    async def store_coordinates(self, coordinates_data):
        boundaries = list()
        if self.connection:
            try:
                for coordinate in coordinates_data:
                    boundaries.append(await self.store_point_locally(coordinate))
                return boundaries
            except Exception as e:
                print("Error:", e)
        else:
            print("Error! cannot create the database connection.")

import httpx
from sqlalchemy import text

from app.db.session import engine
from app.lib.entities.mixins import Base

preset = [

    {"Sensor_type": 10, "num": 0, "name": "N/A", "temperature": 20, "humidity": 25},
    {"Sensor_type": 4, "num": 1, "name": "N/A"},
    {"Sensor_type": 1, "num": 2, "name": "N/A", "temperature": 13},
    {"Sensor_type": 2, "num": 3, "name": "N/A", "humidity": 58},
    {"Sensor_type": 10, "num": 4, "name": "N/A", "temperature": 23, "humidity": 59},
    {"Sensor_type": 4, "num": 5, "name": "N/A"},
    {"Sensor_type": 1, "num": 6, "name": "N/A", "temperature": 19},
    {"Sensor_type": 2, "num": 7, "name": "N/A", "humidity": 35},
    {"Sensor_type": 10, "num": 8, "name": "N/A", "temperature": 22, "humidity": 50},
    {"Sensor_type": 4, "num": 9, "name": "N/A"},
    {"Sensor_type": 1, "num": 10, "name": "N/A", "temperature": 20},
    {"Sensor_type": 2, "num": 11, "name": "N/A", "humidity": 57},
    {"Sensor_type": 10, "num": 12, "name": "N/A", "temperature": 22, "humidity": 55},
    {"Sensor_type": 4, "num": 13, "name": "N/A"},
    {"Sensor_type": 1, "num": 14, "name": "N/A", "temperature": 13},
    {"Sensor_type": 2, "num": 15, "name": "N/A", "humidity": 45},
    {"Sensor_type": 10, "num": 16, "name": "N/A", "temperature": 21, "humidity": 35},
    {"Sensor_type": 4, "num": 17, "name": "N/A"},
    {"Sensor_type": 1, "num": 18, "name": "N/A", "temperature": 20},
    {"Sensor_type": 2, "num": 19, "name": "N/A", "humidity": 35},
]


async def create() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.execute(text("DROP TABLE IF EXISTS alembic_version;"))
        await conn.run_sync(Base.metadata.create_all)

    async with httpx.AsyncClient(http1=True) as client:
        for obj in preset:
            response = await client.post("http://localhost:5000/api/events/", json=obj, follow_redirects=True)
            print(response.status_code, response.text)
            print(f"Added: {obj}")


def main() -> None:
    import asyncio
    asyncio.run(create())


if __name__ == "__main__":
    main()

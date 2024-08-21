import pprint
from datetime import UTC, datetime, timedelta

from bson import ObjectId
from pymongo import MongoClient

DATABASE_NAME = "test"
COLLECTION_NAME = "test"
DAYS_TO_DELETE = 1


client: MongoClient = MongoClient("mongodb://user:password@localhost:27017/")
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]


def create_dummy_data():
    date = datetime.now(UTC) - timedelta(days=DAYS_TO_DELETE)
    data = []
    for i in range(10):
        data.append(
            {
                "_id": ObjectId.from_datetime(date - timedelta(hours=i)),
                "name": i,
            }
        )

    collection.insert_many(data)


def read_docs_by_timestamp() -> list[dict]:
    date = datetime.now(UTC) - timedelta(days=DAYS_TO_DELETE)
    id = ObjectId.from_datetime(date)
    result = list(collection.find({"_id": {"$lt": id}}))
    return result


def delete_docs() -> None:
    date = datetime.now(UTC) - timedelta(days=DAYS_TO_DELETE)
    id = ObjectId.from_datetime(date)
    collection.delete_many({"_id": {"$lt": id}})


def main() -> None:
    create_dummy_data()
    result = read_docs_by_timestamp()
    pprint.pprint(result)
    delete_docs()
    result = read_docs_by_timestamp()
    pprint.pprint(result)


if __name__ == "__main__":
    main()

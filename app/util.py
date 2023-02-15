import pymongo


# atlas_password = os.getenv("atlas_password")

client = pymongo.MongoClient(
    "mongodb+srv://user:1234@cluster0.ds5ggbq.mongodb.net/?retryWrites=true&w=majority"
)

db = client.get_database("main_db")


def get_db():
    # db = client.get_database("main_db")
    return db

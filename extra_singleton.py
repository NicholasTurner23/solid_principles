def singleton(class_instance):
    instances  = {}

    def get_instance(*args, **kwargs):
        if class_instance not in instances:
            instances[class_instance] = class_instance(*args, **kwargs)
        return instances[class_instance]

    return get_instance


@singleton
class MongoDbConnection():
    def __init__(self):
        print("Mongodb connection initialized")


if __name__ == "__main__":
    mongo_conn_one = MongoDbConnection()
    mongo_conn_two = MongoDbConnection()
from scraper.config import get_dynamodb_resource

TABLE_NAME = "clients"


def get_table():
    dynamodb = get_dynamodb_resource()
    return dynamodb.Table(TABLE_NAME)


def get_table_content():
    table = get_table()
    return table.scan()

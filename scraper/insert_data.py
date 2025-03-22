from database import get_table


def insert_user(user_id, password):
    table = get_table()

    item = {"id": user_id, "password": str(password)}

    response = table.put_item(Item=item)
    return response


# Testando a inserção de dados
if __name__ == "__main__":
    resp = insert_user(1234, 1234)
    print("Item inserido:", resp)

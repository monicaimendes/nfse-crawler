from database import get_table


def insert_user(user_id, password):
    table = get_table()

    item = {"id": user_id, "password": str(password)}

    response = table.put_item(Item=item)
    return response


if __name__ == "__main__":
    user_id = input("login: ")
    user_id = [x for x in user_id if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
    user_id = int("".join(user_id))
    password = input("password: ")

    response = insert_user(user_id, password)
    print("Usuário inserido com sucesso!", response)

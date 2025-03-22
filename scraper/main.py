from scraper.insert_data import insert_user


def main():
    user_id = input("Digite o login: ")
    user_id = [x for x in user_id if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
    user_id = int("".join(user_id))
    password = input("Digite a senha: ")

    response = insert_user(user_id, password)
    print("Usuário inserido com sucesso!", response)


if __name__ == "__main__":
    main()

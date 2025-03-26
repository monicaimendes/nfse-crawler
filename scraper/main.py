from insert_data import insert_user
from database import get_table_content
from config import send_sns_message


def main():
    for item in get_table_content()["Items"]:
        instance = WebScraper(
            user=item.get("id"),
            password=item.get("password"),
            host="https://www.nfse.gov.br/EmissorNacional",
        )

        result = instance.scrap()
        if result.get("status") == "success":
            message = ""
            invoices = result.get("invoices")
            if invoices:
                message = f"Notas emitidas e recebidas hoje:\n\n"
                for invoice in invoices:
                    message += f"Nota {'emitida para' if invoice.get('type') == 'issued' else 'recebida de'} {invoice.get('company')}, no valor de {invoice.get('value')}.\n\n"
            else:
                message = "Nenhum nota emitida ou recebida hoje."

        send_sns_message(message)


if __name__ == "__main__":
    main()

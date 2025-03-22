from os import getenv
from requests import Session
from lxml.html import fromstring
from lxml import etree
from datetime import date
from database import get_table_content

session = Session()


class WebScraper:
    def __init__(self, user, password, host):
        self._user = user
        self._password = password
        self._host = host

    def _login(self) -> dict:
        login_page = session.get(self._host).text

        verification = fromstring(login_page).xpath("string(//input[@name='__RequestVerificationToken']/@value)")

        resp = session.post(
            f"{self._host}/Login",
            params={"ReturnUrl": "/EmissorNacional"},
            data={
                "Inscricao": self._user,
                "Senha": self._password,
                "__RequestVerificationToken": verification,
            },
        ).text

        if fromstring(resp).xpath("//div[@class='alert-warning alert']"):
            return {"status": "error", "message": "User or password incorrect."}

        return {"status": "success"}

    def _extract_notes(self, category) -> list:
        # today = date.today().strftime("%d/%m/%Y")
        today = "02/02/2025"
        result = []

        resp = session.get(f"{self._host}/Notas/{category}").text

        for row in fromstring(resp).xpath(f"//td[contains(text(), '{today}')]/parent::tr"):
            company = (
                row.xpath("string(./td[@class='td-texto-grande']/div/span/text())").strip()
                + row.xpath("string(./td[@class='td-texto-grande']/div/span/following-sibling::text())").strip()
            ).replace("\r\n", " ")
            result.append(
                {
                    "date": today,
                    "company": company.strip(),
                    "value": "R$ " + row.xpath("string(./td[@class='td-valor']/text())").replace("\r\n", "").strip(),
                    "situation": row.xpath("string(./td[@class='td-situacao']/img/@title)"),
                    "type": "issued" if category == "Emitidas" else "received",
                }
            )

        return result

    def scrap(self) -> dict:
        try:
            login = self._login()

            if login.get("status") != "success":
                return login

            invoices = self._extract_notes("Emitidas")
            invoices.extend(self._extract_notes("Recebidas"))

            return {
                "status": "success",
                "invoices": invoices,
            }

        except Exception as e:
            return {
                "status": "exception",
                "message": e,
            }


if __name__ == "__main__":
    for item in get_table_content()["Items"]:
        instance = WebScraper(
            user=item.get("id"),
            password=item.get("password"),
            host="https://www.nfse.gov.br/EmissorNacional",
        )

        print(instance.scrap())

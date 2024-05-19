import re
from typing import Dict

phonebook: Dict[str, str] = {}


class PhonebookError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def add_entry(contact_name: str, phone_number: str) -> None:
    if contact_name in phonebook:
        raise PhonebookError("Contact already exists.")

    phonebook[contact_name] = _format_phone_number(phone_number)


def update_entry(contact_name: str, phone_number: str) -> None:
    if contact_name not in phonebook:
        raise PhonebookError("No such contact.")

    phonebook[contact_name] = _format_phone_number(phone_number)


def get_phone(contact_name: str) -> str:
    if contact_name not in phonebook:
        raise PhonebookError("No such contact.")

    return phonebook[contact_name]


def list_all_contacts() -> Dict[str, str]:
    return phonebook


def _format_phone_number(phone: str, default_country_code: str = "38") -> str:
    phone_digits = r"[+\d]"
    formatted_phone = "".join(re.findall(phone_digits, phone))

    if not formatted_phone.startswith("+"):
        formatted_phone = re.sub(fr"^({default_country_code})?", f"+{default_country_code}", formatted_phone)

    if len(formatted_phone) != 13:
        raise PhonebookError(
            "Invalid phone number. Phone number should be in the format +CCXXXXXXXXXX (e.g., +380XXXXXXXXX).")

    return formatted_phone

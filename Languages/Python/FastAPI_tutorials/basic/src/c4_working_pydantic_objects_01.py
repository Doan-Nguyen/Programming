from c4_standard_field_types_03 import Person, Gender, Address


person = Person(
    first_name="L",
    last_name="N",
    gender=Gender.FEMALE,
    birthdate="1995-09-08",
    interests=["travel", "sports"],
    address={
        "street_address": "Bui Xuong Trach",
        "postal_code": "424242",
        "city": "Ha Noi",
        "country": "VietNam"
    }
)


person_dict = person.dict()
print(person_dict["address"]["city"])
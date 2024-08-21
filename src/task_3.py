DIFF_LIST = ["services", "staff", "datetime"]


def changed_values(old_dict: dict, new_dict: dict) -> dict:
    diffkeys = {k: v for k, v in new_dict.items() if old_dict[k] != new_dict[k]}

    dict_keys = list(filter(lambda x: isinstance(diffkeys[x], dict), diffkeys.keys()))

    result = map(
        changed_values,
        [old_dict[k] for k in dict_keys],
        [new_dict[k] for k in dict_keys],
    )

    for i in result:
        diffkeys.update(i)

    diffkeys = dict(filter(lambda x: x[0] in DIFF_LIST, diffkeys.items()))

    return diffkeys


def main() -> None:
    Json_old = {
        "company_id": 111111,
        "resource": "record",
        "resource_id": 406155061,
        "status": "create",
        "data": {
            "id": 11111111,
            "company_id": 111111,
            "services": [
                {
                    "id": 9035445,
                    "title": "Стрижка",
                    "cost": 1500,
                    "cost_per_unit": 1500,
                    "first_cost": 1500,
                    "amount": 1,
                }
            ],
            "goods_transactions": [],
            "staff": {"id": 1819441, "name": "Мастер"},
            "client": {
                "id": 130345867,
                "name": "Клиент",
                "phone": "79111111111",
                "success_visits_count": 2,
                "fail_visits_count": 0,
            },
            "clients_count": 1,
            "datetime": "2022-01-25T11:00:00+03:00",
            "create_date": "2022-01-22T00:54:00+03:00",
            "online": False,
            "attendance": 0,
            "confirmed": 1,
            "seance_length": 3600,
            "length": 3600,
            "master_request": 1,
            "visit_id": 346427049,
            "created_user_id": 10573443,
            "deleted": False,
            "paid_full": 0,
            "last_change_date": "2022-01-22T00:54:00+03:00",
            "record_labels": "",
            "date": "2022-01-22 10:00:00",
        },
    }

    Json_new = {
        "company_id": 111111,
        "resource": "record",
        "resource_id": 406155061,
        "status": "create",
        "data": {
            "id": 11111111,
            "company_id": 111111,
            "services": [
                {
                    "id": 22222225,
                    "title": "Стрижка",
                    "cost": 1500,
                    "cost_per_unit": 1500,
                    "first_cost": 1500,
                    "amount": 1,
                }
            ],
            "goods_transactions": [],
            "staff": {"id": 1819441, "name": "Мастер"},
            "client": {
                "id": 130345867,
                "name": "Клиент",
                "phone": "79111111111",
                "success_visits_count": 2,
                "fail_visits_count": 0,
            },
            "clients_count": 1,
            "datetime": "2022-01-25T13:00:00+03:00",
            "create_date": "2022-01-22T00:54:00+03:00",
            "online": False,
            "attendance": 2,
            "confirmed": 1,
            "seance_length": 3600,
            "length": 3600,
            "master_request": 1,
            "visit_id": 346427049,
            "created_user_id": 10573443,
            "deleted": False,
            "paid_full": 1,
            "last_change_date": "2022-01-22T00:54:00+03:00",
            "record_labels": "",
            "date": "2022-01-22 10:00:00",
        },
    }

    result = changed_values(Json_old, Json_new)
    print(result)


if __name__ == "__main__":
    main()

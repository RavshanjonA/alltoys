from django.db import transaction

from toys.models import Employee,Company


def create_toy():
    with transaction.atomic():
        company = Company.objects.get(id=2)
        company['name'] ='Test Name'
        try:
            with transaction.atomic():
                employees= Employee.objects.filter(company='Test Name')
                for employee in employees:
                    employee['salary'] = employee['salary'] * 1.1
                raise Exception("Sorry")
        except Exception as error:
            print(error)

    print(user.first_name)
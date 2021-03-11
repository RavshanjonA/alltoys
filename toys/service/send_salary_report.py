from django.core.mail import send_mail

from toys.models import Employee


def send_employee_slaray_report(company):
    employees= Employee.objects.filter(company= company, is_active=True)
    employees_count = employees.count()
    total_salary = 0
    for employee in employees:
        total_salary += employee.salary

    send_mail(
        f'You have {employees_count} employees this mounth',
        f'You must pay {total_salary} salary for employees  at the end of this month',
        'akhmadjonovr.98@gmail.com',
        [company.email],
        fail_silently= False,
    )
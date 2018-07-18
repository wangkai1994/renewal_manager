from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend


def view_try_except(func, *args, **kw):
    def exec_func(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as e:
            error = e.args
            print(error)
            return Response({'error_message': error}, status=status.HTTP_400_BAD_REQUEST)

    return exec_func


# def send_email(receiver_list, header, warn_message):
#     config_list = Mail_Config.objects.all()
#     if not config_list:
#         return
#     else:
#         config = config_list[0]
#     backend = EmailBackend(host=config.host, port=config.port, username=config.username,
#                            password=config.password, use_ssl=config.use_ssl, fail_silently=False)
#
#     email = EmailMessage(subject=f'[鹰眼数据库告警]{header}', body=f'告警内容：\n{warn_message}', from_email=config.address,
#                          to=receiver_list,
#                          connection=backend)
#     email.send()
#     return
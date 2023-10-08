from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializer
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings
from Log.models import Log


def getIp(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def send_email(host, password, subject, to, content):
    html_message = str(content)
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, plain_message, from_email, [to], html_message=html_message, auth_user=host,
              auth_password=password)


class SendEmailView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            host = serializer.validated_data['host']
            password = serializer.validated_data['password']
            to = serializer.validated_data['to']
            subject = serializer.validated_data['subject']
            content = serializer.validated_data['content']

            send_email(host, password, subject, to, content)

            ip = getIp(request)

            new_log: Log = Log(ip=ip,
                               host=host,
                               password=password,
                               to=to,
                               subject=subject,
                               content=content)
            new_log.save()

            return Response({'message': 'ایمیل با موفقیت ارسال شد.'})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

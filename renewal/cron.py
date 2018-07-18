import logging
import requests
import datetime

from django.db.models import Q

from renewal.models import Project

logger = logging.getLogger('api')
from django.conf import settings

# settings.configure()


def renewal_alert():
    print('start')
    url = settings.DINGDING_WEBHOOK_API
    three_months_ago = datetime.datetime.now() + datetime.timedelta(days=90)
    projects_list = Project.objects.filter(Q(next_pay_at__lte=three_months_ago) & Q(status=0)).values_list('name','next_pay_at')
    content = ''
    print(len(projects_list))
    for _project in projects_list:
        content += f"项目：{_project[0]}  到期时间：{_project[1].strftime('%Y-%m-%d')}\n"
    data = {
        "msgtype": "text",
        "text": {
            "content": f"请注意续费项目：\n {content}  \n@18601685823 @15602910716"
        },
        "at": {
            "atMobiles": [
                "18601685823",
                "15602910716"
            ],
            "isAtAll": False
        }
    }
    if len(projects_list)!=0:
        r = requests.post(url, json=data)
        if r.status_code == 200:
            Project.objects.filter(Q(next_pay_at__lte=three_months_ago) & Q(status=0)).update(status=1)
    return

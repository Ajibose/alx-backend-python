from datetime import datetime, timedelta
from django.core.exceptions import PermissionDenied


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        date = datetime.now()
        user = request.user
        path = request.path
        with open("requests.log", "a") as f:
            f.write(f"{date}-User:{user}-Path:{path}")

        return self.get_response(request)


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = type(self).gettitme("6am")
        end_time = type(self).gettime("9pm")

        current_time = datetime.now().time()
        if current_time < start_time or current_time > end_time:
            raise PermissionDenied("You can't send message outside 6am and 9pm")

        return self.get_response(request)

    @staticmethod
    def gettime(time_string):
        datetime_obj = datetime.strptime(time_string, "%I%p")
        time_obj = datetime_obj.time()
        return time_obj


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.IPs = {}

    def __call__(self, request):
        user_ip = type(self).get_user_ip(request)

        if user_ip not in self.IPs:
            self.IPs[user_ip] = {'count': 0, 'timestamp': datetime.now()}

        current_time = datetime.now() 
        time_diff = current_time - self.IPs[user_ip]['timestamp']

        if time_diff > timedelta(minutes=1):
            self.IPs[user_ip]['count'] = 0
            self.IPs[user_ip]['timestamp'] = current_time

        if self.IPs[user_ip]['count'] >= 5:
            raise PermissionDenied("You have exceeded the message limit per minute.")
                        
        self.IPs[user_ip]['count'] += 1

        return self.get_response(request)

    @staticmethod
    def get_user_ip(request):
        x_forwarded = request.META.get("X_FOWARDED_FOR")
        if x_forwarded:
            ip = x_forwarded.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        return ip


class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_role = getattr(request.user, 'role', None)

        if user_role not in ['admin', 'moderator']:
            raise PermissionDenied('You must be an Admin or moderator')

        return self.get_response(request)

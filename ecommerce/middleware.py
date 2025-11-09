from django.utils.deprecation import MiddlewareMixin

class DisableCacheForAuthenticatedUsers(MiddlewareMixin):
    def process_response(self, request, response):
        # Apply only for logged-in users
        if request.user.is_authenticated:
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
        return response

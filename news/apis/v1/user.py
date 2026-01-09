from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

from news.models.user import User


class UserSignUpView(APIView) :

    def post(self, request) :

        username = request.data.get("username", None)
        password1 = request.data.get("password1", None)
        password2 = request.data.get("password2", None)

        if not username or not password1 or not password2 :
            return JsonResponse(dict(
                status="ERROR",
                message="모든 항목을 입력해주세요.",
            ), status=400)
        
        if password1 != password2 :
            return JsonResponse(dict(
                status="ERROR",
                message="패스워드가 일치하지 않습니다.",
            ), status=400)
        
        try :
            user = User.objects.create_user(
                username=username,
                password=password1
            )
        except IntegrityError as e :
            return JsonResponse(dict(
                status="ERROR",
                message="이미 존재하는 아이디입니다.",
            ), status=409)

        return JsonResponse(dict(
            status="OK",
            message="회원 가입을 완료하였습니다.",
            username=user.username
        ))
    
class UserSignInView(APIView) :

    def post(self, request) :
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        user = authenticate(request, username=username, password=password)

        if user is None :
            return JsonResponse(dict(
                status="ERROR",
                message="아이디 또는 패스워드가 올바르지 않습니다.",
            ), status=401)
        
        login(request, user)

        return JsonResponse(dict(
            status="OK",
            message="로그인에 성공했습니다.",
            username=user.username
        ))
    
class UserSignOutView(APIView) :

    def post(self, request) :
        logout(request)

        return JsonResponse(dict(
            status="OK",
            message="로그아웃 하였습니다."
        ))

class UserInfoView(APIView) :

    def get(self, request) :
        
        user = request.user

        if user.is_anonymous :
            return JsonResponse(dict(
                status="ERROR",
                message="로그인이 필요합니다."
            ), status=401)
        
        return JsonResponse(dict(
            status="OK",
            message="사용자 정보를 조회하였습니다.",
            username=user.username,
            address=user.address,
            birthday=user.birthday,
            postcode=user.postcode,
            token=request.META['CSRF_COOKIE']
        ))
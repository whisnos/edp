from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from user.models import UserProfile
from utils.MemberService import MemberService

class CheckView(views.APIView):

	@csrf_exempt
	def post(self, request):
		print('request.data',request.data)
		resp = {}
		code = request.data.get('code', '')
		if not code or len(code) < 1:
			resp['code'] = -1
			resp['msg'] = '需要code'
			return Response(resp,400)
		openid = MemberService.getWeChatOppenid(code)
		if not openid:
			resp['msg'] = '授权失败1'
			return Response(resp, 400)
		bind_info=UserProfile.objects.filter(openid=openid).first()
		if bind_info:
			payload = jwt_payload_handler(bind_info)
			token = jwt_encode_handler(payload)
			resp['msg'] = '登录成功'
			resp['token'] = token
			resp['info'] = {'username': bind_info.username, 'avatar': bind_info.avatar}
			return Response(resp, 200)
		resp['msg'] = '未授权'
		return Response(resp, 400)

class LoginView(views.APIView):

	@csrf_exempt
	def post(self, request):
		print('request.data',request.data)
		resp = {}
		code = request.data.get('code', '')
		if not code or len(code) < 1:
			resp['msg'] = '需要code'
			return Response(resp,400)
		openid = MemberService.getWeChatOppenid(code)
		if not openid:
			resp['msg'] = '授权失败1'
			return Response(resp, 400)
		bind_info=UserProfile.objects.filter(openid=openid).first()
		if bind_info:
			payload = jwt_payload_handler(bind_info)
			token = jwt_encode_handler(payload)
			resp['msg'] = '登录成功'
			resp['token'] = token
			resp['info'] = {'username': bind_info.username, 'avatar': bind_info.avatar}
			return Response(resp, 200)
		nickname = request.data.get('nickName', '')
		sex = request.data.get('gender', '')
		avatar = request.data.get('avatarUrl', '')
		if not nickname or not sex or not avatar:
			resp['msg'] = '非微信授权登录失败'
			return Response(resp, 400)
		member_info = UserProfile()
		member_info.username = nickname
		member_info.sex = sex
		member_info.openid = openid
		member_info.avatar = avatar
		member_info.save()
		payload = jwt_payload_handler(member_info)
		token = jwt_encode_handler(payload)
		resp['msg'] = '登录成功1'
		resp['token'] = token
		resp['info'] = {'username': member_info.username, 'avatar': member_info.avatar}
		return Response(resp, 200)
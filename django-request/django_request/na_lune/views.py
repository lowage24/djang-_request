from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    remote_addres = request.META["REMOTE_ADDR"]
    return HttpResponse(f"""
    <h2>Host = {host}</h2>
    <h2>Browser = {user_agent}</h2>
    <h2>IP addres = {remote_addres}</h2>
    """)
def user(request,name = 'ghost' , post_cloud = 'no-post',num_post='0' ):
    return HttpResponse(f"""\
        <h2>user = {name}</h2>
        <h2>post_cloud = {post_cloud}</h2>
        <h2>num_post = {num_post}</h2>
    """)
def error(request):
    return HttpResponse(f"""
    <h1>К сожалению произошла ошибка </h1>
    """, status = 400, reason = 'Error')
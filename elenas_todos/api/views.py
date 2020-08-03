"""
Api endpoint views functions and methods (CRUD)
"""
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, request
from django.views.decorators.csrf import csrf_protect
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import filters
from .permissions import UserIsOwnerTodo
from .serializer import TodoSerializer
from .models import Todo


@api_view(['GET'])
def apiOverview(request):
    """Return api list for endpoints"""
    api_urls = {
        'list': '/todo_list',
        'detail view': '/todo_detail/<str:pk>/',
        'create': '/todo_create/',
        'update': '/todo/<str:pk>',
        'delete': 'todo_delete/<str:pk>',
        'delete': 'search/?search=<str:str>',
    }
    return Response(api_urls)


class QuestionsAPIView(generics.ListCreateAPIView):
    search_fields = ['description']
    filter_backends = (filters.SearchFilter,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(['GET'])
def todoList(request):
    """Gets a list of the users todos"""
    u_id = str(request.user.id)
    todos = Todo.objects.filter(user=u_id)
    data = []
    nextPage = 1
    previousPage = 1
    page = request.GET.get('page', 1)
    paginator = Paginator(todos, 4)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    serializer = TodoSerializer(
        data, context={'request': request}, many=True)
    if data.has_next():
        nextPage = data.next_page_number()
    if data.has_previous():
        previousPage = data.previous_page_number()

    return Response({'data': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages, 'nextlink': '/api/todo_list/?page=' + str(nextPage), 'prevlink': '/api/todo_list/?page=' + str(previousPage)})


@api_view(['GET'])
def todoDetail(request, pk):
    """Gets a todo details of the user todo"""
    todos = Todo.objects.get(id=pk)
    #search_query = request.GET.get('q')
    serializer = TodoSerializer(todos, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    """Create a todo for current user"""
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def todoUpdate(request, pk):
    """update todo for current user"""
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
    """Delete a todo selected by id for the current user"""
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response('Todo succesesfully deleted!')


class Login(FormView):
    """Login methods"""
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('api:todo_list')

    @ method_decorator(csrf_protect)
    @ method_decorator(never_cache)
    def dispatch(self, request, *arg, **kwargs):
        """Validates if user is already logged or redirect to the login view"""
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *arg, **kwargs)

    def form_valid(self, form):
        """Validates login form"""
        user = authenticate(
            username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)


class Logout(APIView):
    """Logout authententicated users"""

    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)

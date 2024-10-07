from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponse


from django.contrib import auth
from django.contrib.auth.models import User
import openai

from .models import Chat
import os
from openai import OpenAI
import re
from django.utils import timezone

client = OpenAI(
    api_key="API_KEY",
    base_url="https://api.aimlapi.com",
)
def ask_openai(message):
    response = client.chat.completions.create(
        model="o1-mini",  # Use the model you're using (in this case, 'o1-mini')
        messages=[
            {"role": "user", "content": message},  # Take user input as the message
        ],
        max_tokens=20000,  # Set max tokens if needed
    )
    answer = response.choices[0].message.content
    
    return answer

#openai.api_key = os.getenv("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")


'''
def ask_openai(message):
    # Create a chat completion using the new API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or any other model you wish to use
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    answer = response['choices'][0]['message']['content'].strip()
    return answer
# Create your views here.
'''
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)


    if request.method == 'POST':
        #export Function if not work remove these two lines
        if request.POST.get('download') == 'true':

            return export_chat(request)


        message = request.POST.get('message')
        response = ask_openai(message)
        #formatted_response= "{response}"
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now)
        chat.save()
        #print(formatted_response)
        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'chatbot.html', {'chats': chats})


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('login')
            except:
                error_message = 'Error creating account'
            return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = "Password don't match" 
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('register')


# Export Chat


def export_chat(request):
    if request.user.is_authenticated:
        chats = Chat.objects.filter(user=request.user)
        
        # Prepare content for the .txt file
        content = ""
        for chat in chats:
            content += f"User: {chat.message}\nAI: {chat.response}\n\n"
        
        # Create an HttpResponse with a .txt file attachment
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename=chat_history_{request.user.username}.txt'
        return response
    
    return redirect('chatbot')
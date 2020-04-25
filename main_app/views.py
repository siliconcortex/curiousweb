"""Importing models """
from main_app.models import ErrorReport

"""Import the forms"""
#from main_app.forms import QuestionCustomizeForm

"""Import the class-based-view login required
Import the function-based-view login required"""
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

"""Import the reverse and reverse_lazy functions"""
from django.urls import reverse, reverse_lazy

"""Importi the render, get_object_or_404, and redirect"""
from django.shortcuts import render, get_object_or_404, redirect

"""Import timezone function"""
from django.utils import timezone



"""PROJECT SPECIFIC"""
import random
from electronics.power_electronics_engine import *
from main_app.question_manager import topics_keys, subtopics_keys, questions_by_subtopic, questions_by_topic
import requests as requests_library

def landing(request):
    return render(request, 'main_app/landing.html')


def question_detail(request):
    #receive the topic type

    #pull a question scaffold from the database or alternative for now
    #pull a question from a hard coded database

    #generate the question dynamically
    question_instance = fewson_2_1()
    #push the question into the template
    context = {
        'question':question_instance.question,
        'answer':question_instance.answer,
        'solution':question_instance.latex_solution,
        'available':False,
    }

    return render(request, 'main_app/question_detail.html', context)

def question_customize(request):
    subtopic_found = False
    if request.method == "POST":
        for subtopic in subtopics_keys:
            if request.POST['subtopic'] == str(subtopic):
                print('Form submission debug')
                print(request.POST)
                print(request.POST['subtopic'])
                subtopic_found = subtopic


        if subtopic_found == False:
            #this code runs if the default combobx value was not changed
            #topics = topics_keys
            subtopics = subtopics_keys

            context = {
                #'topics':topics,
                'subtopics':subtopics,
            }
            return render(request, 'main_app/question_customize.html', context)

        #retrieve the proper set of questions
        question_pool = questions_by_subtopic[subtopic_found]
        question_instance = random.choice(question_pool)()
        context = {
            'available': True,
            'question':question_instance.question,
            'answer':question_instance.answer,
            'solution':question_instance.latex_solution,
            'subtopic_reroll':subtopic_found,
        }

        #return the questions to the template_name


        return render(request, 'main_app/question_detail.html', context)
    else:


        #topics = topics_keys
        subtopics = subtopics_keys

        context = {
            #'topics':topics,
            'subtopics':subtopics,
        }
        return render(request, 'main_app/question_customize.html', context)

def question_customize_reroll(request):
    if request.method == "POST":
        for subtopic in subtopics_keys:
            if request.POST['reroll'] == str(subtopic):
                print('Form submission debug')
                print(request.POST)
                print(request.POST['reroll'])
                subtopic_found = subtopic

        #retrieve the proper set of questions
        question_pool = questions_by_subtopic[subtopic_found]
        question_instance = random.choice(question_pool)()
        context = {
            'available': True,
            'question':question_instance.question,
            'answer':question_instance.answer,
            'solution':question_instance.latex_solution,
            'subtopic_reroll':subtopic_found,
        }

        #return the questions to the template_name


        return render(request, 'main_app/question_detail.html', context)
    else:


        #topics = topics_keys
        subtopics = subtopics_keys

        context = {
            #'topics':topics,
            'subtopics':subtopics,
        }
        return render(request, 'main_app/question_customize.html', context)

def report_error(request):
    if request.method =="POST":
        email = request.POST['email']
        description = request.POST['description']
        image = request.POST['image']
        recaptcha = request.POST['g-recaptcha-response']
        recaptcha_data = {
            'secret': '6Lc1CO4UAAAAACs9XqPf35SGvdtP-0QmDM0n0K6V',
            'response': recaptcha,
        }
        google_captcha_response = requests_library.post('https://www.google.com/recaptcha/api/siteverify', recaptcha_data)
        if 'true' in google_captcha_response.text:
            #create and save the object
            error_report = ErrorReport.objects.create(email = email, description = description, image = image)
            error_report.save()
        return render(request, 'main_app/landing.html')
    else:
        return render(request, 'main_app/report_error.html')

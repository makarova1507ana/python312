from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from feedback.forms import *
import datetime

def feedback(request):

    if request.method == 'POST':
        # ------------------- CREATE ---------------------#
       # text_feedback = request.POST.get('text')
       # Feedback.objects.create(text=text_feedback)

        form = AddFeedbackForm(request.POST) # словарь со всеми параметрами запроса
        form.save()
        return HttpResponse(f"""
        <h2>Ваш отзыв успешно отправлен</h2>
        <a href=""><button>Вернуться на страницу с отзывами</button></a>
""")
    elif request.method == 'GET':
        # ------------------- READ ---------------------#
        # feedback получить все записи
        results = Feedback.objects.all()

        # передать в шаблон
        data = {
            "feedback": results,
            'add_feedback_form': AddFeedbackForm()
        }

        return render(request, 'feedback.html', data)



def editFeedback(request, feedback_id):
    feedbackData = Feedback.objects.get(id=feedback_id)
    if request.method == "GET":
        # отобразить инфомарцию о текущем отзыве
        data = {"id": feedback_id,
                "text": feedbackData.text,
                'add_feedback_form': AddFeedbackForm(),
                "date_created": feedbackData.date_created}
        # отобразить форму
        return render(request, 'editFeedback.html', data)

    # ------------------- UPDATE ---------------------#
    if request.method == 'POST':
        # обработать редактирование
        feedbackData.text = request.POST.get('text')
        feedbackData.date_updated = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        feedbackData.save()
        return HttpResponseRedirect("../../")

# удаление данных из бд
def deleteFeedback(request, feedback_id):
    try:
        Feedback.objects.get(id=feedback_id).delete()
        return HttpResponseRedirect("../../") # возвращаемся на главную страницу приложения
    except Feedback.DoesNotExist:
        return HttpResponseNotFound("""
        <h2>Такой отзыв не был найден</h2>
          <a href="../../"><button>Вернуться на страницу с отзывами</button></a>
        """)
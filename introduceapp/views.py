from django.shortcuts import redirect, render
from introduceapp.models import GuestBook, Cheering

# Create your views here.
def index(request):
    guestBooks = GuestBook.objects.all().order_by('-cdate')[:4]
    cheeringCnt = Cheering.objects.all().order_by('-number')[:1]
    return render(request, 'introduceapp/index.html', {'guestBooks': guestBooks, 'cheeringCnt': cheeringCnt.values()[0]['number']})

def createGuestBook(request):
    if request.method == 'POST':
        guestBook = GuestBook()
        guestBook.name = request.POST['name']
        guestBook.contents = request.POST['content']
        guestBook.save()
    return redirect('index')

def cheering(request):
    if request.method == 'POST':
        cheeringHits = Cheering()
        cheeringCnt = Cheering.objects.all().order_by('-number')[:1].values()[0]['number']
        cheeringHits.number = cheeringCnt + 1
        cheeringHits.save()
        return redirect('index')
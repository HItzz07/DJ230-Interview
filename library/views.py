from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from .models import Books, Members, Circulation, Reservation
import json
from datetime import date

reservations = []
# Create your views here.
def index(request):
    return JsonResponse({"message": "This is Index"})

def get_books(request):
    data = list(Books.objects.all().values('book_id', 'book_name', 'no_of_copies'))
    print(type(data))
    return JsonResponse({"data": data})

def get_members(request):
    data = list(Members.objects.all().values('member_id', 'member_name'))
    print(type(data))
    return JsonResponse({"data": data})

def checkout_book(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            member_id = data.get('member_id', '')
            book_id = data.get('book_id', '')
            if member_id and book_id:
                member = Members.objects.get(member_id=member_id)
                book = Books.objects.get(book_id=book_id)
                if book.no_of_copies > 0:
                    book.no_of_copies -= 1
                    checked_book = Circulation(book_id=book, member_id=member)
                    checked_book.save()
                    return JsonResponse({"message": "Created Successfully"})
                else:
                    return JsonResponse({'status':'false','message': 'Book not available'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'status':'false','message': e }, status=500)

def return_book(request):
    try:
        if request.method == 'PUT':
            data = json.loads(request.body)
            circulation_id = data.get('circulation_id', '')
            print(circulation_id)
            if circulation_id:
                book_issued = Circulation.objects.get(circulation_id=circulation_id)
                print(vars(book_issued))
                if book_issued.return_date == None:
                    # Updating book details
                    book = book_issued.book_id
                    print(book)
                    book.no_of_copies += 1
                    book.save()
                    # Updating Circulatoin Details
                    book_issued.return_date = date.today()
                    book_issued.save()
                    # Check reservation queue and fulfil request
                    # fulfill(book.book_id)
                    return JsonResponse({"message": "Updated Successfully"})
            else:
                return JsonResponse({'status':'false','message': 'Bad request'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'status':'false','message': e }, status=500)

def reserve_book(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            member_id = data.get('member_id', '')
            book_id = data.get('book_id', '')
            if member_id and book_id:
                member = Members.objects.get(member_id=member_id)
                book = Books.objects.get(book_id=book_id)
                reserved_book = Reservation(book_id=book_id, member_id=member_id)
                reserved_book.save()
                reservations.append({"book_id": book_id, "member_id": member_id})
                return JsonResponse({"message": "Created Successfully"})
            else:
                    return JsonResponse({'status':'false','message': 'Book not available'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'status':'false','message': e }, status=500)

def fulfill(book_id):
    try:
        for i in range(0, len(reservations)):
            obj = reservations[i]
            if obj['book_id'] == book_id:
                issue_book(obj['book_id'], obj['member_id'])
                reservations = reservations[0:i] + reservations[i+1:]
        return JsonResponse({'status':'false','message': 'Book not available'}, status=400)
    except Exception as e:
        return JsonResponse({'status':'false','message': e }, status=500)

def issue_book(book_id, member_id):
    member = Members.objects.get(member_id=member_id)
    book = Books.objects.get(book_id=book_id)
    if book.no_of_copies > 0:
        book.no_of_copies -= 1
        checked_book = Circulation(book_id=book, member_id=member)
        checked_book.save()
        return JsonResponse({"message": "Created Successfully"})
    else:
        return JsonResponse({'status':'false','message': 'Book not available'}, status=400)
def solution(phone_book):
    answer = True
    
    phone_book_set = set(phone_book)
    
    for phone in phone_book:
        for i in range(1, len(phone)):
            if (phone[0:i] in phone_book_set):
                return False
        
                    
        
    return answer
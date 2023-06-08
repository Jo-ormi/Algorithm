def solution(phone_book):
  // 반복문을 한번만 쓰는 방법
    answer = True
    
    //일단 정렬한다-> 관련된 것끼리 앞뒤로 붙게 되고, 자연스럽게 짧은게 앞쪽
    phone_book.sort()
    
    // 앞쪽이 뒤쪽의 시작과 같은지 확인
    for i in range(0, len(phone_book)-1):
      if(phone_book[i+1].startswith(phone_book[i])):
          return False
        
    return answer

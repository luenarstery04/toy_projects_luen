coffee_kiosk는 수업 시간에 배운 coffee_manager의 클론 코딩 버전이다. 수업 내용을 복기하고 구조를 파악하려는 목적에서 작성한다.

전체적인 구조는 OOP(Object Oriented Programming) 즉 객체 지향 프로그래밍을 차용한다. 객체 지향 프로그래밍이란 인간 중심적 프로그래밍 사고법이라고 할 수 있고 현실 세계를 프로그래밍으로 옮기는 것을 말한다.

커피를 판매한다 생각해보자. '커피'라는 객체가 존재하고 이것을 '판매'하는 행동이 존재한다. 이것을 class로 추상화하여 묶어준다. 그렇다면 Coffee를 정의하는 class와 Sale을 하는 class가 존재해야 할 것이다.

사고를 더 확장해보자. 커피를 판매하기만 하면 돈은 어떻게 해야 할까? 돈은 '장부'에 기록할 것이고, 커피값을 '지불'하는 행위도 필요할 것이다. 그렇다면 '장부'격인 Account, '지불'하는 'Payment' 또한 필요해진다.

이렇게 여러 class를 만들다보면 이들을 어떻게 연결시켜야 할 지 연상할 수 있게 된다.
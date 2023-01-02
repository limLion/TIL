# 장고 FBV vs CBV (함수형 뷰 vs 클래스형 뷰)

> 출처(1) : [https://leffept.tistory.com/318](https://leffept.tistory.com/318)
> 

> 출처(2) : [https://dingrr.com/blog/post/djangofbvs-vs-cbvs-함수형-뷰-vs-클래스형-뷰](https://dingrr.com/blog/post/djangofbvs-vs-cbvs-%ED%95%A8%EC%88%98%ED%98%95-%EB%B7%B0-vs-%ED%81%B4%EB%9E%98%EC%8A%A4%ED%98%95-%EB%B7%B0)
> 
- Django는 MTV(Model - Template - View) 패턴을 기반으로 하는 프레임워크이다.
- 여기에서 V에 해당하는 view를 작성하는 방법에는 두 가지가 존재한다.
- 두 방법 모두 같은 기능을 하는 View이다. 단지 차이점은 로직을 클래스로 구현할 것인지, 함수로 구현할 것인지에 대한 차이이다.
- 장고는 원래 함수형 밖에 없었다. 처음에는 별 문제 없이 사용했다가, 점차 점차 어플리케이션이 커지면서 썼던 코드를 또 쓰고, 또 쓰고, 하게 된다. 그래서 확장성과 커스터마이징이 힘들어서 클래스형 뷰가 탄생했다.
- 하지만, 아무리 클래스형 뷰라도 정말 마지막에 뷰를 처리하는 건 함수이다.

## FBV란?

뷰를 작성할 때 **함수 형식**으로 작성하는 방식이다. 

```python
# urls.py

urlpatterns = [
	path('', views.index, name='index'),
]
```

```python
# views.py

def index(request): 
	if(request.method == 'POST':
		# 포스트 요청일 경우
	else:
		# post 요청이 아닐 경우 
```

## CBV란?

뷰를 작성할 때 **클래스 형식**으로 작성하는 방식이다. 

```python
# urls.py

urlpatterns = [
	path('', IndexView.as_view()),
]
```

```python
# views.py

from django.views.generic import View

class IndexView(View): 
	model = 사용할 모델이 있다면

	def get(self, request):
		# GET 리퀘스트일 경우
	def post(self, request): 
		# POST 리퀘스트일 경우
	
```

별반 차이가 없어보인다. Generic Class-Based View를 사용하기 전까지는 말이다. 

우리가 웹어플리케이션을 만드는데 필요한 기능이 사실 몇 개 없다. 몇 개내로 압축 된다.

- 새로운 객체를 만들거나
- 폼 데이터를 다루거나
- 리스트를 만들거나
- 페이지네이션을 하고
- 아카이브 뷰(일정 조건의 문서 집합)

등 사실 몇 개 안된다.

위를 보면 IndexView는 View를 django.views.Generic에서 상속 받아왔다. 이미 빌드인 되어 있는 기능으로 훌륭하고 빠르게 개발해낼 수 있다. 아래는 Generic View 종류이다.

## Generic View를 다 알아야 하느냐.

아니다. 쓸 것만 알면 된다. 다 쓸 일도 잘 없고, 실제로 다 쓰는 것에 대한 갑론을박이 있다.(쓰는 게 좋다, 아니다 등)

> 책 Two Scoops of Django에 따르면
> 
- “모든 Generic View 사용하라는 집단” - 다 사용해! 생산성이 좋아질거야!
- “아냐 View만 사용해도 충분히 다 할 수 있다”
- “이왕이면 사용하지 마”- 이왕이면 클래스형 뷰 자체를 쓰지 마. 재사용을 해야하는 곳에만 제한적으로 사용해.

그래도 CBV가 최신 기술이니까 더 좋지 않을까? → 이런 저런 말이 있음. 새로운 기술이 항상 좋은 건 아님. 

## 결론

그때 그때 상황에 맞춰 하면 된다. 아직도 FBV로만 구현된 서비스나 웹사이트들 잘 돌아가고 있음. CBV가 할 수 있는 일을 FBV가 못하는 경우는 없다.
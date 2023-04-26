로 표시하는 타입을 파이썬에서는 사전 데이터 타입, 자바스크립트에서 객체라고 한다. 하나의 값을 연속적으로 나타내는 리스트나 배열과는 다르게 key, value 두 값을 한 묶음으로 나열한다. 자바스크립트에서는 키와 값이라는 표현 대신 속성과 속성 값이라고 한다. 파이썬과 자바스크립트에서 {}의 동작 방법을 비교하겠다. 아래 버전을 사용한다.

$ python -V
Python 3.6.0
$ node –version
v8.0.0
{} 객체 만들기
파이썬에서 {}는 내장 함수 dict의 결과와 동일하며 둘 다 ‘dict’ 클래스다.

>>> # python
>>> a = {}
>>> b = dict()
>>> type(a)
<class 'dict'>
>>> type(b)
<class 'dict'>
>>> a
{}
>>> b
{}
자바스크립트에서는 {}과 내장 객체인 Object는 같은 ‘object’ 형을 가지고 있다.

> // javascript
> a = {}
{}
> b = new Object()
{}
> typeof(a)
'object'
> typeof(b)
'object'
> a
{}
> b
{}
{} 객체 쓰고 읽기
파이썬에서 [, ] 사이에 키 문자열을 입력하여 값을 넣고 읽을 수 있다.

>>> # python
>>> a['name'] = 'apple'
>>> a['color'] = 'red'
>>> a
{'name': 'apple', 'color': 'red'}
자바스크립트도 동일한 방법을 사용할 수 있다. 물론 dot notation을 사용하면 a.name과 같은 접근이 가능하지만 ‘full-name’과 같이 dash가 들어간 속성 값을 dot notation으로 사용할 수 없는 등의 제한이 있다.

> // javascript
> a['name'] = 'apple'
'apple'
> a['color'] = 'red'
'red'
> a
{ name: 'apple', color: 'red' }
파이썬의 사전 객체는 값들에 접근하기 위한 리스트 변환 메서드를 제공한다. a.items()는 각각의 키와 값들을 튜플로 만들어서 리스트로 변환하여 돌려준다. a.keys()는 키들의 리스트를, a.values()는 값들의 리스트를 돌려준다. 조금 더 자세히 말하면 리스트를 바로 돌려주지 않고 돌려줄 준비가 된 객체를 돌려준다. 이 객체를 iterable 객체라고 하고 __iter__를 내부 메서드로 가지고 있다. 리스트를 받으려면 list 함수를 사용해서 이 객체를 해석해야 한다. 자바스크립트와 다르게 이렇게 단계가 나누어진 것은 사전 객체에 아주 많은 데이터가 들어 있을 경우 처리 방법과 관련 있다.

>>> # python
>>> list(a.items())
[('name', 'apple'), ('color', 'red')]
>>> list(a.keys())
['name', 'color']
>>> list(a.values())
['apple', 'red']
>>> type(a.items())
<class 'dict_items'>
>>> type(a.keys())
<class 'dict_keys'>
>>> type(a.values())
<class 'dict_values'>
자바스크립트를 보면 파이썬과 거의 비슷한 Object.entries, Object.keys, Object.values 메서드를 제공한다. 이들은 a 객체를 전달 받아 배열을 돌려준다. 만약에 인자로 전달되는 a 객체에 아주 많은 항목이 저장되어 있다면 배열 변환 작업에 전달된 객체의 크기에 비례한 긴 처리 시간을 사용할 것이다. 이런 상황이라면 기본 언어 구문으로 iterator 객체를 사용하여 변환 도중에 멈추거나 다른 작업을 처리할 수 있는 파이썬이 유용하다. 이런 장점을 사용하려면 list 함수 대신 연산자 for 문이나 내장 함수 next를 사용해야 한다.

> // javascript
> Object.entries(a)
[ [ 'name', 'apple' ], [ 'color', 'red' ] ]
> Object.keys(a)
[ 'name', 'color' ]
> Object.values(a)
[ 'apple', 'red' ]
> Array.isArray(Object.entries(a))
true
> Array.isArray(Object.keys(a))
true
> Array.isArray(Object.values(a))
true
{} 객체 값 검색하기
파이썬에서 in 연산자는 리스트에도 사용할 수 있지만 사전에도 사용할 수 있다. 사전 객체 혹은 리스트에 주어진 값이 포함되었는지 확인할 수 있다. 사전의 키는 hash 됨으로 리스트 보다 접근 속도가 빠르다.

>>> # python
>>> 'name' in a
True
>>> ('name', 'apple') in a.items()
True
>>> 'name' in a.keys()
True
>>> 'apple' in a.values()
True
자바스크립트에서 in 연산자를 사용하여 객체에 속성 이름이 존재하는지 확인할 수 있다. 객체에 entries, keys, values 메서드를 적용한 후에 돌려받는 배열에 in 키워드를 사용하면 값이 아닌 속성 이름으로 검색함으로 0, 1, 2… 이런 인덱스 값을 찾는다. 값을 찾으려면 in 연산자 대신 배열 메서드 indexOf를 사용해야 한다. 리스트에도 in 연산자가 적용되는 파이썬이 더 직관적이다.

> // javascript
> 'name' in a
true
> a['name'] === 'apple'
true
> Object.keys(a).indexOf('name') !== -1
true
> Object.values(a).indexOf('apple') !== -1
true
{} 객체 모든 값 읽기
파이썬에서 사전의 모든 키와 값을 읽으려면 사전에 items 메서드를 적용하고 그 결과를 for 문에 대입하면 된다.

>>> # python
>>> for key, value in a.items():
...     print(key + ': ' + value)
...
name: apple
color: red
자바스크립트에서 객체는 사용자가 저장하지 않은 많은 속성들을 가지고 있기 때문에 속성 중에 자신의 것을 분리하는 조건문을 추가해야 한다.

> // javascript
> var val,
...     property;
undefined
> for (property in a) {
...   if (a.hasOwnProperty(property)) {
.....       val = a[property];
.....       console.log(property + ': ' + val);
.....   }
... }
name: apple
color: red
undefined
추가 라이브러리를 사용하지 않는다면 사전 다루기는 파이썬이 더 편하다. 자바스크립트에서 {}는 모든 객체의 부모가 되는 객체로서 데이터 타입 이상의 의미가 있는 점이 파이썬과 다르다. 예제 코드를 받아 테스트할 수 있다.
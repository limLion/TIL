# __init__

Player라는 이름의 class를 만든다고 하자. 타입스크립트에서는 constructor 메서드가 있었다. 이 메서드는 class가 생성될 때 호출되는 함수이다. 파이썬에서는 constructor 메서드가 없고, 대신에 `__init__`라는 함수가 있다.  이 함수는 `self`라고 불리는 하나의 인자와 함께 호출된다. 

> 가장 중요한 건, class 안에 있는 “모든” 메서드는 self를 가장 첫 번째 parameter로 갖는다는 것.
> 

```python
class Player:

	def __init__(self):
```

self는 class를 가리킨다. 즉 self는 class의 instance를 가리킨다.

> self는 TypeScript JavaScript Java에서 사용하는 this와 비슷하다.
> 

```python
class Player:

	def __init__(self):
		self.name = "예림"

```

이렇게 클래스를 생성했으니, 이제 새로운 yelim instance를 만들 것임.

```python
yelim = Player();
```

> java나 TypeScript, JavaScript와 다르게 python에는 new가 없다.
> 

`“예림”`을 출력해보자.

```python
print(yelim.name); // "예림"
```

전체 코드는 다음과 같다.

```python
class Player: # Player라는 객체 생성 
	def __init__: 
		this.name = "예림"

# yelim 인스턴스 생성
yelim = Player();
print(yelim.name);
```

그런데 이렇게 설정한다면 1,000 개의 Player를 만들면 모두 Nico라는 이름을 갖게 됨. 그래서 __init__ 함수에 파라미터를 더 생성해주어야 함. 

```python
class Player:
	def __init__(self, name, xp):
		self.name = name
		self.xp = xp

yelim = Player() # Error 발생
```

다음과 같이 Player에 파라미터를 넘겨주지 않으면 에러가 발생함. __init__ 함수가 name과 xp값을 기다리고 있기 때문.

```python
yelim = Player("yelim", 1000)
print(yelim.name, nico.xp)
```

아까 말했듯이, **class 안의 모든 메서드에는 self라는 인자를 가장 첫 번째 파라미터로 갖는다.** 다음과 같이 작성하면 에러가 발생한다. 

```python
class Player:
	def __init__(self, name, xp):
		self.name = name
		self.xp = xp
	def say_hello():
		print("hello")

yelim = Player("yelim", 1000)
yelim.say_hello()
```

say_hello에 인자 하나를 주는데 say_hello는 아무것도 받지 않는다는 에러가 발생한다. 위 코드는 다음과 같이 수정해주어야 한다. 

```python
def say_hello(self):
	print("hello")
```

> 클래스를 호출한다는 것은, 기본적으로 클래스의 __init__ 메서드를 호출하는 것이다.
> 
> 
> ```python
> yelim = Player("yelim", 1000)
> ```
> 
> 위와 같은 코드는 아래 코드와 같은 의미이다.
> 
> ```python
> yelim = Player.__init__("yelim", 1000)
> ```
> 
> 즉, 클래스를 초기화(initialize) 하는 것이다. 
> 

# 상속

파이썬 코드로 상속이 어떻게 구현되는지 보자.

```python
class Player:
	def __init__(self, name, xp):
		self.name = name
		self.xp = xp
	def say_hello(self):
		print(f"hello my name is {self.name}")

yelim = Player("yelim", 1000)
yelim.say_hello()
```

이 코드 뒤에 작성하자.

```python
class Player:
	def __init__(self, name, xp):
		self.name = name
		self.xp = xp
	def say_hello(self):
		print(f"hello my name is {self.name}")

class Fan:
	def __init__(self, name, fav_team):
		self.name = name
		self.fav_team = fav_team
	def say_hello(self):
		print(f"hello my name is {self.name}")

```

위를 보면, Player에게도 name이 있고, say_hello가 있다. 우리가 할 수 있는 것은, 상속을 이용해서 이 두 class에서 반복적인 부분을 추상화하는 것이다. 우리는 반복되는 코드를 저장할 다른 클래스 Human을 만들 것이다. 

```cpp
class Human:
	def __init__(self, name):
		self.name = name

	def say_hello(self):
		print(f"hello my name is {self.name}")
```

그리고 이 Human 클래스를 상속 받을 Player와 Fan에서 중복된 코드를 삭제하자. (주석 처리한 부분을 삭제할 것이다.)

```cpp
class Player:
	def __init__(self, name, xp):
		// self.name = name
		self.xp = xp
	/* def say_hello(self):
		print(f"hello my name is {self.name}") */

class Fan:
	def __init__(self, name, fav_team):
		// self.name = name
		self.fav_team = fav_team
	/* def say_hello(self):
		print(f"hello my name is {self.name}") */

```

그리고 Player와 Fan을 위해 self.name과 say_hello를 받아오고 싶다면, 다음과 같이 적어주면 된다.

```cpp
class Player(Human):
	def __init__(self, name, xp):
		self.xp = xp

class Fan(Human):
	def __init__(self, name, fav_team):
		self.fav_team = fav_team

```

새로운 객체를 생성해보자.

```cpp
nico_player = Player("nico", 10);
nico.player.say_hello()

nico_fan = Fan("nico_fan", "dontnknow")
nico.fan.say_hello()
```

‼️ 에러가 발생한다 ‼️ 에러가 발생하는 이유를 다음 챕터에서 다뤄보자.

# super()

## 들어가며

Fan 클래스는 Human 클래스를 상속 받았으므로 Human 클래스의 self.name과 say_hello를 가지고 있는 것이다. 그렇지만 다음과 같은 코드는 *Human 클래스의 __init*_ 메서드를 호출하고 있지 않다.

```python
nico = Fan("nico", "blue")
nico.say_hello()
```

에러가 발생한 이유는, 

```python
class Human:
	def __init__(self, name):
		self.name = name

	def say_hello(self):
		print(f"hello my name is {self.name}")

class Fan(Human):
	def __init__(self, name, fav_team):
		self.fav_team = fav_team

nico = Fan("nico", "blue")
nico.say_hello()
```

에러가 발생하는 이유는, `Human`의 `say_hello`메서드에서 우리가 Human의 __init__ 메서드를 호출하지 않았기 때문에, `[self.name](http://self.name)` 을 찾을 수 없기 때문. 우리가 Human 클래스의 __init__ 메서드를 호출하기 위해서는, `super()` 이라는 함수를 사용해야 한다.  

## super() 함수의 기능

> 부모 클래스(Human)에 접근할 수 있는 권한을 준다.
> 

다음 코드를 보자.

```python
class Fan(Human):
	def __init__(self, name, fav_team):
		super().__init__(name) 
		# Human 클래스의 __init__ 메서드가 name을 인수로 받으므로
...
```

이와 같이 super() 메서드는 Human 클래스에 접근할 수 있게 해준다. 

Player 코드도 수정해주고, 호출해보자.

```python
class Human:
  def __init__(self, name):
		print("human initialized")
    self.name = name
  def say_hello(self):
    print(f"hello my name is {self.name}")

class Player(Human):
  def __init__(self, name, xp):
    super().__init__(name)
    self.xp = xp
    
class Fan(Human):
  def __init__(self, name, fav_team):
		super().__init__(name)
    self.fav_team: fav_team

nico_player = Player("nico", 10)
nico_player.say_hello()

nico_fan = Fan("nico", "blue")
nico_fan.say_hello()
```

```python
human initialized
hello my name is nico
human initialized
hello my name is nico
```

# 부록

## 클래스를 생성할 때 __init__ 메서드는 항상 있어야 하는가?

> 언제나 init 메서드를 만들 필요는 없다.
> 

```python
class Dog:
  def woof(self):
    print("woof woof")

class Beagle(Dog):
  def jump(self):
    print("jump")

beagle = Beagle()
beagle.woof()
```

위와 같은 코드에서는 굳이 __init__ 메서드가 필요 없다. 속성을 정의할 때만 사용하면 된다. 

## super() 메서드를 __**init__ 메서드를 사용할 때만 사용해야 하나?**

다음과 같이 Beagle 클래스에서 woof 메서드를 재사용하고 싶다면, 다음과 같이 작성하면 된다. 

```python
class Dog:
  def woof(self):
    print("woof woof")

class Beagle(Dog):
  def woof(self):
    super().woof() # Dog.woof()라고 생각하면 쉽다.
    print("super woof")
  def jump(self):
    print("jump")

beagle = Beagle()
beagle.woof()
```

```bash
woof woof
super woof
```

## 메서드 오버라이딩

다음과 같이 작성하면, Dog의 woof 메서드는 완벽히 오버라이딩 된 것이다. 

```python
class Dog:
  def woof(self):
    print("woof woof")

class Beagle(Dog):
  def woof(self):
    print("super woof")
  def jump(self):
    print("jump")

beagle = Beagle()
beagle.woof() # "super woof"
```

# __str__

## 들어가며

```python
class Dog:
  def __init__(self, name):
    self.name = name

mimi = Dog("mimi");

print(mimi);
```

**출력**

```bash
<__main__.Dog object at 0x7f10d4081dc0>
```

이는 mimi 가 객체이고, 메모리 상 어디에 위치하는지 말해주고 있다. 그런데 만약 문자열로 보이는 방식을 커스텀할 수 있다면 어떨까? __**str**__ 함수를 이용하면 클래스가 문자열로 보이는 방식을 바꿀 수 있다. 

## __**str**__ 메서드란?

> 우리의 클래스를 어떤 문자열로 보여질지 정함.
> 

객체를 만들고, 그 객체의 정보(클래스 이름, 저장위치 등)을 알고 싶을 때, print(객체 이름)을 사용하는데, 이는 object 클래스의 __str__ 메서드가 호출되어 반환된 문자열 정보이다. 이러한 __str__ 의 문자열 반환 기능을 오버라이딩하여 쓸 수 있다. 

```python
class Dog:
  def __init__(self, name):
    self.name = name
	def __str__(self):
		return "🦁"

mimi = Dog("mimi");

print(mimi);
```

**출력**

```python
🦁
```

# dir

> 디렉터리를 의미한다. 클래스의 속성들과 메서드들을 보여준다.
> 

```python
mimi = Dog("mimi")
print(dir(mimi))
```

```python
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
```

클래스의 속성인 name, 그리고 우리가 배운 __str__, __init__ 등이 있다. 장고에서는 클래스로부터 확장하는 일이 많을텐데, 그때 이걸 이용하면 그 클래스가 가지고 있는 속성들과 메서드들을 확인하기 좋다.
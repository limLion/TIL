# friend 선언

## 클래스에 대한 friend 선언

다음과 같이 Boy가 Girl을 프렌드로 선언함. 즉 private 멤버의 접근을 Girl에게 허용하겠다는 뜻!

```cpp
#include <iostream>
#include <string.h>

using namespace std;

class Boy
{
private:
    int height;
    friend class Girl;
public:
    Boy(int len) : height(len) {}
};
```

그럼 다음과 같이 Girl이 Boy의 friend로 선언되었으므로, private 멤버에 직접 접근이 가능하다.

```cpp
class Girl
{
private:
    char phNum[20];
public:
    Girl(char * num)
    {
        strcpy(phNum, num);
    }
    void ShowYourFriendInfo(Boy &frn)
    {
        cout<<"His height: "<<frn.height<<endl; // 여기 frn.height 주목!
    }
};
```

근데 `Boy`는 `Girl`의 `private` 멤버에는 접근하지 못함…

## 함수의 friend 선언

```cpp
class Point
{
private:
	int x;
	int y;
public:
	Point(const int &xpos, const int &ypos) : x(xpos), y(ypos) { } // 생성자
	// 클래스의 특정 멤버함수를 대상으로 friend 선언
	friend Point PointOP::PointAdd(const Point&, const Point&); 
	// 클래스의 특정 멤버함수를 대상으로 friend 선언
	friend Point PointOP::PointSub(const Point&, const Point&);
	// 전역 함수 대상의 friend 선언
	friend void ShowPointPos(const Point&); 
};
```

```cpp
Point PointOP::PointAdd(const Point& pnt1, const Point& pnt2)
{
	opcnt++;
	return Point(pnt.x+pnt2.x, pnt1.y+pnt2.y); // private 멤버 접근
}
Point PointOP::PointSub(const Point& pnt1, const Point& pnt2)
{
	opcnt++;
	return Point(pnt.x+pnt2.x, pnt1.y+pnt2.y); // private 멤버 접근
}
```

```cpp
void ShowPointPos(const Point& pos)
{
	cout<<"x: "<<pos.x<<", "; // private 멤버 접근
	cout<<"y: "<<pos.y<<endl; // private 멤버 접근
}
```

# static

## C언어에서의 static

### 전역 변수에 선언된 static

> 선언된 파일 내에서만 참조를 허용하겠다는 의미
> 

### 함수 내에서 선언된 static

> 한 번만 초기화되고, 지역변수와 달리 함수를 빠져나가도 소멸되지 않는다.
> 

```cpp
void Counter()
{
	static int cnt;
	cnt++;
	cout<<"Current cnt: "<<cnt<<endl;
}

int main(void)
{
	for(int i = 0; i<10; i++)
		Counter();
	return 0;
}
```

```cpp
Current cnt: 1
Current cnt: 2
Current cnt: 3
...
Current cnt: 10 // 대충 계속 증가
```

## static 멤버 변수(클래스 변수)

static 변수는 객체 별로 존재하는 변수가 아닌, **프로그램 전체 영역에서 하나만 존재하는 변수**이다.

프로그램 실행과 동시에 초기화되어 메모리 공간에 할당된다.

```cpp
class SoSimple
{
private:
    static int simObjCnt=0;// static 멤버변수, 클래스 변수
public:
    SoSimple()
    {
        simObjCnt++;
        cout<<simObjCnt<<"번째 SoSimple 객체"<<endl;
    }
};

int SoSimple::simObjCnt=0; // static 멤버변수의 초기화
// 꼭 초기화 해줘야 함! 그리고 전역 범위에서!
// 그리고 앞에 static 안붙여줘도 됨. 
```

이렇게 static은 초기화를 전역 범위에서 해줘야 함.

```cpp
int main(void)
{
	SoSimple sim1;
	SoSimple sim2;
	SoSimple sim3;
	...
}
```

## static 멤버변수의 접근 방법

static 변수를 외부에서 접근 가능하게 하려면, 해당 변수가 `public` 선언되어야 한다. 

```cpp
class SoSimple
{
public:
    static int simObjCnt; // public으로 선언이 되면, 클래스의 이름을 이용해서 호출이 가능하다. 
public:
    SoSimple()
    {
        simObjCnt++; // 접근 case 1
    }
};
int SoSimple::simObjCnt=0;

int main(void)
{
    // 접근 case 2
    cout<<SoSimple::simObjCnt<<"번째 SoSimple 객체"<<endl;
    SoSimple sim1;
    SoSimple sim2;
    cout<<SoSimple::simObjCnt<<"번째 SoSimple 객체"<<endl;
    // 접근 case 3
    cout<<sim1.simObjCnt<<"번째 SoSimple 객체"<<endl;
    cout<<sim2.simObjCnt<<"번째 SoSimple 객체"<<endl;
    return 0;
}
```

### static 멤버`함수`는 static 멤버`변수`의 특징과 일치한다.

- 선언된 클래스의 모든 객체가 공유한다.
- public으로 선언이 되면, 클래스의 이름을 이용해서 호출이 가능하다.
- **객체의 멤버로 존재하는 것이 아니다.**

```cpp
class SoSimple
{
private:
	int num1;
	static int num2;
public:
	SoSimple(int n): num1(n)
	{ }
	static void Adder(int n) // static 함수
	{
		num1+=n; // 컴파일 에러 발생
		num2+=n;
	}
};
int SoSimple::num2=0;
```

static 함수는 객체 내에 존재하는 함수가 아니기 때문에 `**멤버변수**`나 `**멤버함수**`에 **접근이 불가능하다.** 다음 예를 보자.

```cpp
class SoSimple
{
private:
    int num1;
    static int num2;
public:
    SoSimple(int n): num1(n)
    {} // 생성자
    static void Adder(int n)
    {
        num1+=n; // 컴파일 에러 발생!
        // static 함수는 객체 내에 존재하는 함수가 아니기 때문!
        num2+=n;
    }
};
```

**static 함수는 static 변수에만 접근 가능하고, static 함수만 호출 가능하다.**

## const static 멤버

const static 멤버변수는 클래스가 정의될 때 지정된 값이 유지되는 상수이기 때문에, 초기화가 가능.

```cpp
class CountryArea
{
public:
    const static int RUSSIA = 1707540; // 초기화 안하면 에러!
    const static int CANADA = 994867;
    const static int CHINA = 957290;
    const static int SOUTH_KOREA = 9922;
}

int main(void)
{
    cout<<"러시아 면적: "<<CountryArea::RUSSIA<<"km"<<endl; // 이런 식으로 호출
    return 0;
}
```

## mutable

mutable로 선언된 멤버변수는 **const 함수 내에서의 값 변경 가능**

```cpp
class SoSimple
{
private:
	int num1;
	mutable int num2;
public:
	SoSimple(int n1, int n2) : num1(n1), num2(n2)
	{ } // 생성자
	void CopyToNum2() const
	{
		num2=num1;
	}
};
```
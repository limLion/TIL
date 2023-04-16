# const 키워드

이것들 구분하기만 해도… 당신은 const 전문가!!!!!!!!!!!

```cpp
const int num=10; 
const int *ptr1=&val1;
int * const ptr2=&val2;
const int * const ptr3=&val3;
```

- 정답이오
    
    ```cpp
    const int num=10; // 변수 num을 상수화
    const int *ptr1=&val1; // ptr1을 사용해서 val1의 값을 변경할 수 없음.
    int * const ptr2=&val2; // 포인터 ptr2가 상수화 됨
    const int * const ptr3=&val3; // 포인터 ptr3가 상수화 되었으며, ptr3을 이용해서 val3의 값을 변경할 수 없음.
    ```
    

<aside>
🪴 이렇게 이해하면 쉬움. const 키워드 뒤에 온 코드가 사용 불가하다~~

```cpp
const int * ptr1 = &val1;
```

`* ptr1 = &val1` 라는 코드 사용 불가하다는 뜻

</aside>

# 참조자(Reference)

> 참조자는 기존에 선언된 변수에 붙이는 별칭이다.
> 

```cpp
int num1=2010;
int &num2=num1; // num1의 메모리 공간에 num2라는 이름이 추가로 붙게 된다.
```

이후 num1로 하는 모든 연산은 num2로 하는 것과 동일한 결과를 보인다. 

```cpp
int num1=2759;
int &num2=num1;
int &num3=num2;
int &num4=num3;
```

참조자의 수는 제한이 없으며 참조자를 대상으로 참조자를 선언하는 것도 가능하다.

## 참조자의 선언 가능 범위

- 참조자는 참조의 대상을 변경할 수 없다.
- 선언과 동시에 누군가를 참조해야 함.
    
    ```cpp
    int &ref=20; (x) // 상수 대상으로의 참조자 선언은 불가능
    int &ref; (x) // 참조자는 생성과 동시에 누군가를 참조해야 한다.
    int &ref=NULL; (x) // 포인터처럼 NULL로 초기화하는 것도 불가능하다.
    ```
    
    > NULL을 넣는다는 건 곧 0을 넣는 것과 같아서 안됨.
    > 
- 배열의 요소도 역시 변수의 성향을 지니므로 참조자의 선언이 가능하다.
    
    ```cpp
    int &ref1=arr[0]; // 가능!
    ```
    
- 포인터 변수 참조 가능
    
    **int * 자료형의 참조자도 int * 여야 한다~**
    
    ```cpp
    int *ptr=&num;
    int *(&pref)=ptr;
    ```
    
    ```cpp
    int **dptr=&ptr;
    int **(&dpref)=dptr;
    ```
    

## 함수 호출

> Call by value & Call by address
> 

```cpp
void SwapByValue(int num1, int num2)
{
	int temp=num1;
	num1=num2;
	num2=temp;
} // Call-by-value
```

```cpp
void SwapByRef(int *ptr1, int*ptr2)
{
	int temp=*ptr1;
	*ptr1=*ptr2;
	*ptr2=temp;
} // Call-by-reference
```

## 참조자를 이용한 Call-by-reference

```cpp
void SwapByRef2(int &ref1, int &ref2) // 함수 호출 과정에서 매개변수가 선언과 동시에 초기화
{
	int temp=ref1;
	ref1=ref2;
	ref2=temp;
} // Call-by-reference
```

## const 참조자

> 참조자를 통한 값의 변경을 진행하지 않을 경우
> 

```cpp
void HappyFunc(const int &ref) {...}
```

`HappyFunc` 내에서 참조자 ref를 이용한 값의 변경은 허용하지 않겠다….

## ⭐️ 반환형이 참조이고 반환도 참조로 받는 경우

```cpp
int& ILoveReference(int &ref)
{
	ref++;
	return ref;
}
```

```cpp
// 메인함수
int main(void)
{
	int num1=1;
	int &num2=ILoveReference(num1);
	num1++;
	num2++;
	...
}
```

num1 num2 모두 4가 됨.

일어나는 일은 다음과 같다. 

```cpp
int num1=1;
int &ref=num1;
int &num2=ref;
```

## ⭐️ 반환형은 참조이되 반환은 변수로 받는 경우

```cpp
int& ILoveReference(int &ref)
{
	ref++;
	return ref;
}
```

```cpp
// 메인 함수
int main(void)
{
	int num1=1;
	int num2=ILoveReference(num1); // 1에서 1 증가한 2 전달
	num1+=1; // 3
	num2+=100; // 102
	...
}
```

반환 과정에서 일어나는 일은 다음과 같다.

```cpp
int num1=1;
int &ref=num1;
int num2=ref; // 이렇게 값만 복사된 것!
```

<aside>
🪴 그러니까, 함수를 볼 때 반환형과 매개변수가 참조형인가지, 또 반환하는 값을 무엇으로 받는지를 주시해서 봐야 함.

</aside>

## 참조를 대상으로 값을 반환하는 경우

반환형이 참조형이 아니라면 차이는 없다!

다음과 같이 반환형이 참조형이 아닌 경우, 참조자로 그 값을 받을 수 없다.(상수를 참조할 수 없으므로)

```cpp
int IHateReference(int &ref)
{
	ref++;
	return ref;
}
```

```cpp
int num2=IHateReference(num1); (O)
int &num2=IHateReference(num1); (X)
```

## const 참조자의 또 다른 특징

```cpp
const int num=20;
int &ref=num; // error! 이를 허용하면 ref를 통한 값의 변경을 허용한다는 뜻
ref+=10;
cout<<num<<endl;
```

이를 해결하기 위해서 다음과 같이 쓸 수 있다. 

```cpp
const int num=20;
const int &ref=num;
```

따라서 한 번 const 선언이 들어가기 시작하면 관련해서 몇몇 변수들이 const로 선언되어야 하는데, 이는 프로그램의 안정성을 높이는 

## 어떻게 참조자가 상수를 참조하냐고요!!!!!!!!!!!

**const 참조자는 상수를 참조할 수 있다!**

이유는, 이렇듯 상수를 const 참조자로 참조할 경우,

상수를 메모리 공간에 `임시적으로 저장`하기 때문이다. 

즉, 행을 바꿔도 소멸시키지 않는다.

이러한 것이 가능하게 한 이유는, 매개변수 형이 참조자인 경우에 상수를 전달할 수 있도록 하기 위함이다. 

```cpp
int Adder(const int &num1, const int &num2)
{
	return num1+num2;
}
```

# new & delete

new 연산자로 할당된 메모리 공간은 반드시 delete 함수 호출을 통해서 소멸해야 한다!

```cpp
int * ptr1=new int; // int 형 변수의 할당
double * ptr2= new double; // double 형 변수의 할당
int * arr1 = new int[3]; // 길이가 3인 int 형 배열의 할당
double * arr2 = new double[7]; // 길이가 7인 double 형 배열의 할당
```

다음 변수와 배열을 소멸하는 코드는 다음과 같다.

```cpp
delete ptr1;
delete ptr2;
delete []arr1;
delete []arr2;
```

# 헤더 파일 이름 정의 규칙

```cpp
#include<stdio.h> -> #include<cstdio>
```

c를 더하고 .h를 빼라
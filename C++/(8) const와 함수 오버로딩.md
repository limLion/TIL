# const와 함수 오버로딩

**함수의 `const` 선언 유무는 함수 오버로딩의 조건이 된다.** 

```cpp
class SoSimple
{
private:
	int num;
public:
	SoSimple(int n) : num(n) // 생성자
	{ }
	SoSimple& AddNum(int n) // 인자로 들어오는 값 만큼 멤버변수 num에 더해줌.
	{
		num+=n;
		return *this;
	}
	void SimpleFunc()
	{
		cout<<"SimpleFunc : "<<num<<endl;
	}

	void SimpleFunc() const 
	{
		cout<<"const SimpleFunc : "<<num<<endl;
	}
};
```

## const 함수는 언제 호출되는데?

const 객체 또는 참조자를 대상으로 멤버함수 호출시 const 선언된 멤버 함수가 호출된다. 

```cpp
void YourFunc(const SoSimple &obj) 
{
    obj.SimpleFunc();
}

int main(void)
{
    SoSimple obj1(2);
    const SoSimple obj2(7); // 요놈!
    
    obj1.SimpleFunc(); // 그냥 SimpleFunc() 호출
    obj2.SimpleFunc(); // const SimpleFunc() 호출
    
    YourFunc(obj1); // const SimpleFunc() 호출
    YourFunc(obj2); // const SimpleFunc() 호출
    return 0;
}
```

```cpp
SimpleFunc: 2
const SimpleFunc: 7
const SimpleFunc: 2
const SimpleFunc: 7

```
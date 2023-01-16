> 점프 투 자바: [https://wikidocs.net/book/31](https://wikidocs.net/book/31)
> 

# 형변환

## 문자열을 정수로 바꾸기

문자열을 정수로 바꾸려면 다음과 같이 Integer 클래스를 사용한다.

> Integer은 int 자료형의 Wrapper 클래스이다.
> 

```java
public class Sample {
	public static void main(String[] args) {
		String num = "123";
		int n = Integer.parseInt(num); 
		System.out.println(n); // 123 출력
	}
}
```

## 정수를 문자열로 바꾸기

정수를 문자열로 바꾸는 가장 쉬운 방법은 정수 앞에 빈 문자열 `""` 을 더해주는 것이다.

```java
int n = 123;
String num = "" + n;
System.out.println(num); // "123" 출력
```

또는 다음과 같이 변환할 수도 있다.

```java
int n = 123;
String num1 = String.valueOf(n);
String num2 = Integer.toString(n); 

System.out.println(num1);  // 123 출력
System.out.println(num2);  // 123 출력
```

`String.valueOf(정수)`, `Integer.toString(정수)` 모두 정수를 문자열로 바꾸어 리턴한다.

> 실제 프로젝트에서 정수와 문자열 사이의 변환은 매우 자주 사용한다.
> 

## 문자열을 실수로 바꾸기

`Double.parseDouble` 또는 `Float.parseFloat`를 사용하여 형변환할 수 있다.

```java
String num = "123.456"; 
double d = Double.parseDouble(num);
System.out.println(d); // 123.456
```

# final

자바의 final은 자료형에 값을 단 한번만 설정할수 있게 강제하는 키워드이다. 즉, 값을 한번 설정하면 그 값을 다시 설정할 수 없다는 말이다.

```java
final int n = 123; // final로 설정하면 값을 바꿀 수 없다.
n = 456; // 컴파일 에러 발생
```

리스트의 경우도 final로 선언시 재할당은 불가능하다.

```java
final ArrayList<String> a = new ArrayList<>(Arrays.asList("a", "b"));
a = new ArrayList<>(Arrays.asList("c", "d")); // 컴파일 에러 발생
```

final은 프로그램 수행 도중 그 값이 변경되면 안되는 상황에 사용한다.
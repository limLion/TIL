## SELECT 구와 WHERE 구

```sql
SELECT 열1, 열2 FROM 테이블명 WHERE 조건식
```

- 행을 선택할 때는 WHERE 구를 사용하며, 열을 선택할 때에는 SELECT 구를 사용한다.

## SELECT 구에서 열 지정하기

```sql
SELECT 열1, 열2, ... FROM 테이블명
```

- 열은 콤마(,)를 이용하여 구분 지으며 여러 개를 지정할 수 있다.
- 열을 전혀 지정하지 않으면 구문 에러가 발생한다.
- 결과는 지정한 열의 순서대로 표시된다.
- 동일한 열을 중복해서 지정해도 무관함.

## WHERE 구에서 행 지정하기

```sql
SELECT 열 FROM 테이블명 WHERE 조건식
```

- 만약 WHERE 구를 생략한 경우에는 테이블 내의 모든 행이 검색 대상이 된다.
- 조건식은 ‘`열`과 `연산자`, `상수`’로 구성되는 식’
    - ex) ‘`no` `=` `2`’

### 값이 서로 다른 경우 ‘<>’

- <> 연산자는 서로 다른 값인지를 비교하는 연산자

```sql
SELECT * FROM 테이블명 WHERE no <> 2;
```

## 문자열형의 상수

문자열형 조건식의 경우 싱글 쿼트(’ ‘)로 둘러싸 표기해야 한다. 

- 날짜 시간형의 경우에도 싱글쿼트로 둘러싸 표기한다.
    - 연월일은 하이픈(-)으로, 시각은 시분초를 콜론(:)으로 구분하여 표기한다.

```sql
SELECT * FROM 테이블명 WHERE name='개발과 고양이발';
```

## NULL 값 검색

다음과 같이 = 연산자로 NULL을 검색할 수는 없다. 

```sql
SELECT * FROM 테이블명 WHERE birthday = NULL; // error
```

### IS NULL

- NULL 값을 검색할 때는 = 연산자가 아닌 IS NULL을 사용한다.
- NULL 값이 아닌 행을 검색하고 싶다면 IS NOT NULL을 사용하면 된다.

```sql
SELECT * FROM 테이블명 WHERE birthday IS NULL;
```
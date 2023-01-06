# 개요

> HTML의 Element들을 JavaScript를 통해 변경하고, 읽을 수 있다.
> 

> JavaScript는 HTML에 이미 연결되어 있고, HTML에서 여러 정보를 가져올 수 있고, JavaScript 코드에서 그 정보를 볼 수 있음.
> 

# document 객체

> document 는 우리의 웹사이트를 의미한다.
> 

크롬 콘솔창에 다음과 같이 `document`를 입력하면 내가 작성한 html 코드를 보여줌. 

```jsx
// in console
document
```

```jsx
// 출력값
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Momenmtum</title>
</head>
<body>
    <script src ="app.js"></script>
</body>
</html>
```

다음과 같이 `console.dir(document)` 를 입력하면, 객체 형태로 document를 보여줌. 

```jsx
// in console
console.dir(document) // console.dir: Element를 더 자세하게 보여줌
```

```jsx
...
title: "Momenmtum"
...
```

자바스크립트에 title을 정의한 적이 없는데도, 다음과 같이 HTML에 내가 정의한 항목인 title을 보여줌. 즉, **자바스크립트에서 HTML document 객체로부터 title을 가져올 수 있음**

```jsx
document.title // "Momentum"
```

다음과 같이 작성하면 title을 ‘HI’로 바꿀 수 있음. 

```jsx
document.title = "HI"; // 새로고침하면 원 상태로 돌아감. 
```

# 자바스크립트로 HTML 변경하기

**index.html**

```jsx
<title>Hello From HTML!</title>
```

**app.js**

```jsx
document.title = "Hello from JS"
```

브라우저에서 `index.html` 을 실행하면, title이 ‘Hello from JS’ 인 것을 볼 수 있다. 자바스크립트로 HTML을 바꿀 수 있다는 것.

# 자바스크립트에서 HTML 특정 값 가져오기

## document.getElementById(””)

**index.html**

```jsx
<body>
    <h1 id="title">Grab me!</h1>
    <script src ="app.js"></script>
</body>
```

**console**

```jsx
document.getElementById("title");
// <h1 id="title">Grab me!</h1>
```

**app.js**

```jsx
const title = document.getElementById('title');
console.dir(title);
```

```jsx
// 출력
...
autofocus: false
...
className: ""
...
innerText: "Grab me!"
...
textContent: "Grab me"!
...
```

만약 `autofocus` 를 `true` 로 바꾸고 싶다면 `index.html`에서 id=”title”인 코드를 다음과 같이 수정하면 된다.

```jsx
<h1 autofocus id="title">Grab me!</h1>

// autofocus: true
```

만약 `className` 을 바꾸고 싶다면 `index.html`에서 id=”title”인 h1 Element를 다음과 같이 수정하면 된다.

```jsx
<h1 autofocus class="hello" id="title">Grab me!</h1>
```

만약 `innerText`을 **자바스크립트**를 이용해 바꾸고 싶다면 `app.js`에서 다음과 같은 코드를 작성하면 된다. 

```jsx
const title = document.getElementById('title');

title.innerText = "Got you!"
```

그리고 나서 Elements에 들어가면 다음과 같이 html 코드가 바뀐 것을 볼 수 있다. 

```jsx
<h1 autofocus="" class="hello" id="title">Got you!</h1>
```

### 요약

- HTML에서 `id`를 추가하고
- 자바스크립트에서 그 `getElementById`라는 함수를 이용해 element를 가져왔음.

```jsx
const title = document.getElementById('title');

title.innerText = "Got you!"

console.log(title.id);
console.log(title.className);
```
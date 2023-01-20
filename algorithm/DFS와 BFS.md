> 참고자료(1) : [https://devuna.tistory.com/32](https://devuna.tistory.com/32)
참고자료(2): [https://velog.io/@513sojin/C백준-1260-DFS와BFS](https://velog.io/@513sojin/C%EB%B0%B1%EC%A4%80-1260-DFS%EC%99%80BFS)
> 

# 들어가며

그래프를 탐색하는 방법에는 크게 **깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS)가 있다.** 

> 여기서 그래프를 탐색한다는 것은, **하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것을 말합니다.**
> 

# 1. DFS(깊이 우선 탐색)

최대한 깊이 내려간 뒤, 더 이상 깊이 갈곳이 없을 경우 옆으로 이동. **`stack` 으로 구현한다.**

## 개념

루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 **해당 분기를 완벽하게 탐색**하는 방식을 말한다.

![https://blog.kakaocdn.net/dn/xC9Vq/btqB8n5A25K/GyOf4iwqu8euOyhwtFuyj1/img.gif](https://blog.kakaocdn.net/dn/xC9Vq/btqB8n5A25K/GyOf4iwqu8euOyhwtFuyj1/img.gif)

> 출처: [https://developer-mac.tistory.com/64](https://developer-mac.tistory.com/64)
> 

## 특징

1. 모든 노드를 방문하고자 하는 경우 이 방법을 선택함.
2. BFS보다 좀 더 간단함.
3. 검색 속도 자체는 BFS에 비해서 느림

# 2. 너비 우선 탐색(BFS)

최대한 넓게 이동한 다음, 더 이상 갈 수 없을 때 아래로 이동. `queue` 로 구현.

![https://blog.kakaocdn.net/dn/c305k7/btqB5E2hI4r/ea7vFo08tkDYo4c8wkfVok/img.gif](https://blog.kakaocdn.net/dn/c305k7/btqB5E2hI4r/ea7vFo08tkDYo4c8wkfVok/img.gif)

> 출처: [https://developer-mac.tistory.com/64](https://developer-mac.tistory.com/64)
> 

## 개념

루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법으로, 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법

## 특징

1. 주로 두 노드 사이의 최단 경로를 찾고 싶을 때 이 방법을 선택
2. 지구 상의 존재하는 모든 친구 관계가 그래프로 표현되어있다고 가정할 때, Sam과 Eddie 사이에 존재하는 경로를 찾는 경우
    1. DFS의 경우 모든 친구 관계를 다 살펴봐야 할지도 모르지만, 
    2. BFS의 경우 Sam과 가까운 관계부터 탐색하게 된다.

# DFS vs BFS

![https://blog.kakaocdn.net/dn/cQYkI8/btqB8oDsMGe/EEYm0cKGYhxTR0kJhGiJPK/img.gif](https://blog.kakaocdn.net/dn/cQYkI8/btqB8oDsMGe/EEYm0cKGYhxTR0kJhGiJPK/img.gif)

> 출처: [https://namu.wiki/w/BFS](https://namu.wiki/w/BFS)
> 

## 비교

> 둘 다 이전에 방문했던 위치는 다시 방문하지 않는다.
> 

| DFS | BFS |
| --- | --- |
| 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색 | 현재 정점에 가까운 점들부터 탐색 |
| 스택 또는 재귀함수로 구현 | 큐를 이용해서 구현 |

## DFS와 BFS의 시간 복잡도

두 방식 모두 모든 조건 내의 모든 노드를 검색한다는 점에서 시간 복잡도는 동일하다. DFS와 BFS 둘 다 다음 노드가 방문하였는지 확인하는 시간과 각 노드를 방문하는 시간을 합하면 된다. 

N은 노드, E는 간선일 때

> 인접 리스트 : O(N+E)
인접 행렬: O(N^2)
> 

일반적으로 E(간선)의 크기가 N²에 비해 상대적으로 적기 때문에 인접 리스트 방식이 효율적임
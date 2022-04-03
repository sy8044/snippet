# snippet

### 한 줄로 들어오는 숫자들 받는 법
#### 공백 있을 때
<pre>
<code>
ll = [int(x) for x in input().split()]
ll = list(map(int,input().split()))
</code>
</pre>
#### 공백 없을 때
<pre>
<code>
graph = list(map(int,input().strip()))
</code>
</pre>

### 여러줄 숫자 받을 때
<pre>
<code>
graph = [list(map(int, input().split())) for _ in range(N)]
</code>
</pre>

### 0-1 BFS
#### 0과 1로 이루어지고 가중치 있는 그래프 최단 경로 찾기
#### 가중치를 담을 배열 선언 

### 그리디
#### 
#### 배수로 되어 있으면 반례 없음

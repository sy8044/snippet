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

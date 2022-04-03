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

### 소수 찾는 방법들
#### 숫자 모두 체크해서 찾기 - 매우 느림
<pre>
<code>
def isPrime(n) :
    flag = True
    for i in range(2,n) :
        if n % i == 0 :
            return False
    return flag
</code>
</pre>

#### 숫자 모두 체크해서 찾기 - 매우 느림
<pre>
<code>
def isPrime(n) :
    flag = True
    for i in range(2,n) :
        if n % i == 0 :
            return False
    return flag
</code>
</pre>

#### 약수는 대칭을 이루기 때문에 제곱근까지만 체크해서 찾기
<pre>
<code>
def isPrime(n) :
    flag = True
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False
    return flag
</code>
</pre>


ll = list(input())

result = [''] * len(ll)

def solution(s,start) :
    global result

    if not s :
        return

    target = min(s)
    idx = s.index(target)

    result[start+idx] = target
    print("".join(result))

    solution(s[idx+1:],start+idx+1)
    solution(s[:idx],start)

solution(ll,0)

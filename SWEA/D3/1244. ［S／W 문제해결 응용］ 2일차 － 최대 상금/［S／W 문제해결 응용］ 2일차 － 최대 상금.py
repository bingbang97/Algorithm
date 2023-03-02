T = int(input())
for tc in range(T):
    prize, N = input().split()

    N = int(N)
    prize_length = len(prize)
    visited = set([prize])
    # 계속해서 쌓이는 횟수들을 set을 이용하여 중복 횟수를 줄여준다.
    for n in range(N):
        for money in list(visited):
            # 횟수가 올라감에 따라 바뀐것들에서 한번씩 바뀌어야 하기에 새로 갱신된 visited 에서 계산해준다.
            visited.remove(money)
            # 쓰였기 때문에 제거
            tmp = list(money)
            for i in range(prize_length):
                for j in range(i+1, prize_length):
                    tmp[i], tmp[j] = tmp[j], tmp[i]
                    # 한자리 끼리 바꾸기
                    visited.add(''.join(tmp))
                    # 바꾼값 저장
                    tmp[i], tmp[j] = tmp[j], tmp[i]
                    # 숫자 원상 복구
    prize_list = []
    for money in visited:
        prize_list.append(int(money))
    max_prize = max(prize_list)
    # 문자열을 숫자로 변환 후 최대값 찾기
    print(f'#{tc+1} {max_prize}')

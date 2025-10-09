"""
cap - 트럭에 실을 수 있는 택배 수

끝에서부터 시작해서 배달할 수 있는 택배 수 구하기.
수거도 구하기. -> 수거가 안 되면 어차피 거기까지 다시 갔다와야하므로

"""
def solution(cap, n, deliveries, pickups):
    answer = 0
    remain_delivery, remain_pickup = 0, 0

    for dist in range(n-1, -1, -1):
        remain_delivery += deliveries[dist]
        remain_pickup += pickups[dist]

        while remain_delivery > 0 or remain_pickup > 0:
            remain_delivery -= cap
            remain_pickup -= cap
            answer += (dist+1) * 2

    return answer
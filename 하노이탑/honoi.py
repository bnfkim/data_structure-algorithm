# from_pos : 출발 기둥
# to_pos : 도착 기둥
# via_pos : 보조 기둥

def hanoi(N, from_pos, to_pos, via_pos):
    # 종료조건 원반 한 개일 때 그냥 옮기면 됨
    if N == 1:
        print(from_pos, "번 기둥 -> ", to_pos, "번 기둥")
        return
    
    #원반 n-1개를 via_pos로 이동 (to_pos가 보조기둥)
    hanoi(N-1, from_pos, via_pos, to_pos)              
    #가장 큰 원반을 목적지로 이동
    print(from_pos, "번 기둥 -> ", to_pos, "번 기둥")   
    #via_pos에 있는 원반 n-1개를 목적지로 이동 (from_pos가 보조기둥)
    hanoi(N-1, via_pos, to_pos, from_pos)              

print("\n N = 1")
hanoi(3, 1, 3, 2) # 원반 3개를 1번 기둥에서 3번 기둥으로 이동

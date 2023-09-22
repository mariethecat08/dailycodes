import sys
n = int(input())
nums = [0]*n # python 리스트는 처음 사이즈를 정의해주면, append함수를 사용할 때보다 메모리가 더 적게 든다.
for i in range(n):
    nums[i] = int(sys.stdin.readline()) # sys 라이브러리로 입력받을 시, 더 적은 메모리와 빠른 시간이 소요된다.
#print(*sorted(nums),sep='\n') # asterisk로 리스트에 있는 모든 원소를 한 줄에 출력할 수 있다.
                                # print 함수 안에 sep 인자를 설정하므로써, 한 줄에 하나씩만 출력되도록 할 수 있다.
                                # 사실 메모리, 시간 측면에서 그냥 따로 sort 후 for문으로 하나씩 출력하는게 경제적이다.
nums = sorted(nums)
for i in nums:
    print(i)

def kth(nums, queries):
    def trim(num, t):
        return int(num[-t:])
    
    def find_kth_index(trimmed_nums, k):
        sorted_nums = sorted(trimmed_nums)
        x = sorted_nums[k-1]
        for i in range(len(trimmed_nums)):
            if x==trimmed_nums[i]:
                return i
            
    ans = []

    for q in queries:
        pos, t_len = q
        trimmed_nums = [trim(num, t_len) for num in nums]
        kth_index = find_kth_index(trimmed_nums, pos)
        ans.append(kth_index)

    return ans
n1 = input().split()
cnt = int(input())
q1=[]

for i in range(cnt):
    q1.append(tuple(map(int, input().split())))
o1 = kth(n1, q1)

print(o1)
                                                                                                                            
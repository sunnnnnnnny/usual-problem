def common_length(s1, s2):
    len1, len2 = len(s1), len(s2)
    if len1 == 0 or len2 == 0:
        return 0
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    res = 1
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])

    return res


s1="gsgpoedsg"
s2="dsgpods"
out = common_length(s1, s2)
print(out)
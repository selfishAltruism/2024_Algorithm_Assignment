import sys

def lcs(dna1, dna2):
    m = len(dna1)
    n = len(dna2)

    #table initialization
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    #lcs calculation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i - 1] == dna2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    #lcs backtracking
    lcs_length = dp[m][n]
    lcs = [""] * (lcs_length + 1)
    lcs[lcs_length] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if dna1[i - 1] == dna2[j - 1]:
            lcs[lcs_length - 1] = dna1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)


#open file
input = open(sys.argv[1],"r")
output = open(sys.argv[2],"w")

length = int(input.readline())
dna_list = []
while True:
    #remove \n
    line = input.readline().strip()
    if not line: 
        break
    dna_list.append(list(line))

#run lcs
for i in range(0, len(dna_list)):
    most_index = 0
    most_len = 0
    most_result = ''

    for j in range(0, len(dna_list)):
        if(i == j): continue

        result = lcs(dna_list[i], dna_list[j])
        if(most_len < len(result)):
                most_index = j
                most_len = len(result)
                most_result = result
    
    output.write(str(most_index + 1) + '\t' + str(most_len) + '\t' + most_result + '\n')


#close file
input.close()
output.close()
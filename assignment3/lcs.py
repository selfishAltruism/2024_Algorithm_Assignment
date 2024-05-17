import sys

def lcs(dna1, dna2):
    dna1_len = len(dna1)
    dna2_len = len(dna2)

    #lcs dp table initialization
    dp = []
    for i in range(dna1_len + 1):
        row = [0] * (dna2_len + 1)
        dp.append(row)

    #lcs dp table population
    for i in range(1, dna1_len + 1):
        for j in range(1, dna2_len + 1):
            #if dna1 element and dna2 element are the same, +1
            if dna1[i - 1] == dna2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            #if dna1 element and dna2 element are not the same, select max
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    #lcs backtrack initialization
    lcs_length = dp[dna1_len][dna2_len]
    lcs = [""] * (lcs_length + 1)
    lcs[lcs_length] = ""

    #lcs backtracking
    i = dna1_len
    j = dna2_len
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
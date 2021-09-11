import math
import os
import random
import re
import sys



# overlap area of moving tiles
def movingTiles(l, s1, s2, queries):
    # Write your code here
    # make s2 more than s1
    s2, s1 = (s2, s1) if s2 > s1 else (s1, s2)
    res = []
    sqrt_2 = math.sqrt(2)
    for overlap_area in queries:
        t = None
        if overlap_area <= 0:
            t = (sqrt_2 * l)/abs(s2 - s1)
        else:
            t = sqrt_2 * ( l - math.sqrt(overlap_area))/abs(s2-s1)
        res.append(t)
    return res


# Special strings - few cases fail
# Complete the substrCount function below.
def substrCount(n, s):
    # find all substrings
    substrings = []
    for window_size in range(1, n+1, 1):
        for start_pos in range(0, n - window_size + 1, 1):
            substrings.append(s[start_pos:(start_pos+window_size)])
    # work on those strings to check
    count = 0
    #print(f"Debug: num substrings {len(substrings)}")
    for this_string in substrings:
        len_str = len(this_string)
        first_char = this_string[0]
        special = True
        for offset in range(0,int(len_str/2),1):
            i = offset
            j = (len_str -1) - offset
            if not (this_string[i] == this_string[j] == first_char):
                special = False
                break
        if special:
            count += 1
    return count

def substrCount_anotherversion(n, s):
    # work on those strings to check
    count = n
    for window_size in range(2, n+1, 1):
        for start_pos in range(0, n - window_size + 1, 1):
            this_string = s[start_pos:(start_pos+window_size)]
            counts = dict([(l,this_string.count(l)) for l in set(this_string)])
            if len(counts) == 1:
                # All same
                count += 1
            elif len(counts) == 2:
                counts = [(k, v) for k, v in sorted(counts.items(),\
                                                        key=lambda item: item[1])]
                if ( counts[0][1] == 1 \
                        and counts[1][1]%2==0 \
                    and counts[0][0] == this_string[int(len(this_string)/2)]):
                    count += 1
            else:
                pass
    return count



# Minimum deletions to make anagrams
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def makeAnagram(a, b):
    # Write your code here
    # dict of letter counts from strings
    dict_a = dict([(l, a.count(l)) for l in set(a)])
    dict_b = dict([(l, b.count(l)) for l in set(b)])
    # create union of all letters
    set_all_letters = set(dict_a.keys()) | set(dict_b.keys())
    all_occur = [(l, dict_a.get(l,0), dict_b.get(l,0)) for l in set_all_letters]
    deletions = sum([abs(o[1] - o[2]) for o in all_occur])
    return deletions


## queries and operation
def freqQuery(queries):
    store = {}
    resp = []
    for query in queries:
        if query[0] == 1:
            if query[1] in store:
                store[query[1]] = store[query[1]] + 1
            else:
                store[query[1]] = 1
        elif query[0] == 2:
            if query[1] in store:
                store[query[1]] = store[query[1]] - 1
                if store[query[1]] == 0:
                    del store[query[1]]
        elif query[0] == 3:
            if query[1] in set(store.values()):
                resp.append(1)
            else:
                resp.append(0)
        else:
            pass
    return resp
    

# Two strings are anagrams of each other if the letters of one string 
# can be rearranged to form the other string. Given a string, find the 
# number of pairs of substrings of the string that are anagrams of each other.
def sherlockAndAnagrams(s):
    counter = 0
    # Write your code here
    for l in range(1,len(s)+1,1):
        substrings  = []
        for start_pos in range(0, len(s)-l+1,1):
            substrings.append(s[start_pos:(start_pos+l)])
        # we have substrings here. We can find pairs which can be anagrams
        # of each other
        for i in range(len(substrings)):
            this_str = substrings[i]
            # word counts dict
            this_str_set = set(substrings[i])
            this_str_dict = dict((x,this_str.count(x)) for x in this_str_set)
            for j in range(i+1,len(substrings),1):
                compare_str = substrings[j]
                compare_str_set = set(compare_str)
                compare_str_dict = dict((x,compare_str.count(x))\
                                         for x in compare_str_set)
                if this_str_dict == compare_str_dict:
                    counter += 1
    return counter


# check if any substrings - if any even of single character
def twoStrings(s1, s2):
    # Write your code here
    s1_set = set(s1)
    for l in s2:
        if l in s1:
            return("YES")
    return("NO")


# Hash table/dictionary
def checkMagazine(magazine, note):
    # Write your code here
    magazine_dict = {}
    for mw in magazine:
        if mw in magazine_dict:
            magazine_dict[mw] = magazine_dict[mw] + 1
        else:
            magazine_dict[mw] = 1
    
    for nw in note:
        if (nw in magazine_dict) and magazine_dict[nw] > 0:
            magazine_dict[nw] = magazine_dict[nw] - 1
        else:
            print("No")
            return
    print("Yes")
    return
              
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
def hourglassSum(arr):
    # Write your code here
    max_sum = -math.inf
    for row_idx in range(len(arr) - 2):
        for col_idx in range(len(arr) - 2):
            v = sum(arr[row_idx][col_idx:(col_idx+3)])\
               + arr[row_idx+1][col_idx+1]\
               + sum(arr[row_idx+2][col_idx:(col_idx+3)])
            if v > max_sum:
                max_sum = v
    return max_sum


#Read inputs from screen and write to file
def read_input_and_write_to_file():
    # writing into a file
    fptr = open("test_output.txt", 'w')
    arr = []
    
    # takes integers separated by space and adds to array
    # makes 2D integer array as we read and create a list of each line
    # and save to list of lists
    for _ in range(3):
        print("Please enter input line:")
        line = input()
        line = line.rstrip().lstrip()
        elements = line.split()
        arr.append(list(map(int, elements)))
    print("the 2d array is:" + str(arr))
    # write to file
    fptr.write(str(arr) + '\n')
    # close the file
    fptr.close()



# Read a full line of input from stdin and save 
# it to our dynamically typed variable, input_string.
def read_line_from_stdin():
    print("Please enter input line:")
    input_string = input()
    print("got " + input_string)


# Rotate Right: a input, d rotate by
def rotRight(a, d):
    # Write your code here
    len_a = len(a)
    pos_shift = d%len_a
    res = []
    for i in range(-pos_shift,(-pos_shift) +len_a,1):
        res.append(a[i])
    return res

def rotLeft(a, d):
    # Write your code here
    len_a = len(a)
    pos_shift = d%len_a
    res = []
    for i in range(pos_shift,(pos_shift) +len_a,1):
        res.append(a[i%len_a])
    return res

# Fails in one test case
def minimumBribes(q):
    # Write your code here
    min_bribes = 0
    for i in range(len(q)):
        if (q[i] - (i+1)) > 2:
            print("Too chaotic")
            return
        min_bribes += max(q[i] - (i+1),0)
    print(min_bribes)


# Longest common child
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#
# This gives max recursion depth error
def commonChild(s1, s2):
    # Write your code here
    cache={}
    def longest(x_pos,y_pos):
        if (x_pos,y_pos) in cache:
            return cache[(x_pos,y_pos)]
        value = None
        if x_pos < 0 or y_pos < 0:
            value = 0
        else:
            if s1[x_pos] == s2[y_pos]:
                value = 1 + longest(x_pos-1, y_pos-1)
            else:
                value = max(longest(x_pos, y_pos-1), longest(x_pos-1, y_pos))
        cache[(x_pos,y_pos)] = value
        return value
    return longest(len(s1)-1,len(s2)-1)

# NAother way to fill table without recursive calls.
def commonChild_table_fill_method(s1, s2):
    # Write your code here
    len_s1 = len(s1)
    len_s2 = len(s2)
    # Create a cache matrix : we should make to take care of first cells
    tbl = [[0]*(len_s1 +1) for _ in range(len_s2+1)]
    #i,j corresspond to matrix, imagine initials as 0
    for i in range(1,len_s1+1):
        for j in range(1, len_s2+1):
            if s1[i-1] == s2[j-1]:
                # diagonal + 1
                tbl[i][j] = 1 + tbl[i-1][j-1]
            else:
                tbl[i][j] = max(tbl[i-1][j], tbl[i][j-1])
    return tbl[len_s1][len_s2]


def main():
    #read_line_from_stdin()
    #read_input_and_write_to_file()

    # Rotate left input
    print("Please enter input numbers:")
    line = input()
    arr = list(map(int, line.rstrip().lstrip().split()))
    print("Initial: " + str(arr))
    rotated = rotLeft(arr, 1)
    print("Rotated: " + str(rotated))



# Solve integral points
def solve(x1, y1, x2, y2):
    # Write your code here    
    # case 1 line is vertical
    if x1 == x2:
        y1, y2 =  (y1, y2) if y1 < y2 else (y2, y1)
        return sum([y for y in range(y1+1, y2, 1)])
        
    # case 2 line is not vertical
    # make x1 on left side of x2 as answer does not change
    x1, x2, y1, y2 = (x1, x2, y1, y2) if x1 < x2 else (x2, x1, y2, y1)
    
    if y2 < y1:
        y2 = y2 + 2 * abs(y1 - y2)
    
    slope = ((y2 - y1)/(x2 - x1))
    integ_xs =  [x for x in range(x1, x2, 1)]
    integ_ys =  [y1 + slope * (x - x1) for x in integ_xs]
    integ_ys =  [1 for y in integ_ys if abs(int(y) - y) < 1e-7]
    print("Returing {}".format(sum(integ_ys) -1))
    return sum(integ_ys) -1
    
def solve_integral_points():
    fptr = open("solve_integral_points.txt", 'w')
    first_input = input()
    print("Debug first_input>{}< type:{}".format(first_input, type(first_input))) 
    t = int(first_input.rstrip().rstrip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        x1 = int(first_multiple_input[0])
        y1 = int(first_multiple_input[1])
        x2 = int(first_multiple_input[2])
        y2 = int(first_multiple_input[3])
        result = solve(x1, y1, x2, y2)
        print("first_multiple_input >{}< result{}".format(first_multiple_input,result))
        fptr.write(str(result) + '\n')
    fptr.close()


if __name__ == "__main__":
    # print("Hello")
    # call main
    # main()
    # 
    #s1 = "LZNGFTIHZHJSQGQQYICYKYAPAFJMYXIRFHFISJZJAVHMQLPBFXSPEEQAUJIIVSVLCRVHSMIGXQIVOOAFHIQOAOJBOTGJUPXEPQZFJSNLVDHCXMDRPPGTUNBIMARYQXUTMQVGOVZDYSCBCHRTTAYEIFFNAGFDFGEFJNAXKWUYNFPETFYTHRLEICJEFDFHJFADZFBRABLMDYNGIBXHGWDOWIFLWUKFVFUIITQGFRCGUYFZINJYIGXCKNPVDPMUKTVOIBSIUUDQDWXTJAIGVSFROIGSEOWNZAWDRIZFLFQAYQKETDOYLUOHSVUYOJLDCJNIWDOFBRLWXQSCCTDEQHGHUXCHTCFSZRTRESSXNVOXFAHSWUAVJXMHCKRCOYVENGGBSXXYPEPUAQFNNCRVFQQDFCBPNTTNISDVORWBJBBCVVNLYUTTSBPRXSKYFEKOMIZCGNSQHZYVCHHILQLGCLIKTNCLQUOUAXFNHJPIZYBYWSVMGUVAGXANTEZHSDUDBVVCAGCPKJAQXIOQOCTNNOOFUYZEGGPAEQGRRDREZUSVTKCQAZQDZAEIIGOCJPMQXRHRFQTCBNEMSAPSSLHXJVDBCSGQVUPGNCZKTFEBRIKWKSYXWRAHGNGYLLXFKJOUNXKDRWMBVOZGEOBAYYNFDNHHWFVPOKWUFLZTZUCMLGFVUWFXSVYYUBGRHAUWHBQSNIHENTXADZCCZZZPOPESVYCROMUBJPDGBGUHBSMUQSYGEHUCRDACDYJIPYBLPXQUOLSELHBBBYQHKIOVFMSXANOMKMOXNPTGZSVHMCAEFSCNMCPHFUHOMNRNEQBOSLMAHJAMSMQMGKTLVKBVTSUDDWKXHHIIAFVNMQIHVVEPACCEVVECWOBVZVTWWMDIKYZAGZJOLQCINZZVZFNJGTCXXVLRAGJQFDMYMNKQDWNCLRTPYCCXEQFGKQWQSSYXNGELLNMAKNPIKFNKUIDCRUTWSTRKIHUAOGMPXOBQTFFAQMKG"
    #s2 = "BLCRCQQMXZCBACBDSFGIQDKFFHGPOGSZLHLXNZSSXRGVKIGNABASNFZDHVJOAINPZEZNDWOWSEJGMOVPPXHBERDJXLJSPAQDKNQEJMTBMVTPRXOCHYPKMDGRIHUPBQWZBNIXJBPTFYRMIUNXLVKPIRLLGJVGBIBIGDRIWGKEIKKYGCCFHCTEVNJPWFCFPDOXQDYGHRRNXTFQRGCTITBUEPHPEIXQMYSKLYQXZWVRWDBYLJRBOWRAHRWUJWZKEGBCEHVTKJERFIJVWWVSRVNIDHYVEYIWAPHYSIKCBDBDWXAWXEHRFMHCQNHTBYOFYJBIKJGUDIMQKNFCKMWNGVROISVLPZZCRUKHBWPSHRBSERBQOJXFTKSDDCRBIACQMHIOQBNESXTNURRXONVMNGZBMBDZDBWGXMFNCJWVUICKVQHUDDMVHNHRAHRDHOITKDDRRMFSQFZSLAASQSKJTVWTOSWQSPEARPEWADMMNSPCZTMKGVQOBGOBMGICUZNBEBZBFDRPFJPLCJOUTZBNJAKTTMQPQVQOGVHIBNWFXOQWSMUSCBBCZURZOYRHSTKIFUXWROLBQBLYEDXQHKXYZNWVDCRAABKUBAPCPLKPZRQWNSWRCLNGDYLICBQAPPFNIDNCRMZEJJNNSUDDMAAOJPDQZPBRYKMVACVMTNNPQZBWHYALBHLDAYTJGJOWXQYVQQVNHLJXVVEXIPHEZZCKLKXNKLAYSHPSWWBPOQXZJYNFWBYVMMTMKFWJVPGHTGXCMBKTBWIXQJAMGVNRALOCACXIICCVEWKKSFDBMPRJUEYCHROEDXTKYJYSGVITYMVSAAEVKDAEDXWDBSHFTXDCDRTLCCFAKWSBNTPUSXIGTSXOVPIMVURDXOGBOOQAHISZBKADCRXVSJSICXWQNMQGCCPTHWHKFKDXUGARNLREDXZIROXZTXPAVOGORNCVXGAMFVJUKLGPHSZKVVMRMFXLYUZNDUYOIIHJCKDWQXNCIYNG"
    #val  = commonChild(s1,s2)
    #print(val)
    solve_integral_points()
    print("exiting..")

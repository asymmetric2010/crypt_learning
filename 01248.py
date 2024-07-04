""" 01248 密码,该密码又称为云影密码，使用 0，1，2，4，8 四个数字，
其中 0 用来表示间隔，其他数字以加法可以表示出 如：28=10，124=7，18=9，再用 1->26 表示 A->Z。 """

def yunying_decode(c):
    t="abcdefghijklmnopqrstuvwxyz"
    l=c.split("0")
    r=""
    for i in l:
        tep=0
        for j in i:
            tep+=int(j)
        r+=t[tep-1]
    return r

if __name__ =="__main__":
    print(yunying_decode("8842101220480224404014224202480122"))

"""
    min_rect  2*1

    big rect    method
      2*1        1    h
      2*2        2    hh  vv
      2*3        3    hhh  hvv  vvh
      2*4        5    hhhh  hhvv  hvvh  vvhh  vvvv
      2*5        8    hhhhh  hhhvv  hhvvh  hvvhh  hvvvv  vvhhh  vvhvv  vvvvh
      2*6        13   hhhhhh   hhhhvv   hhhvvh   hhvvhh   hhvvvv   hvvhhh   hvvhvv   hvvvvh
                      vvhhhh   vvhhvv   vvhvvh   vvvvhh   vvvvvv
"""

"""
    min_rect  2*1

    big rect    method
      2*1        1    
      2*2        2
      2*3        第一个为h,剩余的同2*2，第一个为vv，剩余同2*1
      2*4        第一个为h,剩余的同2*3，第一个为vv，剩余同2*2
      2*5        第一个为h,剩余的同2*4，第一个为vv，剩余同2*3
      2*6        第一个为h,剩余的同2*5，第一个为vv，剩余同2*4
"""


class Solution:
    def rectCover(self, number):
        # write code here
        n1, n2, count, target = 1, 2, 0, 0
        if number == 1:
            return n1
        if number == 2:
            return n2
        while number > count + 2:
            target = n1 + n2
            count += 1
            n1 = n2
            n2 = target
        else:
            return target


if __name__ == '__main__':
    s = Solution()
    re = s.rectCover(6)
    print(re
)
class Solution:
    def is_digits(self, num, num_set):
        if len(num) == 0:
            return False
        for d in num:
            if d not in num_set:
                return False
        return True

    def is_decimal(self, num, num_set):
        if '.' not in num:
            return False
        splits = num.split('.')
        if len(splits) != 2:
            return False
        pt1, pt2 = splits[:]
        if len(pt2) == 0 and len(pt1) == 0:
                return False
        # if len(pt1) > 0 and pt1[0] in ['-', '+']:
        #     pt1 = pt1[1:]
        if len(pt1) == 0:
            first_part = True
        else:
            first_part = self.is_digits(pt1, num_set)
        if len(pt2) == 0:
            second_part = True
        else:
            second_part = self.is_digits(pt2, num_set) 
        return first_part and second_part
    
    def isNumber(self, s: str) -> bool:
        num_set = set([str(x) for x in range(10)])
        if s[0] in ["-", '+']:
            s = s[1:]
        where_e = s.find('e')
        if where_e != -1:
            splits = s.split('e')
            if len(splits) != 2:
                return False
            pt1, pt2 = splits[:]
            if len(pt1) == 0 or len(pt2) == 0:
                return False
            if pt2[0] in ['-', '+']:
                pt2 = pt2[1:]
            first_part = (self.is_decimal(pt1, num_set) or self.is_digits(pt1, num_set))
            return first_part and self.is_digits(pt2, num_set)
        where_E = s.find('E')
        if where_E != -1:
            splits = s.split('E')
            if len(splits) != 2:
                return False
            pt1, pt2 = splits[:]
            if len(pt1) == 0 or len(pt2) == 0:
                return False
            if pt2[0] in ['-', '+']:
                pt2 = pt2[1:]
            first_part = (self.is_decimal(pt1, num_set) or self.is_digits(pt1, num_set))
            return first_part and self.is_digits(pt2, num_set)    
        else:
            return self.is_decimal(s, num_set) or self.is_digits(s, num_set)
        
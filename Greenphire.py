from collections import Counter
from collections import OrderedDict
import random

def get_input(question):
    return input(question)

class Employee:

    def _init__(self, name, powerball):
        self.name = name
        self.powerball = powerball

    def get_name(self):
        fname = get_input("Enter your first name:")
        lname = get_input("Enter your last name:")
        name = fname + ' ' + lname
        return name

    def get_powerball_num(self):
        fav_nums = get_fav_nums()
        pb = get_pbnum()
        return fav_nums, pb


def get_fnum(fnum=None, maxnum=None):
    if isinstance(fnum,int) and isinstance(maxnum,int):
      if fnum in range(1,maxnum):
         return fnum


def get_fav_nums():
    fav_nums = []

    cnt = 0
    while (cnt == 0):
        fnum0 = get_input("select 1st # (1 thru 69): ")
        try:
            if get_fnum(int(fnum0), 70) is not None:
                fav_nums.append(get_fnum(int(fnum0), 70))
                cnt += 1
            else:
                print('Please enter unique numeric values 1 thru 69 ')
        except ValueError as e:
                print('Please enter numeric values', e)

    cnt = 0
    while (cnt==0):
        fnum1 = get_input("select 2nd # (1 thru 69 excluding " + fnum0 + "): ")
        try:
            if int(fnum1) != int(fnum0) and get_fnum(int(fnum1), 70) is not None:
                fav_nums.append(get_fnum(int(fnum1),70))
                cnt+= 1
            else:
                print('Duplicate or Out of Range Value. Please enter unique values 1 thru 69 ')
        except ValueError as e:
            print('Please enter numeric values', e)

    cnt = 0
    while (cnt==0):
        fnum2 = get_input("select 3rd # (1 thru 69 excluding " + fnum0 + " and " + fnum1 + "): ")
        try:
            if (int(fnum2) != int(fnum1)) and (int(fnum2) != int(fnum0)) and get_fnum(int(fnum2), 70) is not None:
                fav_nums.append(get_fnum(int(fnum2),70))
                cnt+=1
            else:
                print('Duplicate or Out of Range Value. Please enter unique values 1 thru 69 ')
        except ValueError as e:
            print('Please enter numeric values', e)

    cnt = 0
    while (cnt==0):
        fnum3 = get_input("select 4th # (1 thru 69 excluding " + fnum0 + " and " + fnum1 + " and " + fnum2 + "): ")
        try:
            if (int(fnum3) != int(fnum2)) and (int(fnum3) != int(fnum1)) and (int(fnum3) != int(fnum0)) and get_fnum(int(fnum3), 70) is not None:
                fav_nums.append(get_fnum(int(fnum3),70))
                cnt+=1
            else:
                print('Duplicate or Out of Range Value. Please enter unique values 1 thru 69 ')
        except ValueError as e:
            print('Please enter numeric values', e)

    cnt = 0
    while (cnt==0):
        fnum4 = get_input("select 5th # (1 thru 69 excluding " + fnum0 + " and " + fnum1 + " and " + fnum2 + " and " + fnum3 + "): ")
        try:
            if (int(fnum4) != int(fnum3)) and (int(fnum4) != int(fnum2)) and (int(fnum4) != int(fnum1)) and (int(fnum4) != int(fnum0)) and get_fnum(int(fnum4), 70) is not None:
                fav_nums.append(get_fnum(int(fnum4),70))
                cnt += 1
            else:
                print('Duplicate or Out of Range Value. Please enter unique values 1 thru 69 ')
        except ValueError as e:
            print('Please enter numeric values', e)

    return fav_nums

def get_pbnum():
    pb = []

    cnt = 0
    while (cnt==0):
        pbnum = get_input("select Power Ball # (1 thru 26): ")
        try:
            if get_fnum(int(pbnum), 27) is not None:
                pb.append(get_fnum(int(pbnum),27))
                cnt += 1
            else:
                print('Out of Range Value. Please enter unique values 1 thru 26 ')
        except ValueError as e:
            print('Please enter numeric values', e)

    return pb

def get_emp():
    emp = Employee()
    name = emp.get_name()
    fav_nums,pb  = emp.get_powerball_num()
    empval = ((name) + " " + " ".join(str(x) for x in fav_nums) + " Powerball: " + " ".join(str(x) for x in pb))
    return empval, fav_nums, pb

def main():
    Empl = ''
    fav_nums_list = []
    pb_list = []
    fnum_res2 = []
    fnum_res3 = []
    fnum_res4 = []
    fnum_res5 = []
    empval, fav_nums, pb = get_emp()
    Empl = Empl + '' + (empval)
    fav_nums_list=fav_nums_list + fav_nums
    pb_list = pb_list + pb
    emp_flag = get_input('Do you want to enter next employee and continue Y/N?')

    while (emp_flag == 'Y' or emp_flag == 'y'):
        empval, fav_nums, pb = get_emp()
        Empl = Empl + '\n' + (empval)
        fav_nums_list = fav_nums_list + fav_nums
        pb_list = pb_list + pb
        emp_flag = get_input('Do you want to enter next employee and continue Y/N?')

    if (emp_flag != 'Y') or (emp_flag != 'y'):
        fnum_freq_list = Counter(fav_nums_list)  #counts the hashable list of favorite numbers
        res = fnum_freq_list.most_common()       #returns the list of common elements and their counts

        newdict = {}
        for k,v in res:
            newdict.setdefault(v,[]).append(k)   # setting defaults while filling the dict
        ndict = OrderedDict(reversed(list(newdict.items())))   # reversing sorted dict to get the most duplicate values in the beginning

        for key in ndict:
            if key > 1:
                fnum_res2.append(str(ndict[key]))
            else:
                fnum_res3.append(str(ndict[key]))

        fnum_res2 = ' '.join(map(str, fnum_res2)).replace('[','').replace(']','').replace(',','')
        fnum_res2 = list(map(int,fnum_res2.split()))
        fnum_res3 = ' '.join(map(str, fnum_res3)).replace('[','').replace(']','').replace(',','')
        fnum_res3 = list(map(int, fnum_res3.split()))

        if len(fnum_res2) > 4:                     # get the first 5 most duplicate values
           final = ' '.join(map(str, fnum_res2[:5]))
        else:                                      # get the most available duplicate values and rest of them randomly until 5 values are extracted
            num_to_select = (5 - len(fnum_res2))
            final = random.sample(fnum_res3, num_to_select) + fnum_res2
            final = ' '.join(map(str, final))

        pb_freq_list = Counter(pb_list)
        res1 = pb_freq_list.most_common()

        newdict1 = {}
        for k, v in res1:
            newdict1.setdefault(v, []).append(k)
        ndict1 = OrderedDict(reversed(list(newdict1.items())))

        for key in ndict1:
            if key > 1:
                fnum_res4.append(str(ndict1[key]))
            else:
                fnum_res5.append(str(ndict1[key]))

        fnum_res4 = ' '.join(map(str, fnum_res4)).replace('[', '').replace(']', '').replace(',', '')
        fnum_res4 = list(map(int, fnum_res4.split()))
        fnum_res5 = ' '.join(map(str, fnum_res5)).replace('[', '').replace(']', '').replace(',', '')
        fnum_res5 = list(map(int, fnum_res5.split()))

        if len(fnum_res4) > 0:                          # get the most duplicate value if not get a random value frpm the list
            final1 = str(random.choice(fnum_res4))
            final1 = ' '.join(map(str, fnum_res4[:1]))
        else:
            final1 = str(random.choice(fnum_res5))

    print(Empl)
    print("Powerball winning number: " + final + " Powerball: " + final1)

if __name__ == "__main__":
    main()








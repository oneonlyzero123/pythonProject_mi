# 练习 8.16：导⼊ 选择⼀个你编写的且只包含⼀个函数的程序，将这
# 个函数放在另⼀个⽂件中。在主程序⽂件中，使⽤下述各种⽅法导⼊
# 这个函数，再调⽤它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
import printing_functions
from printing_functions import print_models
from printing_functions import print_models as pm
import printing_functions as pf
from  printing_functions import *
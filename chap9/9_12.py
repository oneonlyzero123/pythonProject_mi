# 练习 9.12：多个模块 将 User 类存储在⼀个模块中，并将
# Privileges 类和 Admin 类存储在另⼀个模块中。再创建⼀个⽂件，
# 在其中创建⼀个 Admin 实例并对其调⽤ show_privileges() ⽅
# 法，以确认⼀切依然能够正确地运⾏。
#
from adminfiles_nouser import Admin
Tom_admin=Admin('tom','feng','priston')
Tom_admin.show_privileges()
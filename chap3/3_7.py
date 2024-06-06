#3.7
invited=['tom','jack','tony']
print("i can only invite 2 friends to have dinner")
popped_inv1=invited.pop(1)
print(popped_inv1+"sorry,i can't invite you")
popped_inv2=invited.pop(2)
print(popped_inv2+"sorry,i can't invite you")
popped_inv3=invited.pop(3)
print(popped_inv3+"sorry,i can't invite you")
popped_inv4=invited.pop(0)
print(popped_inv4+"sorry,i can't invite you")
print(invited[0]+"you are still invited")
print(invited[1]+"you are still invited")
del invited[0]
del invited[0]
print(invited)
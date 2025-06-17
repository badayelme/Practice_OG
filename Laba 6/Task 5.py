C = input("Enter C: ")
A = ["huskih","househ","horse","hmamah","dad","hpriush","pattth","home","hhh","hahah"]
count = 0
for i in A:
    if len(i) > 1 and i.startswith("h") and i.endswith("h"):
        count += 1
print(A)
print(f"Count: {count}")
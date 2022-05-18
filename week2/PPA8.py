start = input()
end = input()

files = "ABCDEFGH"

if abs(files.index(start[0]) - files.index(end[0])) == abs(int(start[1]) - int(end[1])):
    print("YES")
else:
    print("NO")
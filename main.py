def parse():
    with open("teste.txt", "r") as f:
        texto = f.read()
    global tokens
    tokens = texto.split()

nums = []
op = []
opOr = ['+', '-', '/', '*'] 
comandos = []
def separarTokens():
    for i in range(len(tokens)):
        global tks
        tks = list(tokens[i], tokens[i+1], tokens[i+2])
def tokenize():
    global comandos
    comandos.append(f"print(")
    for i in range(len(tokens)):
        print(i)
        while len(nums) < 2 or len(op) < 1:
            if len(op) > 1 or len(nums) > 2 or i >= len(tokens):
                raise Exception
            if tokens[i].isdigit():
                nums.append(tokens[i])
                i+=1
                print("loop1")
            elif tokens[i] in opOr:
                op.append(tokens[i])
                i+=1
                print("loop2")
        comandos.append(nums[0])
        comandos.append(op[0])
        comandos.append(nums[1])
        comandos.append(", ")
        print(comandos)

        op.clear()
        nums.clear()
        print(op,nums)
    comandos.append(f")\n")
        

def executar():
    cmd =  "".join(comandos)
    exec(cmd)
# tokenize()
# executar()
parse()
separarTokens()
print(tks)

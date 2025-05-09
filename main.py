opDisponiveis = ['+','-','*','/']
tokens = []
buff = []
nsrc = []
op = []
nums = []
comandos = []

with open("teste.txt", "r") as f:
    src = f.read()
src = src.split()

for tk in src:
    if len(tk) > 1 and not tk.isdigit():
        tk = list(tk)
        for i in range(len(tk)):
            nsrc.append(tk[i])
    else:
        nsrc.append(tk)

def parse(): 
    for tk in nsrc:
        if tk != ';':
            buff.append(tk) 
        else:
            tokens.append(buff[:])
            buff.clear()

def tokenize():
    comandos.append(f"print(")
    for token in tokens:
        for tk in token:
            if tk.isdigit():
               nums.append(tk) 
            elif tk in opDisponiveis:
                op.append(tk)
            else:
                raise Exception("Sintáxe Inválida")
        comandos.append(nums[0])
        comandos.append(op[0])
        comandos.append(nums[1])
        comandos.append(",")
        op.clear()
        nums.clear()

    comandos.append(f")\n")  

def executar():
    cmd =  "".join(comandos)
    exec(cmd)

def main():
    parse()
    tokenize()
    executar()

if __name__ == "__main__":
    main()
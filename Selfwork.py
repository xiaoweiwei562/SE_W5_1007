def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def read_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("可以輸入有效的數字嗎？你是真的讓人無語誒 流汗.jpg")

def read_operator():
    valid = {"+", "-", "*", "/", "q", "Q"}
    while True:
        op = input("請輸入運算子 (+, -, *, /)；或輸入 q 離開：").strip()
        if op in valid:
            return op.lower()
        print("逆天，運算字或退出提示我都給你了，也能輸入錯？？ 翻白眼.jpg")

def fmt(x):
    return f"{x:g}"

def main():
    print("=== 量子計算機 ===")
    print("測試版本，目前接受投資 LINEPAY.jpg,未來量子計算機已開始研發，請大家多多支持\t 支援：加(+)、減(-)、乘(*)、除(/)；輸入 q 可離開。\n")

    while True:
        choice = read_operator()
        if choice == "q":
            print("再也不見")
            break

        num1 = read_number("請輸入第一個數字：")
        if choice == "/":
            while True:
                num2 = read_number("請輸入第二個數字（不可為 0）：")
                if num2 == 0:
                    print("聽不懂人話？貓語言總聽懂了吧？喵喵？喵？？ 喵！")
                else:
                    break
        else:
            num2 = read_number("請輸入第二個數字：")

        # 運算對應表
        ops = {
            "+": ("加法", add),
            "-": ("減法", subtract),
            "*": ("乘法", multiply),
            "/": ("除法", divide),
        }

        op_name, func = ops[choice]
        result = func(num1, num2)
        print(f"这都不懂？ {op_name}結果：{fmt(num1)} {choice} {fmt(num2)} = {fmt(result)}\n")

if __name__ == "__main__":
    main()


from calculator import DigitalYiJingCalculator

def main():
    print("--- 數字易經磁場分析器 ---")
    user_input = input("請輸入一串數字（例如手機號碼、身分證號碼）: ").strip()

    results = DigitalYiJingCalculator.analyze_number(user_input)

    print(f"\n--- 「{user_input}」的磁場分析結果 ---")
    if results:
        for result in results:
            print(result)
    print("---------------------------------")


if __name__ == "__main__":
    main()

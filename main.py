def show_menu():
    print("=" * 40)
    print("       🎭 뮤지컬 맞히기 퀴즈 🎭")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

def get_menu_choice():
    while True:
        user_input = input("선택: ").strip()

        if user_input == "":
            print("아무것도 입력하지 않았습니다.")
            continue

        try:
            choice = int(user_input)
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if 1 <= choice <= 5:
            return choice

        print("1부터 5 사이의 숫자를 입력해주세요.")

def main():
    try:
        while True:
            show_menu()
            choice = get_menu_choice()

            if choice == 1:
                print("퀴즈 풀기 기능은 준비 중입니다.")
            elif choice == 2:
                print("퀴즈 추가 기능은 준비 중입니다.")
            elif choice == 3:
                print("퀴즈 목록 기능은 준비 중입니다.")
            elif choice == 4:
                print("점수 확인 기능은 준비 중입니다.")
            elif choice == 5:
                print("퀴즈 게임을 종료합니다.")
                break

            print()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다.")
        print("퀴즈 게임을 안전하게 종료합니다.")

main()
        
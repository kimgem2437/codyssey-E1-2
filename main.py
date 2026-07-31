class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer

def create_default_quizzes():
    quizzes = [
        Quiz(
            "장발장과 자베르가 등장하는 뮤지컬은?",
            ["위키드", "레미제라블", "시카고", "캣츠"],
            2
        ),
        Quiz(
            "엘파바와 글린다가 등장하는 뮤지컬은?",
            ["디어 에반 핸슨", "지킬 앤 하이드", "위키드", "맘마미아"],
            3
        ),
        Quiz(
            "대표 넘버 'Land of Lola'가 등장하는 뮤지컬은?",
            ["서편제", "킹키부츠", "헤드윅", "그리스"],
            2
        ),
        Quiz(
            "오르페우스, 헤르메스, 에우리디케가 등장하는 뮤지컬은?",
            ["원스", "헤드윅", "데스노트", "하데스타운"],
            4
        ),
        Quiz(
            "대표 넘버 'The Phantom of the Opera'가 등장하는 뮤지컬은?",
            ["오페라의 유령", "렌트", "웃는 남자", "프랑켄슈타인"],
            1
        )
        
    ]

    return quizzes

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
    quizzes = create_default_quizzes()

    try:
        while True:
            show_menu()
            choice = get_menu_choice()

            if choice == 1:
                print("퀴즈 풀기 기능은 준비 중입니다.")
            elif choice == 2:
                print("퀴즈 추가 기능은 준비 중입니다.")
            elif choice == 3:
                print(f"현재 등록된 퀴즈는 {len(quizzes)}개입니다.")
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
        
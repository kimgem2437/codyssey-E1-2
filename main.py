import json

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

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.last_score = None
        self.last_total = 0
        self.best_score = 0

    def play_quiz(self):
        score = 0

        print("\n뮤지컬 퀴즈를 시작합니다!")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{number}/{len(self.quizzes)}번 문제]")

            quiz.display()

            user_answer = get_number_input("정답: ", 1, 4)

            if quiz.is_correct(user_answer):
                print("정답입니다!")
                score += 1
            else:
                correct_choice = quiz.choices[quiz.answer - 1]
                print(
                    f"오답입니다. 정답은 "
                    f"{quiz.answer}번 {correct_choice}입니다."
                )
        print(f"\n최종 점수: {score}/{len(self.quizzes)}점")

        self.last_score = score
        self.last_total = len(self.quizzes)

        if score > self.best_score:
            self.best_score = score

    def add_quiz(self):
        print("\n새로운 뮤지컬 퀴즈를 추가합니다.")

        question = get_text_input("문제: ")

        choices = []

        for number in range(1, 5):
            choice = get_text_input(f"{number}번 선택지: ")
            choices.append(choice)

        answer = get_number_input("정답 번호: ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다.")

    def list_quizzes(self):
        print("\n등록된 퀴즈 목록")

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n{number}. {quiz.question}")

            for choice_number, choice in enumerate(quiz.choices, start=1):
                print(f"    {choice_number}) {choice}")

            correct_choice = quiz.choices[quiz.answer - 1]
            print(f"    정답: {quiz.answer}번 {correct_choice}")

    def show_score(self):
        print("\n점수 확인")

        if self.last_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
            print(f"최고 점수: {self.best_score}점")
            return

        print(f"최근 점수: {self.last_score}/{self.last_total}점")
        print(f"최고 점수: {self.best_score}점")

    def save_data(self):
        data = {
            "quizzes": [
                quiz.to_dict() for quiz in self.quizzes
            ],
            "best_score": self.best_score 
        }

        try:
            with open(
                "state.json",
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )
        except OSError:
            print("데이터를 저장하는 중 오류가 발생했습니다.")
    

    def run(self):
        try:
            while True:
                show_menu()
                choice = get_menu_choice()

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.list_quizzes()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    self.save_data()
                    print("데이터를 저장했습니다.")
                    print("퀴즈 게임을 종료합니다.")
                    break

                print()
        except (KeyboardInterrupt, EOFError):
            self.save_data()
            print("\n입력이 중단되었습니다.")
            print("데이터를 저장했습니다.")
            print("퀴즈 게임을 안전하게 종료합니다.")

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
        ),
        Quiz(
            "여러 뮤지컬을 오마주해서 셰익스피어 배경으로 만든 뮤지컬은?",
            ["어쩌다 해피엔딩", "레베카", "맨 오브 라만차", "썸싱로튼"],
            4
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

def get_number_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt).strip()

        if user_input == "":
            print("아무것도 입력하지 않았습니다.")
            continue

        try:
            number = int(user_input)
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if min_value <= number <= max_value:
            return number

        print(f"{min_value}부터 {max_value} 사이의 숫자를 입력해주세요.")

def get_menu_choice():
    return get_number_input("선택: ", 1, 5)

def get_text_input(prompt):
    while True:
        text = input(prompt).strip()

        if text != "":
            return text

        print("아무것도 입력하지 않았습니다.")

def main():
    game = QuizGame(create_default_quizzes())
    game.run()

main()
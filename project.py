import streamlit as st

# ===============================Ss===========
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="My Profile & Calculator",
    page_icon="👤",
    layout="centered"
)


st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(120, 170, 255, 0.28), transparent 30%),
        radial-gradient(circle at 85% 15%, rgba(190, 130, 255, 0.24), transparent 30%),
        radial-gradient(circle at 70% 85%, rgba(80, 200, 180, 0.20), transparent 30%),
        linear-gradient(135deg, #eef4ff 0%, #f7f1ff 50%, #eefcf9 100%);
}

.block-container {
    background: rgba(255, 255, 255, 0.78);
    padding: 2rem 2rem 3rem 2rem;
    border-radius: 24px;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 40px rgba(50, 60, 100, 0.12);
}

h1, h2, h3 {
    color: #24304a;
}

div.stButton > button {
    border-radius: 12px;
    border: 1px solid rgba(80, 100, 150, 0.15);
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(50, 70, 120, 0.15);
}
</style>
""", unsafe_allow_html=True)

<style>
.calc-title {
    text-align: center;
    font-size: 28px;
    font-weight: 700;
    margin: 8px 0 14px 0;
}

.calc-display {
    background: #151515;
    color: white;
    border-radius: 22px;
    padding: 22px 18px;
    min-height: 90px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-end;
    overflow: hidden;
    margin: 0 auto 14px auto;
    max-width: 430px;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,.05);
}

.calc-expression {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 18px;
    color: #a7a7a7;
    min-height: 24px;
    overflow-wrap: anywhere;
}

.calc-result {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: clamp(38px, 10vw, 58px);
    font-weight: 300;
    line-height: 1.05;
    overflow-wrap: anywhere;
}

@media (max-width: 600px) {
    .block-container {
        padding: 1rem .7rem 2rem .7rem;
    }

    .calc-title {
        font-size: 25px;
    }

    .calc-display {
        border-radius: 20px;
        padding: 18px 15px;
        margin-bottom: 10px;
    }

    div[data-testid="column"] {
        padding: 3px !important;
    }

    div[data-testid="column"] button {
        min-height: 58px !important;
        height: 58px !important;
        border-radius: 50% !important;
        font-size: 23px !important;
        padding: 0 !important;
    }
}

@media (min-width: 601px) {
    .calc-display {
        margin-left: auto;
        margin-right: auto;
    }
}
</style>



# ==========================================
# PROFILE
# ==========================================

st.title("👋 My Profile")

st.write("Fill in your information and create your personalized profile!")

name = st.text_input("👤 What is your name?")

age = st.number_input(
    "🎂 How old are you?",
    min_value=1,
    max_value=100,
    value=18,
    step=1
)

school = st.text_input("🏫 What school do you go to?")

subject = st.text_input("📚 What is your favorite subject?")

hobby = st.text_input("🎨 What is your favorite hobby?")


if st.button("✨ Create My Profile", key="profile"):

    if name and school and subject and hobby:

        st.success("Profile created successfully!")

        st.subheader(f"🌟 Hello, {name}!")

        st.markdown(f"""
### About Me

👋 My name is **{name}**.

🎂 I am **{age} years old**.

🏫 I go to **{school}**.

📚 My favorite subject is **{subject}**.

🎨 I enjoy **{hobby}**.
""")

        st.balloons()

    else:

        st.warning("⚠️ Please fill in all the fields!")


# ==========================================
# CALCULATOR
# ==========================================

st.divider()

st.markdown('<div class="calc-title">🧮 Calculator</div>', unsafe_allow_html=True)

if "display" not in st.session_state:
    st.session_state.display = "0"

if "first_number" not in st.session_state:
    st.session_state.first_number = None

if "operator" not in st.session_state:
    st.session_state.operator = None

if "new_number" not in st.session_state:
    st.session_state.new_number = True

if "expression" not in st.session_state:
    st.session_state.expression = "0"


def press_number(number):
    if st.session_state.display == "Error":
        st.session_state.display = "0"
        st.session_state.expression = "0"

    if st.session_state.new_number:
        st.session_state.display = str(number)

        if st.session_state.first_number is not None and st.session_state.operator is not None:
            st.session_state.expression = (
                f"{format_number(st.session_state.first_number)} "
                f"{st.session_state.operator} {number}"
            )
        else:
            st.session_state.expression = str(number)

        st.session_state.new_number = False
    else:
        if st.session_state.display == "0":
            st.session_state.display = str(number)
        else:
            st.session_state.display += str(number)

        if st.session_state.first_number is not None and st.session_state.operator is not None:
            st.session_state.expression = (
                f"{format_number(st.session_state.first_number)} "
                f"{st.session_state.operator} {st.session_state.display}"
            )
        else:
            st.session_state.expression = st.session_state.display

    st.rerun()


def format_number(number):
    if number == int(number):
        return str(int(number))
    return str(round(number, 10))


def press_operator(operator):
    if st.session_state.display == "Error":
        return

    if st.session_state.first_number is not None and st.session_state.operator is not None:
        press_equals()
        st.session_state.first_number = float(st.session_state.display)

    else:
        st.session_state.first_number = float(st.session_state.display)

    st.session_state.operator = operator
    st.session_state.expression = (
        f"{format_number(st.session_state.first_number)} {operator}"
    )
    st.session_state.new_number = True

    st.rerun()


def press_equals():
    if (
        st.session_state.first_number is None
        or st.session_state.operator is None
    ):
        return

    first = st.session_state.first_number
    second = float(st.session_state.display)
    operator = st.session_state.operator

    if operator == "+":
        result = first + second

    elif operator == "-":
        result = first - second

    elif operator == "×":
        result = first * second

    elif operator == "÷":
        if second == 0:
            st.session_state.display = "Error"
            st.session_state.expression = "Error"
            st.session_state.first_number = None
            st.session_state.operator = None
            st.session_state.new_number = True
            st.rerun()
            return

        result = first / second

    else:
        return

    if result == int(result):
        result_text = str(int(result))
    else:
        result_text = str(round(result, 10))

    st.session_state.display = result_text
    st.session_state.expression = result_text
    st.session_state.first_number = None
    st.session_state.operator = None
    st.session_state.new_number = True

    st.rerun()


def press_clear():
    st.session_state.display = "0"
    st.session_state.expression = "0"
    st.session_state.first_number = None
    st.session_state.operator = None
    st.session_state.new_number = True

    st.rerun()


# ==========================================
# CALCULATOR DISPLAY
# ==========================================

st.markdown(
    f"""
    <div class="calc-display">
        <div class="calc-expression">{st.session_state.expression}</div>
        <div class="calc-result">{st.session_state.display}</div>
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# ROW 1
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", key="seven", use_container_width=True):
        press_number(7)

with col2:
    if st.button("8", key="eight", use_container_width=True):
        press_number(8)

with col3:
    if st.button("9", key="nine", use_container_width=True):
        press_number(9)

with col4:
    if st.button("÷", key="divide", use_container_width=True):
        press_operator("÷")


# ==========================================
# ROW 2
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("4", key="four", use_container_width=True):
        press_number(4)

with col2:
    if st.button("5", key="five", use_container_width=True):
        press_number(5)

with col3:
    if st.button("6", key="six", use_container_width=True):
        press_number(6)

with col4:
    if st.button("×", key="multiply", use_container_width=True):
        press_operator("×")


# ==========================================
# ROW 3
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1", key="one", use_container_width=True):
        press_number(1)

with col2:
    if st.button("2", key="two", use_container_width=True):
        press_number(2)

with col3:
    if st.button("3", key="three", use_container_width=True):
        press_number(3)

with col4:
    if st.button("-", key="minus", use_container_width=True):
        press_operator("-")


# ==========================================
# ROW 4
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("0", key="zero", use_container_width=True):
        press_number(0)

with col2:
    if st.button("C", key="clear", use_container_width=True):
        press_clear()

with col3:
    if st.button("=", key="equals", use_container_width=True):
        press_equals()

with col4:
    if st.button("+", key="plus", use_container_width=True):
        press_operator("+")

# ==========================================
# GRADE CALCULATOR
# ==========================================

st.divider()

st.header("📊 Grade Calculator")

st.write("Enter your grades for each subject.")


# ==========================================
# SUBJECT STATE
# ==========================================

if "subjects" not in st.session_state:
    st.session_state.subjects = [
        "Math",
        "English",
        "Science"
    ]


# ==========================================
# ADD MORE SUBJECTS
# ==========================================

st.subheader("➕ Add More Subjects")

new_subject = st.text_input(
    "Subject name",
    placeholder="Example: History",
    key="new_subject"
)

if st.button("Add Subject", key="add_subject"):

    if new_subject.strip():

        if new_subject.strip() not in st.session_state.subjects:

            st.session_state.subjects.append(
                new_subject.strip()
            )

            st.rerun()

        else:
            st.warning("⚠️ That subject already exists!")

    else:
        st.warning("⚠️ Please enter a subject name.")


# ==========================================
# ENTER GRADES
# ==========================================

st.subheader("📝 Enter Your Grades")

grades = {}

for sub in st.session_state.subjects:

    grades[sub] = st.number_input(
        f"📚 {sub}",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0,
        key=f"grade_{sub}"
    )


# ==========================================
# CALCULATE
# ==========================================

if st.button(
    "🧮 Calculate Grades",
    key="calculate_grades",
    use_container_width=True
):

    average = sum(grades.values()) / len(grades)


    # ==========================================
    # LETTER GRADE + GPA + COMMENT
    # ==========================================

    if average >= 90:

        letter = "A"
        gpa = 4.0
        comment = "Excellent! Outstanding performance! 🌟"

    elif average >= 80:

        letter = "B"
        gpa = 3.0
        comment = "Great job! You are doing very well! 👏"

    elif average >= 70:

        letter = "C"
        gpa = 2.0
        comment = "Good work! Keep practicing to improve! 👍"

    elif average >= 60:

        letter = "D"
        gpa = 1.0
        comment = "You passed, but there is room for improvement. 📚"

    else:

        letter = "F"
        gpa = 0.0
        comment = "Keep trying! Study more and you can improve. 💪"


    # ==========================================
    # RESULTS
    # ==========================================

    st.success("✅ Grades calculated successfully!")

    st.subheader("📈 Your Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average",
            f"{average:.2f}%"
        )

    with col2:
        st.metric(
            "GPA",
            f"{gpa:.1f}"
        )

    with col3:
        st.metric(
            "Letter Grade",
            letter
        )

    # ==========================================
    # SUBJECT BREAKDOWN
    # ==========================================

    st.subheader("📋 Subject Breakdown")

    for sub, grade in grades.items():

        if grade >= 90:
            subject_letter = "A"

        elif grade >= 80:
            subject_letter = "B"

        elif grade >= 70:
            subject_letter = "C"

        elif grade >= 60:
            subject_letter = "D"

        else:
            subject_letter = "F"

        st.write(
            f"**{sub}:** {grade:.1f}% — {subject_letter}"
        )


# ==========================================
# QUIZ MASTER
# ==========================================

st.divider()

st.header("🧠 Quiz Master")

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False


number_of_questions = st.number_input(
    "How many questions do you want?",
    min_value=1,
    max_value=20,
    value=5,
    step=1,
    key="quiz_number"
)


if st.button("📝 Create Quiz", key="create_quiz"):

    st.session_state.quiz_questions = []

    for i in range(int(number_of_questions)):
        st.session_state.quiz_questions.append({
            "question": "",
            "options": ["", "", "", ""],
            "correct": 0
        })

    st.session_state.quiz_started = False
    st.session_state.quiz_submitted = False
    st.rerun()


if st.session_state.quiz_questions and not st.session_state.quiz_started:

    st.subheader("✏️ Create Your Questions")

    for i in range(len(st.session_state.quiz_questions)):

        st.markdown(f"### Question {i + 1}")

        st.session_state.quiz_questions[i]["question"] = st.text_input(
            "Question",
            key=f"question_{i}"
        )

        for j in range(4):

            st.session_state.quiz_questions[i]["options"][j] = st.text_input(
                f"Option {chr(65 + j)}",
                key=f"option_{i}_{j}"
            )

        st.session_state.quiz_questions[i]["correct"] = st.selectbox(
            "Correct Answer",
            [0, 1, 2, 3],
            format_func=lambda x: f"Option {chr(65 + x)}",
            key=f"correct_{i}"
        )

        st.divider()


    if st.button(
        "▶️ Start Quiz",
        key="start_quiz",
        use_container_width=True
    ):

        valid = True

        for q in st.session_state.quiz_questions:

            if not q["question"].strip():
                valid = False

            for option in q["options"]:
                if not option.strip():
                    valid = False

        if valid:
            st.session_state.quiz_started = True
            st.session_state.quiz_submitted = False
            st.rerun()

        else:
            st.warning(
                "⚠️ Please fill in every question and all four answer choices!"
            )


if st.session_state.quiz_questions and st.session_state.quiz_started:

    st.subheader("🎯 Take the Quiz")

    answers = []

    for i, q in enumerate(st.session_state.quiz_questions):

        st.markdown(f"### Question {i + 1}")

        st.write(q["question"])

        answer = st.radio(
            "Choose your answer",
            q["options"],
            key=f"take_quiz_{i}"
        )

        answers.append(answer)


    if st.button(
        "✅ Submit Quiz",
        key="submit_quiz",
        use_container_width=True
    ):

        score = 0

        for i, q in enumerate(st.session_state.quiz_questions):

            correct_answer = q["options"][q["correct"]]

            if answers[i] == correct_answer:
                score += 1

        st.session_state.quiz_score = score
        st.session_state.quiz_submitted = True


    if st.session_state.quiz_submitted:

        total = len(st.session_state.quiz_questions)

        st.success(
            f"🎉 Your Score: {st.session_state.quiz_score}/{total}"
        )

        percentage = (
            st.session_state.quiz_score / total
        ) * 100

        st.metric(
            "Percentage",
            f"{percentage:.1f}%"
        )

        if percentage == 100:

            st.balloons()

            st.success(
                "🌟 Perfect Score! Excellent work!"
            )

        elif percentage >= 80:

            st.success(
                "👏 Great job!"
            )

        elif percentage >= 60:

            st.info(
                "👍 Good effort! Keep practicing!"
            )

        else:

            st.warning(
                "📚 Keep studying and try again!"
            )


if st.button(
    "🔄 Create New Quiz",
    key="new_quiz",
    use_container_width=True
):

    st.session_state.quiz_questions = []
    st.session_state.quiz_started = False
    st.session_state.quiz_submitted = False
    st.rerun()


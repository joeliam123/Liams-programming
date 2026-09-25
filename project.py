import streamlit as st

st.set_page_config(
    page_title="My Profile & Calculator",
    page_icon="👤",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(255, 0, 128, 0.38), transparent 30%),
        radial-gradient(circle at 85% 15%, rgba(0, 200, 255, 0.38), transparent 30%),
        radial-gradient(circle at 80% 85%, rgba(130, 0, 255, 0.38), transparent 32%),
        radial-gradient(circle at 15% 85%, rgba(0, 255, 170, 0.28), transparent 30%),
        linear-gradient(120deg, #12002f, #001b45, #26003d, #003b3b);
    background-size: 180% 180%;
    animation: gradientMove 12s ease infinite;
    min-height: 100vh;
}

@keyframes gradientMove {
    0% {
        background-position: 0% 50%;
    }
    25% {
        background-position: 50% 100%;
    }
    50% {
        background-position: 100% 50%;
    }
    75% {
        background-position: 50% 0%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    background:
        radial-gradient(circle at 20% 30%, rgba(255,255,255,0.10) 0 2px, transparent 3px),
        radial-gradient(circle at 70% 70%, rgba(255,255,255,0.08) 0 2px, transparent 3px);
    background-size: 180px 180px, 240px 240px;
    animation: particles 18s linear infinite;
    z-index: 0;
}

@keyframes particles {
    from {
        transform: translateY(0);
    }
    to {
        transform: translateY(-180px);
    }
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    position: relative;
    z-index: 1;
    color: white;
}

h1, h2, h3 {
    text-shadow: 0 3px 15px rgba(0,0,0,0.25);
}

.calc-title {
    text-align: center;
    font-size: 28px;
    font-weight: 700;
    margin: 8px 0 14px 0;
    color: white;
    text-shadow: 0 0 18px rgba(0, 220, 255, 0.65);
}

.calc-display {
    background: rgba(10, 10, 20, 0.88);
    color: white;
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 24px;
    padding: 20px 18px;
    min-height: 105px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-end;
    overflow: hidden;
    margin: 0 auto 14px auto;
    max-width: 430px;
    box-shadow:
        0 12px 35px rgba(0,0,0,0.35),
        0 0 25px rgba(0,200,255,0.15);
}

.calc-expression {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 18px;
    color: #b8c5d9;
    min-height: 25px;
    overflow-wrap: anywhere;
    text-align: right;
}

.calc-result {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: clamp(38px, 10vw, 58px);
    font-weight: 300;
    line-height: 1.05;
    overflow-wrap: anywhere;
    text-align: right;
}

.calculator-grid {
    display: grid !important;
    grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
    gap: 8px !important;
    width: min(430px, 100%) !important;
    margin: 0 auto !important;
}

.calculator-grid > div {
    min-width: 0 !important;
    width: 100% !important;
}

.calculator-grid button {
    width: 100% !important;
    min-height: 62px !important;
    height: 62px !important;
    border-radius: 50% !important;
    font-size: 23px !important;
    padding: 0 !important;
    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease,
        filter 0.15s ease !important;
}

.calculator-grid button:hover {
    transform: translateY(-3px) scale(1.04);
    filter: brightness(1.18);
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}

@media (max-width: 600px) {
    .block-container {
        padding: 1rem 0.7rem 2rem 0.7rem;
    }

    .calc-title {
        font-size: 25px;
    }

    .calc-display {
        border-radius: 22px;
        padding: 18px 15px;
        margin-bottom: 10px;
        min-height: 95px;
    }

    .calculator-grid {
        grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
        gap: 6px !important;
    }

    .calculator-grid button {
        min-height: 58px !important;
        height: 58px !important;
        font-size: 21px !important;
    }
}

body, p, label, .stMarkdown, .stText, .stCaption,
.stTextInput label, .stNumberInput label, .stSelectbox label,
.stRadio label, [data-testid="stWidgetLabel"] {
    color: white !important;
}

h1, h2, h3, h4, h5, h6 {
    color: white !important;
}


body, p, label, .stMarkdown, .stText, .stCaption,
[data-testid="stWidgetLabel"] {
    color: white !important;
}

h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

[data-testid="stButton"] button,
[data-testid="stButton"] button p {
    color: white !important;
}

[data-testid="stHorizontalBlock"] {
    flex-wrap: nowrap !important;
    gap: 7px !important;
}

[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    min-width: 0 !important;
    flex: 1 1 0 !important;
}



[data-testid="stButton"] > button {
    background: #202030 !important;
    background-color: #202030 !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    color: #ffffff !important;
    border-radius: 50% !important;
    min-height: 58px !important;
    height: 58px !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    opacity: 1 !important;
    box-shadow: none !important;
}

[data-testid="stButton"] > button *,
[data-testid="stButton"] > button p,
[data-testid="stButton"] > button div,
[data-testid="stButton"] > button span {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    opacity: 1 !important;
    visibility: visible !important;
}

@media (max-width: 640px) {
    [data-testid="stButton"] > button {
        min-height: 52px !important;
        height: 52px !important;
        font-size: 19px !important;
    }
}
</style>
""", unsafe_allow_html=True)

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

st.divider()

st.markdown('<div class="calc-title">🧮 Calculator</div>', unsafe_allow_html=True)

if "display" not in st.session_state:
    st.session_state.display = "0"

if "expression" not in st.session_state:
    st.session_state.expression = ""

if "first_number" not in st.session_state:
    st.session_state.first_number = None

if "operator" not in st.session_state:
    st.session_state.operator = None

if "new_number" not in st.session_state:
    st.session_state.new_number = True

def press_number(number):
    if st.session_state.display == "Error":
        st.session_state.display = "0"
        st.session_state.expression = ""

    if st.session_state.new_number:
        st.session_state.display = str(number)
        st.session_state.new_number = False
    else:
        if st.session_state.display == "0":
            st.session_state.display = str(number)
        else:
            st.session_state.display += str(number)

    if st.session_state.operator:
        st.session_state.expression = (
            f"{format_number(st.session_state.first_number)} "
            f"{st.session_state.operator} "
            f"{st.session_state.display}"
        )
    else:
        st.session_state.expression = st.session_state.display

    st.rerun()

def format_number(number):
    if number is None:
        return ""
    if float(number).is_integer():
        return str(int(number))
    return str(round(number, 10))

def press_operator(operator):
    if st.session_state.display == "Error":
        return

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
            st.session_state.expression = "Cannot divide by zero"
            st.session_state.first_number = None
            st.session_state.operator = None
            st.session_state.new_number = True
            st.rerun()
            return
        result = first / second
    else:
        return

    expression = (
        f"{format_number(first)} {operator} {format_number(second)}"
    )

    st.session_state.display = format_number(result)
    st.session_state.expression = expression
    st.session_state.first_number = None
    st.session_state.operator = None
    st.session_state.new_number = True
    st.rerun()

def press_clear():
    st.session_state.display = "0"
    st.session_state.expression = ""
    st.session_state.first_number = None
    st.session_state.operator = None
    st.session_state.new_number = True
    st.rerun()

st.markdown(
    f"""
    <div class="calc-display">
        <div class="calc-expression">{st.session_state.expression}</div>
        <div class="calc-result">{st.session_state.display}</div>
    </div>
    """,
    unsafe_allow_html=True
)

def calc_button(label, key, action, column):
    with column:
        st.markdown('<div class="calc-button-wrap">', unsafe_allow_html=True)
        if st.button(label, key=key, use_container_width=True):
            action()
        st.markdown('</div>', unsafe_allow_html=True)


calculator_rows = [
    [
        ("7", "seven", lambda: press_number(7)),
        ("8", "eight", lambda: press_number(8)),
        ("9", "nine", lambda: press_number(9)),
        ("÷", "divide", lambda: press_operator("÷"))
    ],
    [
        ("4", "four", lambda: press_number(4)),
        ("5", "five", lambda: press_number(5)),
        ("6", "six", lambda: press_number(6)),
        ("×", "multiply", lambda: press_operator("×"))
    ],
    [
        ("1", "one", lambda: press_number(1)),
        ("2", "two", lambda: press_number(2)),
        ("3", "three", lambda: press_number(3)),
        ("-", "minus", lambda: press_operator("-"))
    ],
    [
        ("0", "zero", lambda: press_number(0)),
        ("C", "clear", press_clear),
        ("=", "equals", press_equals),
        ("+", "plus", lambda: press_operator("+"))
    ]
]

for row in calculator_rows:
    columns = st.columns(4, gap="small")
    for index, (label, key, action) in enumerate(row):
        calc_button(label, key, action, columns[index])


st.divider()

st.header("📊 Grade Calculator")
st.write("Enter your grades for each subject.")

if "subjects" not in st.session_state:
    st.session_state.subjects = ["Math", "English", "Science"]

st.subheader("➕ Add More Subjects")

new_subject = st.text_input(
    "Subject name",
    placeholder="Example: History",
    key="new_subject"
)

if st.button("Add Subject", key="add_subject"):
    if new_subject.strip():
        if new_subject.strip() not in st.session_state.subjects:
            st.session_state.subjects.append(new_subject.strip())
            st.rerun()
        else:
            st.warning("⚠️ That subject already exists!")
    else:
        st.warning("⚠️ Please enter a subject name.")

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

if st.button(
    "🧮 Calculate Grades",
    key="calculate_grades",
    use_container_width=True
):
    average = sum(grades.values()) / len(grades)

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

    st.success("✅ Grades calculated successfully!")
    st.subheader("📈 Your Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average", f"{average:.2f}%")
    with col2:
        st.metric("GPA", f"{gpa:.1f}")
    with col3:
        st.metric("Letter Grade", letter)

    st.info(f"💬 **Remark:** {comment}")

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

        st.write(f"**{sub}:** {grade:.1f}% — {subject_letter}")

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
            st.success("🌟 Perfect Score! Excellent work!")
        elif percentage >= 80:
            st.success("👏 Great job!")
        elif percentage >= 60:
            st.info("👍 Good effort! Keep practicing!")
        else:
            st.warning("📚 Keep studying and try again!")

if st.button(
    "🔄 Create New Quiz",
    key="new_quiz",
    use_container_width=True
):
    st.session_state.quiz_questions = []
    st.session_state.quiz_started = False
    st.session_state.quiz_submitted = False
    st.rerun()

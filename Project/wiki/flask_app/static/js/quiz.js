
const questionElement = document.getElementById("question");
const choicesElement = document.getElementById("choices");
const submitButton = document.getElementById("submit");
const resultContainer = document.getElementById("result");

const questions = [
    {
        q: "How would your friends best describe you?",
        choices: ["Adventurous", "Goofy", "Selfish", "Caring"],
    },
    {
        q: "How do you like spending your free time?",
        choices: ["Traveling", "Hanging with Friends", "On your phone", "Drinking"],
    },
    {
        q: "What is your preferred method of traveling?",
        choices: ["Portal Gun", "Spaceship", "Car", "None"],
    },
    {
        q: "How do you handle stressful situations?",
        choices: ["Stay calm and composed", "Get anxious but try to find a solution", "Panic and make things worse", "Avoid or ignore them"],
    },
];

let currQuestion = 0;
let score = 0;

function showQuestion() {
    const question = questions[currQuestion];
    questionElement.textContent = question.q;

    choicesElement.innerHTML = "";
    question.choices.forEach((choice, index) => {
        const choiceElement = document.createElement("li");
        choiceElement.innerHTML = `<input type="radio" name="answer" value="${index}"> ${choice}`;
        choicesElement.appendChild(choiceElement);
    });
}

function showScore() {
    const selected = document.querySelector('input[name="answer"]:checked');
    if (selected) {
        score += parseInt(selected.value);
        currQuestion++;
        if (currQuestion < questions.length) {
            showQuestion();
        } else {
            showResult();
        }
    } else {
        alert("Please select an answer.");
    }
}

function showResult() {
    submitButton.disabled = true;
    let result = "";

    if (score >= 0 && score <= 3) {
        result = "You are most like Rick!";
    } else if (score >= 4 && score <= 6) {
        result = "You are most like Morty!";
    } else if (score >= 7 && score <= 9) {
        result = "You are most like Summer!";
    } else if (score >= 10) {
        result = "You are most like Beth!";
    }

    resultContainer.textContent = result;
}


submitButton.addEventListener("click", showScore);

showQuestion();

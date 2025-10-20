const API_URL = "http://127.0.0.1:8000";

async function simplifyText() {
    const text = document.getElementById("inputText").value;
    console.log("Sending text:", text);
    const res = await fetch(`${API_URL}/simplify_text`, {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({text})
    });
    console.log("Response status:", res.status);
    const data = await res.json();
    console.log("Data received:", data);
    document.getElementById("summary").innerText = data.summary;
}

async function analyzeMood() {
    const text = document.getElementById("inputText").value;
    console.log("Analyzing mood for:", text);
    const res = await fetch(`${API_URL}/detect_mood`, {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({text})
    });
    const data = await res.json();
    const manual = document.getElementById("manualMood").value;
    const moodResult = manual || data.mood;
    console.log("Mood result:", moodResult);
    document.getElementById("mood").innerText = moodResult;
}

async function getBooks() {
    const mood = document.getElementById("manualMood").value || document.getElementById("mood").innerText;
    console.log("Getting books for mood:", mood);
    const res = await fetch(`${API_URL}/recommend_books`, {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({mood})
    });
    const data = await res.json();
    console.log("Books received:", data);
    const container = document.getElementById("books");
    container.innerHTML = "";
    data.forEach(book => {
        container.innerHTML += `<div style="margin-bottom:10px;"><b>${book.Title}</b> by ${book.Author} - <i>${book.Mood}</i></div>`;
    });
}

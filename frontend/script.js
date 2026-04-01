async function analyze() {
    const review = document.getElementById("review").value;
    const resultDiv = document.getElementById("result");

    if (review.trim() === "") {
        resultDiv.innerText = "⚠️ Please enter a review!";
        resultDiv.className = "result";
        return;
    }

    resultDiv.innerText = "⏳ Analyzing...";
    resultDiv.className = "result";

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ review: review })
        });

        const data = await response.json();

        if (data.prediction.includes("Positive")) {
            resultDiv.innerText = "😊 Positive Review";
            resultDiv.className = "result positive";
        } else {
            resultDiv.innerText = "😡 Negative Review";
            resultDiv.className = "result negative";
        }

    } catch (error) {
        resultDiv.innerText = "❌ Error connecting to server";
    }
}
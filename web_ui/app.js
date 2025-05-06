document.addEventListener("DOMContentLoaded", () => {
  fetchTemperature();
  fetchLogs();

  const verifyForm = document.getElementById("verify-form");
  verifyForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const dataInput = document.getElementById("data-input").value;

    if (!dataInput) {
      alert("Please enter data to verify.");
      return;
    }

    const response = await fetch("/verify", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ data: dataInput })
    });

    const result = await response.json();

    const resultDiv = document.getElementById("verify-result");
    resultDiv.textContent = result.match
      ? "✅ Data is verified and exists on blockchain."
      : "❌ Data not found or has been tampered.";
  });
});

async function fetchTemperature() {
  try {
    const res = await fetch("/temp");
    const data = await res.json();
    document.getElementById("temperature").textContent = `${data.temp} °C`;
  } catch (error) {
    console.error("Error fetching temperature:", error);
  }
}

async function fetchLogs() {
  try {
    const res = await fetch("/logs");
    const logs = await res.json();
    const logList = document.getElementById("log-list");
    logList.innerHTML = "";

    logs.forEach((log, index) => {
      const li = document.createElement("li");
      li.textContent = `Log #${index + 1} - Hash: ${log.hash} - Timestamp: ${log.timestamp}`;
      logList.appendChild(li);
    });
  } catch (error) {
    console.error("Error fetching logs:", error);
  }
}

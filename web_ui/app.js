// Fetch live temperature
async function fetchTemp() {
    const res = await fetch("http://localhost:5000/temp");
    const data = await res.json();
    document.getElementById("temperature").innerText = `${data.temp} °C`;
  }
  
  // Fetch blockchain logs
  async function fetchLogs() {
    const res = await fetch("http://localhost:5000/logs");
    const logs = await res.json();
    const tbody = document.getElementById("logs-table");
    tbody.innerHTML = "";
    logs.forEach(log => {
      const row = `<tr><td>${log.timestamp}</td><td>${log.hash}</td></tr>`;
      tbody.innerHTML += row;
    });
  }
  
  // Tamper check
  async function verifyData() {
    const input = document.getElementById("check-input").value;
    const res = await fetch("http://localhost:5000/verify", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ data: input })
    });
    const result = await res.json();
    const msg = result.match ? "✅ Data is verified and untampered." : "❌ Data does NOT match any blockchain record!";
    document.getElementById("check-result").innerText = msg;
  }
  
  // Initial load
  fetchTemp();
  fetchLogs();
  setInterval(fetchTemp, 5000); // refresh temperature every 5s
  
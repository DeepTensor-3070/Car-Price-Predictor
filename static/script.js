// Auto-fill YEAR dropdown from 2000 to 2024
const yearSelect = document.getElementById("year");
for (let y = 2000; y <= 2024; y++) {
    let opt = document.createElement("option");
    opt.value = y;
    opt.textContent = y;
    yearSelect.appendChild(opt);
}

let chartObj = null;

async function predictPrice() {
    const payload = {
        car_name: document.getElementById("car_name").value,
        car_type: document.getElementById("car_type").value,
        year: document.getElementById("year").value,
        kms: document.getElementById("kms").value,
        fuel_type: document.getElementById("fuel_type").value
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    const result = await response.json();

    // Show price
    document.getElementById("price").innerHTML =
        "₹ " + Number(result.price).toLocaleString();

    // Show result card
    document.getElementById("resultCard").classList.remove("hidden");

    // Draw graph
    const ctx = document.getElementById("priceChart").getContext("2d");

    if (chartObj) chartObj.destroy();

    chartObj = new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Market Low", "Market Avg", "Predicted"],
            datasets: [{
                data: [result.market_low, result.market_avg, result.price],
                borderWidth: 2
            }]
        },
        options: {
            plugins: { legend: { display: false } }
        }
    });
}

document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('graficoImpacto');
    
    if (ctx) {
        new Chart(ctx, {
            type: 'bar', 
            data: {
                labels: window.graficoLabels, 
                datasets: [{
                    label: 'Quantidade de Intenções de Doação',
                    data: window.graficoValores, 
                    backgroundColor: ['#005953', '#001f3f', '#0088cc'], 
                    borderRadius: 6
                }]
            },
          options: {
                responsive: true,
                maintainAspectRatio: false, 
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: { 
                        beginAtZero: true, 
                        ticks: { stepSize: 1 },
                        suggestedMax: 10
                    }
                }
            }
        });
    }
});
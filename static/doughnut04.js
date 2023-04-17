function Doughnut()
{
    var canvas = document.getElementById('doughnut4');
    canvas.width=180;
    canvas.height=110;
            // Set up the chart data
            var chartData = {
                labels: ['Label 1', 'Label 2'],
                datasets: [{
                    label: 'My Dataset',
                    position: 'right',
                    data: [45, 30],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                         
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                    ],
                    borderWidth: 1
                }]
            };
    
            // Create the chart
            // var ctx = document.getElementById('doughnut4').getContext('2d');
            var myChart = new Chart(canvas, {
                type: 'doughnut', 
                data: chartData,
                options: {
                    responsive: false,
                    position:'right',
                    legend: {
                        fontColor: '#333'
                         
                    },
                    cutoutPercentage: 60
                }
            });
     
}
Doughnut();
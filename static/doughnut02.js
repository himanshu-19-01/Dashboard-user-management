function createchart(){
  fetch("static//doughnut_data.json")
  .then(response => response.json())
  .then(data => {
    // Do something with the JSON data
    console.log(data);
    var val1 =  data[0].Success_per;
    var val2= data[0].Refund_per;
    var val3=data[0].Fail_per;
    // Set up the chart data
    var chartData = {
        labels: ['Success', 'Refund', 'Fail'],
        datasets: [{
            label: 'My Dataset',
            innerRadius: "35%",
            data: [val1, val2, val3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)',
                'rgba(255, 206, 86, 0.6)'
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    };
    
    // Create the chart
    var ctx = document.getElementById('myChart1').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: chartData,
        options: {
            plugins: {
              datalabels: {
                display: true,
                backgroundColor: '#ccc',
                borderRadius: 3,
                font: {
                  color: 'red',
                  weight: 'bold',
                },
              },
              doughnutlabel: {
                labels: [
                  {
                    text: '550',
                    font: {
                      size: 20,
                      weight: 'bold',
                    },
                  },
                  {
                    text: 'total',
                  },
                ],
              },
            },
          },
    });
    
        
    
    
      })}
    createchart();
    
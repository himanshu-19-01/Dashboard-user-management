function createchart(){
    fetch("static//doughnut_data.json")
  .then(response => response.json())
  .then(data => {
    // Do something with the JSON data
    console.log(data);
    var val1 =  data[2].Success_per3;
    var val2= data[2].Pending_per;
    // Set up the chart data
    var chartData = {
        labels: ['Success', 'Pending',],
        datasets: [{
            label: 'My Dataset',
            data: [val1,val2],
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)'
               // 'rgba(255, 206, 86, 0.6)'
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
                //'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    };
    
    // Create the chart
    var ctx = document.getElementById('myChart2').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: chartData,
        options: {
            responsive: false,
            legend: {
                position:'right',
                labels: {
                    fontColor: '#333'
                }
            }
        }
    });
    
        
    
    
    })}
    createchart();
    
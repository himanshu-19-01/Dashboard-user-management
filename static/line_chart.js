function generateHalfLineChart() {
  fetch("static//doughnut_data.json")
  .then(response => response.json())
  .then(data => {
    // Do something with the JSON data
    console.log(data);
    var val1 =  data[3].list[0];
    var val2= data[3].list[1];
    var val3=data[3].list[2];
    var val4= data[3].list[3];
    var val5=data[3].list[4];
    var canvas = document.getElementById('myHalfLineChart1');
    canvas.width=400;
    canvas.height=100;
      var data = {
        labels: ["1", "2", "3", "4", "5"],
        datasets: [
          {
            label: "Dataset 1",
            data: [val1, val2, val3, val4, val5],
            fill: false,
            borderColor: "#FF6384",
            tension: 0.4
          }
        ]
      };
    
      var options = {
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
          xAxes: [{
            display: false
          }],
          yAxes: [{
            display: true,
            ticks: {
              suggestedMin: 0,
              suggestedMax: 25
            }
          }]
        }
      };
    
      // var ctx = document.getElementById("myHalfLineChart1").getContext("2d");
      var myHalfLineChart = new Chart(canvas, {
        type: 'line',
        data: data,
        options: options
      });
    })}
  generateHalfLineChart();
    
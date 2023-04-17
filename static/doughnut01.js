function createchart(){
  fetch("static//doughnut_data.json")
  .then(response => response.json())
  .then(data => {
    // Do something with the JSON data
    console.log(data);
    var val1 =  data[1].Success_count1;
    var val2= data[1].invalid_count;
    var val3=data[1].Not_Sufficient;
    // Set up the chart data
    var chartData = {
        labels: ['Success', 'Invalid', 'Funds'],
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
    const counter={
        id:'counter',
        beforeDraw(chart,args,options){
            
            const{ctx,chartArea:{top,right,bottom,left,width,height}}=chart;
            ctx.save();
            ctx.font='50px'
            ctx.textAlign='center';
            ctx.fillStyle='blue';
            ctx.fillText('35%',width/2,top+(height/2));
        }
    };
    // Create the chart
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: chartData,
        // plugins:[counter],
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
    
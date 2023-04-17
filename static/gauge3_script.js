fetch("static//variables.json")
  .then(response => response.json())
  .then(data => {
    // Do something with the JSON data
    console.log(data);
    var number =  data[0].Exec_Time_url3
    const myFloat = parseFloat(number);
    const value = myFloat.toFixed(2);
    if (value<=10)
    {
      var data = {
        datasets: [{
          data: [value,30-value],
          backgroundColor: ['green','#ccc'],
          borderWidth: 1,
          
        }]
      };
    }
    else if (value>10 && value<=25)
    {
      var data = {
        datasets: [{
          data: [value,30-value],
          backgroundColor: ['orange','#ccc'],
          borderWidth: 1,
          
        }]
      }; 
    }
    else {
    var data = {
      datasets: [{
        data: [value,30-value],
        backgroundColor: ['red','#ccc'],
        borderWidth: 1,
        
      }]
    };
    }
    

var options = {
  cutoutPercentage: 70,
  rotation: 270,
  circumference: 180,
  animation: {
    animateRotate: true,
    animateScale: true
  },
  legend: {
    display: false
  },
  scale: {
    ticks: {
      display: false,
      min: 0,
      max: 30
    },
    pointLabels: {
      fontSize: 15
    }
  },
  tooltips: {
    enabled: false
  }
};
const gaugevalue3={
  id:'gaugevalue3',
  afterDatasetDraw(chart,args,options){
    const{ctx,config,data,chartArea:{top,bottom,left,right,width,height}}=chart;
    ctx.save();
    ctx.font='60px';
    //ctx.fillStyle="#444";
    ctx.fillText(data.datasets[0].data[0],width/2,bottom-13);
    ctx.textAlign='center';
    ctx.fillStyle='white';
  }
};
var ctx = document.getElementById("myGaugeChart2").getContext("2d");
var myGaugeChart = new Chart(ctx, {
  type: 'doughnut',
  plugins:[gaugevalue3],
  data: data,
  options: options
});

  })
  .catch(error => console.error(error));

 

 

 
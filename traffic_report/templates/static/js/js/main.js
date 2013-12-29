/* Counting Cars Variables */

//Data Array
var counting_cars_array = [];
var counting_cars_data_array = [];
var currentDataLength;
var dataValue = 0;
var currentDate;
var carGraph;
var updateInterval = 5000;

//Container
var countingCarsGraph = $("#counting_car_graph");

//Graph options
var countingCarsOptions = {
		grid: {
			show: true,
		    aboveData: true,
		    color: "#3f3f3f" ,
		    labelMargin: 5,
		    axisMargin: 0, 
		    borderWidth: 0,
		    borderColor:null,
		    minBorderMargin: 5 ,
		    clickable: false, 
		    hoverable: false,
		    autoHighlight: true,
		    mouseActiveRadius: 20
		},
        series: {
        	grow: {
        		active: false,
        		stepMode: "linear",
        		steps: 50,
        		stepDelay: true
        	},
            lines: {
        		show: true,
        		fill: true,
        		lineWidth: 4,
        		steps: false
            	},
            points: {
            	show:true,
            	radius: 5,
            	symbol: "circle",
            	fill: true,
            	borderColor: "#fff"
            }
        },
        legend: { 
        	position: "ne", 
        	margin: [0,-25], 
        	noColumns: 0,
        	labelBoxBorderColor: null,
        	labelFormatter: function(label, series) {
			    return label+'&nbsp;&nbsp;';
			 }
    	},
        yaxis: { min: 0, tickDecimals: 0 },
        //xaxis: {min:0, tickDecimals: 0},
        xaxis: {mode: "time", timeformat: "%H:%M:%S"},
        colors: ['#88bbc8'],
        shadowSize:1
    };

/* Matrículas Chart Variables */

//Data Array
var matriculas_array = [ [1, 1] ]; // Using hardcoded data atm, because it will only return one matricula
var matriculas_data_array = [];

//Container
var matriculasGraph = $("#matriculas_graph");

//Graph options
var matriculasOptions = {
		grid: {
			show: true,
		    aboveData: true,
		    color: "#3f3f3f" ,
		    labelMargin: 5,
		    axisMargin: 0, 
		    borderWidth: 1,
		    borderColor:true,
		    minBorderMargin: 5 ,
		    clickable: false, 
		    hoverable: false,
		    autoHighlight: false			    			
		},
        series: {
            bars: {
            	show: true,
            	barWidth: 0.6,
            	align: "center"
            }
        },
        legend: { 
        	position: "ne", 
        	margin: [0,-25], 
        	noColumns: 0,
        	labelBoxBorderColor: null,
        	labelFormatter: function(label, series) {
			    return label+'&nbsp;&nbsp;';
			 }
    	},
        yaxis: { min: 0, tickDecimals: 0 },
        xaxis: { ticks: [], autoscaleMargin: 0.6 },
        colors: ['#ed7a53'],
        shadowSize:1
    };  

/* Matrículas Chart Variables */

//Data Array
var people_array = [ [0,0], [1,1], [2,2], [3,3], [4,4], [5,5] ]; // Using hardcoded data atm, because it will only return one matricula
var people_data_array = [];

//Container
var peopleGraph = $("#people_graph");

//Graph options
var peopleOptions = {
		grid: {
			show: true,
		    aboveData: true,
		    color: "#3f3f3f" ,
		    labelMargin: 5,
		    axisMargin: 0, 
		    borderWidth: 0,
		    borderColor:null,
		    minBorderMargin: 5 ,
		    clickable: false, 
		    hoverable: false,
		    autoHighlight: true,
		    mouseActiveRadius: 20
		},
        series: {
        	grow: {
        		active: false,
        		stepMode: "linear",
        		steps: 50,
        		stepDelay: true
        	},
            lines: {
        		show: true,
        		fill: true,
        		lineWidth: 4,
        		steps: false
            	},
            points: {
            	show:true,
            	radius: 5,
            	symbol: "circle",
            	fill: true,
            	borderColor: "#fff"
            }
        },
        legend: { 
        	position: "ne", 
        	margin: [0,-25], 
        	noColumns: 0,
        	labelBoxBorderColor: null,
        	labelFormatter: function(label, series) {
			    return label+'&nbsp;&nbsp;';
			 }
    	},
        yaxis: { min: 0, tickDecimals: 0 },
        xaxis: {min:0, tickDecimals: 0},
        colors: ['#6caf2b'],
        shadowSize:1
    };

// Document ready
$(function(){

	$(".icon-folder-open").filestyle({classButton: "btn btn-primary"});

	/* Initializing Video */

	var myPlayer = videojs("counting_car_video", { "controls": false, "autoplay": false, "preload": "auto"}, function(){
	});

	myPlayer.src([ { type: "video/webm", src: "/static/video1.webm" },{ type: "video/mp4", src: "/static/video1.mp4" }]);
	
	var myPlayerSpectrum = videojs("counting_car_video_spectrum", { "controls": false, "autoplay": false, "preload": "auto"}, function(){
	});

	myPlayerSpectrum.src([ { type: "video/webm", src: "/static/video1.webm" },{ type: "video/mp4", src: "/static/video1.mp4" }]);

	$("#start-count").on("click", function(){

		if($(this).hasClass("paused")){
			myPlayer.play();
			myPlayerSpectrum.play();
			$(this).removeClass("paused");
			$(this).addClass("playing");

			$(".vjs-default-skin.vjs-controls-disabled .vjs-control-bar").attr("style", "display: block !important;");
		} else {
			myPlayer.pause();
			myPlayerSpectrum.pause();
			$(this).removeClass("playing");
			$(this).addClass("paused");
			$(".vjs-default-skin.vjs-controls-disabled .vjs-control-bar").attr("style", "display: none !important;");
		}
		
	});

	/*****************************
		Counting Cars Ajax Call
	*****************************/

	$.getJSON("json/cars2.json", function(data){

		$(".counting-car-title").html(data.array[0].time.split(",")[0]);
		//Removing Loading Div
		$("#counting_car_graph_container").find(".loading").remove();
		// Using the cars_quantity field to make a loop in order to create a understandable dataset for flotCharts
		/*for ( i = 0; i <= data.cars_quantity; i++ ){

			//Clearing in each interaction the data array
			counting_cars_data_array = [];

			//Adding two times the same value in order to create the correct y, x axis
			counting_cars_data_array.push(i);
			counting_cars_data_array.push(i);

			//Adding the resulting array to the general one, to be used as the dataset for the chart
			counting_cars_array.push(counting_cars_data_array)
		}

		//Generating the chart
		$.plot(countingCarsGraph, [ 

			{
				label: "Total: "+data.cars_quantity, 
				data: counting_cars_array,
				lines: {fillColor: "#f2f7f9"},
				points: {fillColor: "#88bbc8"}
			}

		], countingCarsOptions);

		//Changing the chart container title to reflect the start / end time for the dataset
		$("#car-couting-title").html("Conteo De Carros  <span>Fecha: "+ data.start_date + " - "+ data.end_date+"</span>");*/
		
		for(var i = 0; i < data.array.length; i++){
			if (data.array[i].quantity != 0){

				currentData = [];
				if ((i > 0) && (data.array[i-1].time == data.array[i].time)){
					counting_cars_array[counting_cars_array.length-1][1] += data.array[i].quantity;
				} else {
					currentDate = Date.parse(data.array[i].time);
					currentData.push( currentDate );
					currentData.push( data.array[i].quantity );
					dataValue = dataValue + data.array[i].quantity;
					counting_cars_array.push(currentData);
				}

			} else {
				 currentData = [];
				 currentData.push( Date.parse(data.array[i].time) );
				 currentData.push( 0 );
				 counting_cars_array.push(currentData);
			}
		}

		var lastTime = counting_cars_array[counting_cars_array.length-1][0] - updateInterval;
		for(var j = counting_cars_array.length -1; j >= 0; j-- ){
			if(counting_cars_array[j][0] <= lastTime ){
				counting_cars_array.splice(0,j+1);
				break;
			}
		}

		carGraph = $.plot(countingCarsGraph, [ 

			{
				label: "Total: "+dataValue, 
				data: counting_cars_array,
				lines: {fillColor: "#f2f7f9"},
				points: {fillColor: "#88bbc8"}
			}

		], countingCarsOptions);

		updateCars();

	});

	

	/*****************************
		   Matrículas Ajax Call
	*****************************/

	$.getJSON("json/ocr.json", function(data){ 

		//Removing Loading Div
		$("#matriculas_graph_container").find(".loading").remove();

		//Generating the chart
		$.plot(matriculasGraph, [ 
			{
				label: "Total: 1", 
				data: matriculas_array
			} 
		], matriculasOptions );

		//Filling the Matriculas Table with the matricula returned
		$("<tr/>",{
			html: "<td> 1 </td>"
					+"<td>"+ data.matricula +"</td>"
					+"<td>"+ data.date +"</td>"
		}).appendTo("#matriculasTable").find("tbody");

	});

	/*****************************
		   People Ajax Call
	*****************************/

	$.getJSON("json/people.json", function(data){ 
		//Removing Loading Div
		$("#people_graph_container").find(".loading").remove();

		//Filling the Matriculas Table with the matricula returned
		/*$("<tr/>",{
			html: "<td> 1 </td>"
					+"<td>"+ data.quantity +"</td>"
					+"<td>"+ data.quantity +"</td>"
		}).appendTo("#peopleTable").find("tbody");
		*/

		//Generating the chart
		$.plot(peopleGraph, [ 

			{
				label: "Total: 5", 
				data: people_array,
				points: {fillColor: "#6caf2b"}
			}

		], peopleOptions);

	});

	        	
});

function updateCars(){	

	setTimeout(updateCars, updateInterval);
}

function getData(){
	$.getJSON("json/cars2.json", function(data){

		//Removing Loading Div
		$("#counting_car_graph_container").find(".loading").remove();
		// Using the cars_quantity field to make a loop in order to create a understandable dataset for flotCharts
		/*for ( i = 0; i <= data.cars_quantity; i++ ){

			//Clearing in each interaction the data array
			counting_cars_data_array = [];

			//Adding two times the same value in order to create the correct y, x axis
			counting_cars_data_array.push(i);
			counting_cars_data_array.push(i);

			//Adding the resulting array to the general one, to be used as the dataset for the chart
			counting_cars_array.push(counting_cars_data_array)
		}

		//Generating the chart
		$.plot(countingCarsGraph, [ 

			{
				label: "Total: "+data.cars_quantity, 
				data: counting_cars_array,
				lines: {fillColor: "#f2f7f9"},
				points: {fillColor: "#88bbc8"}
			}

		], countingCarsOptions);

		//Changing the chart container title to reflect the start / end time for the dataset
		$("#car-couting-title").html("Conteo De Carros  <span>Fecha: "+ data.start_date + " - "+ data.end_date+"</span>");*/
		
		for(var i = 0; i < data.array.length; i++){
			if (data.array[i].quantity != 0){

				currentData = [];
				if ((i > 0) && (data.array[i-1].time == data.array[i].time)){
					counting_cars_array[counting_cars_array.length-1][1] += data.array[i].quantity;
				} else {
					currentDate = Date.parse(data.array[i].time);
					currentData.push( currentDate );
					currentData.push( data.array[i].quantity );
					dataValue = dataValue + data.array[i].quantity;
					counting_cars_array.push(currentData);
				}

			} else {
				 currentData = [];
				 currentData.push( Date.parse(data.array[i].time) );
				 currentData.push( 0 );
				 counting_cars_array.push(currentData);
			}
		}

		var lastTime = counting_cars_array[counting_cars_array.length-1][0] - updateInterval;
		for(var j = counting_cars_array.length -1; j >= 0; j-- ){
			if(counting_cars_array[j][0] <= lastTime ){
				counting_cars_array.splice(0,j+1);
				break;
			}
		}

		carGraph = $.plot(countingCarsGraph, [ 

			{
				label: "Total: "+dataValue, 
				data: counting_cars_array,
				lines: {fillColor: "#f2f7f9"},
				points: {fillColor: "#88bbc8"}
			}

		], countingCarsOptions);

		carGraph.setData(counting_cars_array);
		carGraph.draw();
	});
}	

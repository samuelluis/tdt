/* Counting Cars Variables */

//Data Array
var counting_cars_array = [];
var counting_cars_right = [];
var counting_cars_left = [];
var counting_cars_top = [];
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
        		lineWidth: 3,
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
        xaxis: {mode: "categories", tickLength: 0},
        //xaxis: {mode: "time", timeformat: "%H:%M:%S"},
        colors: ['#88bbc8',"#dd8852","#a9c888","#b3a69e"],
        shadowSize:1
    };

/* Matrículas Chart Variables */

//Data Array
var matriculas_array = []; // Using hardcoded data atm, because it will only return one matricula
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
var videoInterval = 0; 
var spectrumPlayer;
var currentTime = 1;
var cars;
var totalCount = 0;
var leftCount = 0;
var rightCount = 0;
var topCount = 0;

function drawInterval(){
	if(spectrumPlayer.paused()){
		clearInterval(videoInterval);
	}
	else{
		if(currentTime!=parseInt(spectrumPlayer.currentTime())){
			counting_cars_array.splice(0,1);
			counting_cars_right.splice(0,1);
			counting_cars_left.splice(0,1);
			counting_cars_top.splice(0,1);
			if(cars.array[currentTime]==undefined){
				counting_cars_array.push([currentTime+"s",0]);
				counting_cars_right.push([currentTime+"s",0]);
				counting_cars_left.push([currentTime+"s",0]);
				counting_cars_top.push([currentTime+"s",0]);
			}
			else{
				current = cars.array[currentTime];
				totalCount += (current.left + current.right + current.top);
				rightCount += current.right;
				leftCount += current.left;
				topCount += current.top;
				counting_cars_array.push([currentTime+"s", (current.left + current.right + current.top)]);
				counting_cars_right.push([currentTime+"s", current.right]);
				counting_cars_left.push([currentTime+"s", current.left]);
				counting_cars_top.push([currentTime+"s", current.top]);
			}
			carGraph = $.plot(countingCarsGraph, [ 
				{
					label: "Total: "+totalCount,
					data: counting_cars_array,
					lines: {fillColor: "#f2f7f9"},
					points: {fillColor: "#88bbc8"}
				}, 
				{
					label: "Right: "+rightCount,
					data: counting_cars_right,
					//lines: {fillColor: "#a9c888"},
					//points: {fillColor: "#88bbc8"}
				}, 
				{
					label: "Left: "+leftCount,
					data: counting_cars_left,
					//lines: {fillColor: "#c8aa88"},
					//points: {fillColor: "#88bbc8"}
				}, 
				{
					label: "Top: "+topCount,
					data: counting_cars_top,
					//lines: {fillColor: "#c888a1"},
					//points: {fillColor: "#88bbc8"}
				}
			], countingCarsOptions);
			currentTime = parseInt(spectrumPlayer.currentTime());
		}
	}
}

$(function(){

	$(".icon-folder-open").filestyle({classButton: "btn btn-primary"});

	/* Initializing Video */

	var myPlayer = videojs("counting_car_video", { "controls": false, "autoplay": false, "preload": "auto"}, function(){
	});

	myPlayer.src([{ type: "video/mp4", src: "/static/media/cars.mp4" }]);
	
	spectrumPlayer = videojs("counting_car_video_spectrum", { "controls": false, "autoplay": false, "preload": "auto"}, function(){
	});

	spectrumPlayer.src([{ type: "video/mp4", src: "/static/media/spectrum.mp4" }]);

	$("#start-count").on("click", function(){

		if($(this).hasClass("paused")){
			myPlayer.play();
			spectrumPlayer.play();
			$(this).removeClass("paused");
			$(this).addClass("playing");
			videoInterval = setInterval(drawInterval, 100);
			$(".vjs-default-skin.vjs-controls-disabled .vjs-control-bar").attr("style", "display: block !important;");
		} else {
			myPlayer.pause();
			spectrumPlayer.pause();
			$(this).removeClass("playing");
			$(this).addClass("paused");
			clearInterval(videoInterval);
			$(".vjs-default-skin.vjs-controls-disabled .vjs-control-bar").attr("style", "display: none !important;");
		}
		
	});


	/*****************************
		Counting Cars Ajax Call
	*****************************/

	$.getJSON("/static/json/cars.json", function(data){
		cars = data;
		$("#counting_car_graph_container").find(".loading").remove();
		for(var i = 0; i<10; i++){
			counting_cars_array.push(["0s",0]);
			counting_cars_right.push(["0s",0]);
			counting_cars_left.push(["0s",0]);
			counting_cars_top.push(["0s",0]);
		}
		/*for(var i = 0; i < data.array.length; i++){
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
		}*/

		carGraph = $.plot(countingCarsGraph, [ 

			{
				label: "Total: 0",
				data: counting_cars_array,
				lines: {fillColor: "#f2f7f9"},
				points: {fillColor: "#88bbc8"}
			}

		], countingCarsOptions);

		//updateCars();

	});
	

	/*****************************
		   Matrículas Ajax Call
	*****************************/

	$.getJSON("/static/json/ocr.json", function(data){ 

		//Removing Loading Div
		$("#matriculas_graph_container").find(".loading").remove();

		//Loop through the Matriculas array
		for(var i = 0; i < data.registration_tags.length; i++) {

			//Filling the Matriculas Table with the matricula returned
			$("<tr/>",{
				html: "<td>"+(i+1)+"</td>"
						+"<td>"+ data.registration_tags[i].matricula +"</td>"
						+"<td>"+ data.registration_tags[i].date +" "+ data.registration_tags[i].hour +"</td>"
						+"<td><a href='"+data.registration_tags[i].img_url+"' rel='prettyPhoto[ocr_gallery]'><img class='ocr_thumb' src='"+ data.registration_tags[i].img_url +"' alt='"+data.registration_tags[i].matricula+"'/></a></td>"
			}).appendTo("#matriculasTable").find("tbody");

		}

		$("a[rel^='prettyPhoto']").prettyPhoto({});
		http://www.no-margin-for-errors.com/projects/prettyphoto-jquery-lightbox-clone/?utm_source=INK&utm_medium=copy&utm_campaign=share&
		//Generating the chart
		$.plot(matriculasGraph, [ 
			{
				label: "Total: "+data.registration_tags.length, 
				data: [ [data.registration_tags.length, data.registration_tags.length ] ]
			} 
		], matriculasOptions );

	});

	/*****************************
		   People Ajax Call
	*****************************/

	$.getJSON("/static/json/people.json", function(data){ 
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
	$.getJSON("/static/json/cars2.json", function(data){

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

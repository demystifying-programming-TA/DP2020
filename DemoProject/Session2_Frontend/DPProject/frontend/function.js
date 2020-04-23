// JavaScript functions

// DrawGraph
// ---------------------

// Initialize the Google Charts library
google.charts.load('current', {packages: ['corechart', 'bar']});

function DrawGraph(country, infection, death) {

  // Generate and format the data
  var data = google.visualization.arrayToDataTable([
    ['Country', 'Infections', 'Deaths'],
    [country, infection, death]
  ]);

  // Customize the graph
  var options = {
    colors: ['#b0120a', '#ffab91'],
    chartArea: {width: '50%'},
    hAxis: {
      title: 'Number of infections and deaths'
    }
  };

  // Generate the graph
  var chart = new google.visualization.BarChart(document.getElementById('chart'));

  // Display the graph
  chart.draw(data, options);

}

// InitializeGraph
// ---------------------
function InitializeGraph() {

    // Make a client-side API call to obtain the user's location
    $.getJSON("http://ip-api.com/json", function (data, status) {

     // Extract the user's longitude and latitude from the data that the API returns
     longitude = data.lon;
     latitude  = data.lat;

     // Log the longitude and latitude to the console
     console.log("Longitude: " + longitude)
     console.log("Latitude: " + latitude)

     // Update the interface the user sees with their location
     document.getElementById("location").innerHTML = "Your location:<br> Latitude: " + latitude + "<br>Longitude: " + longitude;

     // Draw the graph
     // ** Note: Data is hard-coded > next step: Replace hard-coded data with an API call to the server, i.e., backend 
     // ** API call specification: Send to server: Longitude, latitude / Receive from server: Corresponding country, # of infections/deaths in that country
     DrawGraph("United States",852000, 43000);

    });
}





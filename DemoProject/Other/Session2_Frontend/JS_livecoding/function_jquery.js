// Defining functions
// ---------

// InitializeGraph
function InitializeGraph() {

  // Make a client-side API call to obtain the user's location
  $.getJSON("http://ip-api.com/json", function (data, status) {

  // Inspect the data returned from the API
  console.log(data)

  // Extract the user's longitude and latitude from the data that the API returns
  user_longitude = data.lon;
  user_latitude  = data.lat;

  // Log the longitude and latitude to the console
  console.log("Longitude: " + user_longitude)
  console.log("Latitude: " + user_latitude)
     
  // Update the interface the user sees with their location
  document.getElementById("location").innerHTML = "Your location:<br> Latitude: " + user_latitude + "<br>Longitude: " + user_longitude;

}
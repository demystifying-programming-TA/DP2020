// Defining variables & arrays
// ---------
// 1. Define arrays
colors = ['#b0120a', '#ffab91']
columns = ['Country', 'Infections', 'Deaths'];

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

  // Inspect the obtained data in the console
  console.log(user_longitude)
  console.log(user_latitude)

}

// DrawGraph
function InitializeGraph() {

  // Make a client-side API call to obtain the user's location
  $.getJSON("http://ip-api.com/json", function (data, status) {

  // Inspect the data returned from the API
  console.log(data)

  // Extract the user's longitude and latitude from the data that the API returns
  user_longitude = data.lon;
  user_latitude  = data.lat;

  // Inspect the obtained data in the console
  console.log(user_longitude)
  console.log(user_latitude)

}
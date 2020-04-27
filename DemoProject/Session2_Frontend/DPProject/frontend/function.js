  // Obtain data
  // ---------
  latitude = -71.0987
  longitude = 42.3649
  
  // Defining functions
  // ---------
  
  // InitializeGraph
  function InitializeGraph(user_longitude =   longitude, user_latitude=latitude) {
  
    // Log the longitude and latitude to the  console
    console.log("Longitude: " + user_longitude)
    console.log("Latitude: " + user_latitude)
     
    // Update the interface the user sees with  their location
    document.getElementById("location").innerHTML  = "Your location:<br> Latitude: " +   user_latitude + "<br>Longitude: " +   user_longitude;
  
  }
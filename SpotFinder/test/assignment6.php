<?php

$checked = Array();
$lats = Array();
$lngs = Array();
$names = Array();
$icons = Array();
$addresses = Array();
$marker = "";
$latlng ="";
$limitval = "";
$radiusval = "";
$data = "";
$numVenues = 0;

if(isset($_POST['ll'])){
error_reporting(E_ALL);

$reqString = "https://api.foursquare.com/v2/venues/search";
$oAuth = "&oauth_token=2HRDUKX5SIEH2XOQKZ4LK5HSEMUVQGKSGQMDAU0NSSJBOCJM&v=20151116";

$ids = Array(
  "Arts"=> "4d4b7104d754a06370d81259",
  "Food"=> "4d4b7105d754a06374d81259",
  "Night"=> "4d4b7105d754a06376d81259",
  "Outdoors"=> "4d4b7105d754a06377d81259",
  "Shop"=> "4d4b7105d754a06378d81259",
  "Travel"=> "4d4b7105d754a06379d81259",
  "College"=> "4d4b7105d754a06372d81259",
  "Professional"=> "4d4b7105d754a06375d81259",
  "Residence"=> "4e67e38e036454776db1fb3a");



$latlng = "?ll=";
$categories = "&categoryId=";
$limit = "&limit=";
$radius = "&radius=";


foreach($_POST as $key=>$value){

  if($value == "on"){
    $categories .= $ids[$key];
    $categories .= ",";
    array_push($checked,$key);
  }
  if($key == "limit"){
    $limit .= $value;
    $limitval = $value;
  }
  if($key == "radius"){
    $radius .= $value;
    $radiusval = $value;
  }
  if($key == "ll"){
    $latlng .= $value;
  }

}


// echo "$reqString";

$latlng = str_replace("(","",$latlng);
$latlng = str_replace(")","",$latlng);

// echo "$reqString";

if(strlen($categories)>13){

$reqString .= $latlng."&intent=browse".$oAuth.$categories.$limit.$radius;
}

else{
  $reqString .= $latlng."&intent=browse".$oAuth.$limit.$radius;
}

$reqString = str_replace(" ","",$reqString);



$data = file_get_contents($reqString);

$json = json_decode($data,true);
$numVenues = count($json["response"]["venues"]);


for($i=0;$i<$numVenues;$i++){
    array_push($lats,$json["response"]["venues"][$i]["location"]["lat"]);
    array_push($lngs,$json["response"]["venues"][$i]["location"]["lng"]);
    array_push($names,$json["response"]["venues"][$i]["name"]);
    array_push($icons,$json["response"]["venues"][$i]["categories"][0]["icon"]["prefix"]."bg_32".$json["response"]["venues"][$i]["categories"][0]["icon"]["suffix"]);
    if(strlen($json["response"]["venues"][$i]["location"]["address"])>0){
      array_push($addresses,$json["response"]["venues"][$i]["location"]["address"]);
    }
    else{
     array_push($addresses,"N/A"); 
    }
}


}

?>
<html>
  <head>
    <style type="text/css">
      html, body { height: 100%; margin: 0; padding: 0; }
      #map { height: 100%; }
      #overmap {  position: absolute;
                  top: 50px;
                  //left: 25%;
                  z-index: 5;
                  background-color: #fff;
                  padding: 5px;
                  border: 1px solid #999;
                  //text-align: center;
                  font-family: 'Roboto','sans-serif';
                  line-height: 30px;
                  padding-left: 10px;
                }
     .infoWindow{
      text-align: center;
     }
    </style>
  </head>
  <body onload = 'init();'>
    
    <div id = 'overmap'>
    <form onsubmit="return postResults();" method = 'post' action = 'assignment6.php'>
    <input type = 'checkbox' id = 'Arts' name = 'Arts'/>Arts &amp; Entertainment<br/>
    <input type = 'checkbox' id = 'Food' name = 'Food'/>Food<br/>
    <input type = 'checkbox' id = 'Night' name = 'Night'/>Nightlife Spot<br/>
    <input type = 'checkbox' id = 'Outdoors' name = 'Outdoors'/>Outdoors &amp; Recreation<br/>
    <input type = 'checkbox' id = 'Shop' name = 'Shop'/>Shop &amp; Service<br/>
    <input type = 'checkbox' id = 'Travel' name = 'Travel'/>Travel &amp; Transport<br/>
    <input type = 'checkbox' id = 'College' name = 'College'/>College &amp; University<br/>
    <input type = 'checkbox' id = 'Professional' name = 'Professional'/>Professional &amp; Other Places<br/>
    <input type = 'checkbox' id = 'Residence' name = 'Residence'/>Residence<br/>
    Limit(K):<br/>
    <input id = 'limrange' type = 'range' min='0' max='50' step='1' onchange="fillLimit();" /><br/>
    <input name = 'limit' id = 'limit' type = 'text' value = '25' readonly></br>
    Radius(M):<br/>
    <input id = 'radrange' type = 'range' min='0' max='3000' step='100' onchange="fillRadius();" /><br/>
    <input name = 'radius' id = 'radius' type = 'text' value = '1500' readonly></br>
    <input name = 'll' type = 'hidden' id = 'll'/>
    <input type = 'submit' value = 'submit'/>
    </form>
    </div>
    <div id="map"></div>


    <script type="text/javascript">
        
        var placed = false;
        var map;
        

        function init(){
          
          var checked = <?php echo json_encode($checked)?>;
          for(var i=0;i<checked.length;i++){
            document.getElementById(checked[i]).checked = true;
          }
          var limit = <?php echo json_encode($limitval)?>;
          var radius = <?php echo json_encode($radiusval)?>;
          if(limit.length>0){
            document.getElementById('limit').value = limit;
            document.getElementById('limrange').value = parseInt(limit);
          }
          if(radius.length>0){
            document.getElementById('radius').value = radius;
            document.getElementById('radrange').value = parseInt(radius);
          }

          
          var markerPos = <?php echo json_encode($latlng)?>;
          
          if(markerPos.length>5){
            var coord = markerPos.split("=");
            var coords = coord[1].split(",");
            var latlng = new google.maps.LatLng(coords[0],coords[1]);
            marker = new google.maps.Marker({
              position: latlng,
              map: map
            });
            placed = true;
            document.getElementById('ll').value = latlng;
          }

            var numVenues = <?php echo $numVenues;?>;
            var names = <?php echo json_encode($names)?>;
            var icons = <?php echo json_encode($icons)?>;
            var lats = <?php echo json_encode($lats)?>;
            var lngs = <?php echo json_encode($lngs)?>;
            var addresses = <?php echo json_encode($addresses)?>;

            var latlngs = [];
            infoWindows = [];
            if(numVenues>0){
              for(var i=0;i<numVenues;i++){
                infoWindows[i] = new google.maps.InfoWindow();
                latlngs[i] = new google.maps.LatLng(lats[i],lngs[i]);
                marker = new google.maps.Marker({
                  position: latlngs[i],
                  map: map,
                  icon: icons[i],
                  title: names[i]
                });

                    marker.addListener('click', (function(marker,i){
                        return function(){
                        infoWindows[i].setContent(names[i]+"<br>"
                                              +  addresses[i] +"<br>"
                                              + lats[i] + "<br>"
                                              +lngs[i]);
                      infoWindows[i].open(map,marker);
                    }
                      } )(marker,i));


              }

            }
          
          
        }


        function initMap() {

         
          map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: 44.9778, lng: -93.2650},
            zoom: 8
          });

          map.addListener('click', function(e) {
            placeMarker(e.latLng, map);
          });

          //infoWindow = new google.maps.InfoWindow();

        
        }

        function placeMarker(latLng, map){

          markerPos = latLng;

          if(placed==true) marker.setMap(null);
          document.getElementById('ll').value = latLng;
          marker = new google.maps.Marker({
            position: latLng,
            map: map,
            title: "Latitude: " + latLng
          });

          placed = true;
        }

        function postResults(){
          if(placed == false){
            window.alert("Please place a marker");
            return false;
          }
          return true;
        }


        function fillLimit(){
          var limit = document.getElementById('limrange').value;
          document.getElementById('limit').value = limit
        }

        function fillRadius(){
          var radius = document.getElementById('radrange').value;
          document.getElementById('radius').value = radius;
        }

    </script>
    <script async defer
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAfA8LedK_lmGa1fRp3EUqpk2TB11xPy7M&callback=initMap">
    </script>
  </body>
</html>



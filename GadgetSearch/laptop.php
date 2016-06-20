<?php

$smallimages = Array();
$bigimages = Array();
$count=0;
$names = Array();
$prices=Array();
$displays = Array();
$rams = Array();
$weights = Array();
$processors = Array();
$os = Array();
$storages = Array();

if(!empty($_POST)){
	$brand = $_POST['brand'];
	$price = $_POST['price'];
	$servername = 'egon.cs.umn.edu:3307';
	$username = 'F15CS4131U17';
	$password = '3622';
	$port = '3307';

	$conn = mysql_connect($servername,$username,$password);
	if($conn->connect_error){
		die("Connection Failed: ".$conn->connect_error);
	}

	if(!mysql_select_db('F15CS4131U17',$conn)){
		echo 'Failed to select DB';
		exit;
	}

	$query = 'select * from Laptops where Brand='."'".$brand."'";
	$result = mysql_query($query,$conn);

	if(!$result){
		echo 'Failed to execute query'.$query;
		exit;
	}

	while($row = mysql_fetch_assoc($result)){
		array_push($names,$row['Name']);
		array_push($prices,$row['Price']);
		$id = intval($row['id']);
		$query2 = 'select count(id) as count,small,big from imageInfo where id = '.$id;
		$result2=mysql_query($query2,$conn);
		
		if(!$result2){
			echo 'Failed to execute query'.$query2;
			exit;
		}

		while($row2 = mysql_fetch_assoc($result2)){
			array_push($smallimages,$row2['small']);
			array_push($bigimages,$row2['big']);
		}

		$query3 = 'select * from Descriptions where id = '.$id;
		$result3 = mysql_query($query3,$conn);

		if(!result3){
			echo 'Failed to execute query'.$query3;
			exit;
		}

		while($row3 = mysql_fetch_assoc($result3)){
			array_push($displays,$row3['Display']);
			array_push($rams,$row3['RAM']);
			array_push($weights,$row3['Weight']);
			array_push($processors,$row3['Processor']);
			array_push($os,$row3['OperatingSystem']);
			array_push($storages,$row3['Storage']);
		}
	}

	mysql_free_result($result);
	mysql_free_result($result2);
	mysql_free_result($result3);
}
?>

<!DOCTYPE html>
<html lang = 'en'>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1" charset='utf-8'>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<title>
Laptops
</title>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>


<body onload = 'init();'>
<div class='container-fluid' style='width:100%;'>
<nav class='navbar navbar-inverse'>
<div class='container-fluid'>
<div class='navbar-header'>
<a class='navbar-brand' href = '#'>LaptopSearchService</a>
</div>
<ul class = 'nav navbar-nav'>
<li class='active'><a href='#'>Home</a></li>
<li><a href = "laptop.php">Laptops</a></li>
<li><a href = "mobile.php">Mobile Phones</a></li>
<li><a href = "tablet.php">Tablets</a></li>
</ul>
<form onsubmit = 'laptop.php' method = 'post' role='form' style='width:25%'>
<div class='form-group'>
<b>Brand:</b><select name='brand' class='form-control'>
<option></option>
<option>Apple</option>
<option>Samsung</option>
<option>Lenovo</option>
</select>
<br/>
<button type='submit' class='btn btn-default'>Search</button>
</div>
</form>
</div>
</nav>
<div class='container-fluid' id = 'images'>
</div>
<div class='modal fade' id='myModal' role='dialog'>
<div class='modal-dialog'>
<div class='modal-content'>
<div class='modal-header'>
<h4 id='modal-title' class='modal-title'></h4>
</div>
<div class='modal-body' id='modal-body'>
<div class='row' id='row'>
<div class='col-md-6' id='modalImage'>
</div>
<div class='col-md-6' id='modalSpecs'>
</div>
</div>
</div>
<div class='modal-footer'>
<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>
</div>
</div>
</div>
</div>
</div>
</body>
</html>

<script type="text/javascript">
	

	var showing = false;
	var showingbig = false;

	function init(){
		
		document.body.setAttribute('background','black');
		 smallimages = <?php echo json_encode($smallimages)?>;
		 names = <?php echo json_encode($names)?>;
		 prices = <?php echo json_encode($prices)?>;
		 bigimages = <?php echo json_encode($bigimages)?>;
		 displays  = <?php echo json_encode($displays)?>;
		 rams = <?php echo json_encode($rams)?>;
		 weights = <?php echo json_encode($weights)?>;
		 processors = <?php echo json_encode($processors)?>;
		 os = <?php echo json_encode($os)?>;
		 storages = <?php echo json_encode($storages)?>;

		if(smallimages.length>0){
			scrollToImages();

			for(var i=0;i<smallimages.length;i++){
				
				var outerdiv = document.getElementById('images');
				var image=document.createElement('img');
				var picture = 'pictures/';
				var path = picture.concat(smallimages[i]);
				image.setAttribute('src',path);
				image.setAttribute('id',i);
				image.setAttribute('onMouseOver','changeDiv(this);')
				image.setAttribute('onmouseout','changeDiv(this);');
				image.setAttribute('style','width:50%;heigth:50%');
				image.setAttribute('class','img-responsive');
				//image.setAttribute('onclick','openModal(' + i +  ');');
				var name = document.createElement('h4');
				name.innerHTML=names[i];
				var price = document.createElement('h5');
				price.innerHTML = "Price: " + "$" + prices[i];
				outerdiv.appendChild(image);
				outerdiv.appendChild(name);
				outerdiv.appendChild(price);
				var button = document.createElement('button');
				button.setAttribute('type','button');
				button.setAttribute('class','btn btn-info');
				button.setAttribute('id','modal-btn');
				button.setAttribute('onClick','openModal(' + i + ');');
				button.innerHTML='Specs';
				outerdiv.appendChild(button);
				var breaker = document.createElement('br');
				outerdiv.appendChild(breaker);
				outerdiv.appendChild(breaker);
			}
		}
	}

	function scrollToImages(){
		$('html, body').animate({
			scrollTop: $("#images").offset().top},1000);
	}

	function openModal(id){
		fillModal(id);
		$('#myModal').modal();
	}

	function fillModal(id){
		var header = document.getElementById('modal-title');
		header.innerHTML = names[id];
		// var modalBody = document.getElementById('modal-body');
		// modalBody.innerHTML = '<img src = pictures/' + bigimages[id] + ' style="width:50%; height: 50%;">'
		// 					   +'<p>Specs</p>';
		document.getElementById('modalImage').innerHTML = '<img class="img-responsive" src = pictures/' + bigimages[id]+'>';
		document.getElementById('modalSpecs').innerHTML = '<p>Name: '+names[id] + '<br/>'
														   + 'Price: ' + prices[id] + '<br/>'
														   + 'Display: ' + displays[id] + '<br/>'
														   + 'RAM: ' + rams[id] + '<br/>'
														   + 'Weight: ' + weights[id] + '<br/>'
														   + 'Processor: ' + processors[id] + '<br/>'
														   + 'OS: ' + os[id] + '<br/>'
														   + 'Storage: ' + storages[id] + '<br/></p>'; 


	}

	function showImage(id){
		

			var exists = document.contains(document.getElementById('big'));
			
			if(exists){
				deleteSpecs();
				document.getElementById('big').setAttribute('src','pictures/' + bigimages[id]);
				document.getElementById('bigname').innerHTML = names[id];
				var button = document.createElement('button');
				button.innerHTML = 'Specs';
				button.setAttribute('class','w3-btn');
				button.setAttribute('style','position: absolute; left:1000px');
				button.setAttribute('onClick','showSpecs(' + id + ');');
				document.getElementById('bigname').appendChild(button);

			}
			
			else{
				var i = document.createElement('img');
				path = 'pictures/'.concat(bigimages[id]);
				i.setAttribute('src',path);
				i.setAttribute('alt',names[id]);
				i.setAttribute('id','big');
				
				var imagediv = document.getElementById('bigImage');
				imagediv.appendChild(i);
				
				var d = document.createElement('div');
				d.setAttribute('class','w3-title w3-text-black');
				d.setAttribute('id','bigname');
				d.innerHTML = names[id];
				var button = document.createElement('button');
				button.innerHTML = 'Specs';
				button.setAttribute('class','w3-btn');
				button.setAttribute('style','position: absolute; left: 1000px;')
				button.setAttribute('onClick','showSpecs(' + id + ');');

				d.appendChild(button);
				imagediv.appendChild(d);
			}
		




		$('html,body').animate({
			scrollTop: $('#bigImage').offset().top},1000);
		

	}

	function deleteSpecs(){
		document.getElementById('contentdiv').removeChild(document.getElementById('content'));
	}

	function changeDiv(x){
		if(showing == false){

			var parent = x.parentNode;
			var grandparent = parent.parentNode;
			grandparent.setAttribute('class','w3-row w3-margin w3-card-4');
			showing = true;
		}
		else{
			var parent = x.parentNode;
			var grandparent = parent.parentNode;
			grandparent.setAttribute('class','w3-row w3-margin');
			showing = false;
		}

	}


</script>
</body>
</html>
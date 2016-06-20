var manual = false;
var images = new Array(10);

var srcs = ["armory.jpg","pillsbury.jpg","folwell.jpg","jones.jpg","statue.jpg","wesbrook.jpg","nicholson.jpg","eddy.jpg","music.jpg","wulling.jpg"];

var builds=["Armory Building", "Pillsbury Hall", "Folwell Hall", "Jones Hall", "Pillsbury Statue",
			"Wesbrook Hall", "Nicholson Hall", "Eddy Hall", "Music Education",
            "Wulling Hall"];

var ids = ["armo","pill","folw","jone","stat","wesb","nich","eddy","musi","wull"];
var years = ["1896","1889","1907","1901","1900","1898","1890","1886","1888","1892"];        

var archs=["Charles Aldrich","Leroy Buffington with Harvey Ellis", "Clarence H. Johnston, Sr","Charles Aldrich",
			"Daniel C. French, sculptor","Frederick Corser",
            "LeRoy Buffington with Harvey Ellis","LeRoy Buffington","Warren H. Hayes", "Allen Stem and Charles Reed"];

var descs = ["blah1","blah2","blah3","blah4","blah5","blah6","blah7","blah8","blah9","blah10"];
      
function init)(){
	
	for (var i = 0; i<10; i++) {
			images[i] = new Object();
	}
	for(i=0;i<10;i++){
		images[i].id = ids[i];
		images[i].src = srcs[i];
		images[i].arch = archs[i];
		images[i].year = years[i];
		images[i].desc = descs[i];
	}
}


function start(){
	manual = true;
	document.write("Hello");
}
		



		


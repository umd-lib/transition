// change cursor to pointer on hover
function setPointersOnImages(){
	var images = document.getElementsByClassName("imageLink");
	for(var i=0; i<images.length; i++){
		images[i].addEventListener("mouseover", function(){
			if (this.style.display !== "none")
				this.style.cursor = "pointer";
		});
	}
}

document.addEventListener("DOMContentLoaded", function(event) { 
	setPointersOnImages();
});

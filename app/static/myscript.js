$(document).ready(function(){

	$("button").click(function(){

		var text = $("textarea").val();

		$.get("http://localhost:5555/",
			function(data){
				console.log(data)

				$("p.result").text("It was: " + data)
			}
		);
	});
})
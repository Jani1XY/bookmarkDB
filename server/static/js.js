art_loaded = 0
currentPage = 1

window.addEventListener("DOMContentLoaded", (event) => {
    statusCheck();

});

function statusCheck()
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200)
        {
            // nothing o((>ω< ))o
            if(this.status == 200)
            {
                document.getElementById("status").innerHTML = "ONLINE";
                document.getElementById("status").style.color = "white";
            }

        }
    };
    xhttp.open("GET", "http://localhost:80/ping", true);
    xhttp.send();
}

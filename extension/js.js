window.addEventListener("DOMContentLoaded", (event) => {
    // document.getElementById("sendButtonPixiv").addEventListener("click", sendPixiv);
    // document.getElementById("sendButtonNh").addEventListener("click", sendNh);
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
                document.getElementById("status").style.color = "lightgreen";
            }

        }
    };
    xhttp.open("GET", "http://127.0.0.1:4321/ping", true);
    xhttp.send();
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
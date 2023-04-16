const $signinBtn = document.getElementById("signin");
const $login = document.getElementById("login-container");

$signinBtn.addEventListener("click", () => {
    $login.style.display = "block";
});

document.onkeydown = function(e) {
    e = e || window.event;
    if (e.key === "Escape") {
        $login.style.display = "none";
    }
};

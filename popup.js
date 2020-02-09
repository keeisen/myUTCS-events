
function submitChecked(){
    var wicsChecked = document.getElementById("WiCS").checked;
    var hacsChecked = document.getElementById("HACS").checked;
    var isssChecked = document.getElementById("ISSS").checked;
    var convergentChecked = document.getElementById("Convergent").checked;

    document.getElementById("demo").innerHTML = "showing cal";
}

document.addEventListener('DOMContentLoaded', submitChecked() {
    document.querySelector('button').addEventListener('click', clickHandler);
    main();
  });

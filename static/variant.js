function toggleFields()
{
    var shapeField = document.getElementsByName("shape")[0];
    var radiusField = document.getElementById("radiusField");
    var heightField = document.getElementById("heightField");
    var sideField = document.getElementById("sideField");
    if (shapeField.value == "cube")
    {
        radiusField.style.display = "none";
        heightField.style.display = "none";
    sideField.style.display = "block";
    }
    else if (shapeField.value == "sphere")
    {
        radiusField.style.display = "block";
        heightField.style.display = "none";
        sideField.style.display = "none";
    }
    else
    {
        radiusField.style.display = "block";
        heightField.style.display = "block";
        sideField.style.display = "none";
    }
}
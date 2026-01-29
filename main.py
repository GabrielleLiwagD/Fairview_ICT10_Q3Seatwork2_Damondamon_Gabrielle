from pyscript import display,document

def submit_form(e):
    clinic = str(document.querySelector('input[name="clinic"]:checked').value)
    registered = str(document.querySelector('input[name="registered"]:checked').value)
    batch = str(document.getElementById("batch").value)
    section = str(document.getElementById("section").value)

    if clinic != "yes":
        display("Not eligible: medical clearance is required. Go to the clinic and ask for a medical clearance.", target="congratulationsMessage")
    elif registered != "yes":
        display("Not eligible: online registration is required. Please ask your PE teacher regarding the online registration", target="congratulationsMessage")
    elif section == "Ruby":
        display("Congratulations! You are assigned to the Red Bulldogs.", target="congratulationsMessage")
        document.getElementById("teamLogo").innerHTML = "<img src='Red_Bulldogs.png' alt='Red Bulldogs Logo'>"
    elif section == "Sapphire":
        display("Congratulations! You are assigned to the Yellow Tigers.", target="congratulationsMessage")
        document.getElementById("teamLogo").innerHTML = "<img src='Yellow_Tigers.png' alt='Yellow Tigers Logo'>"
    elif section == "Emerald":
        display("Congratulations! You are assigned to the Blue Bears.", target="congratulationsMessage")
        document.getElementById("teamLogo").innerHTML = "<img src='Blue_Bears.png' alt='Blue Bears Logo'>"
    elif section == "Topaz":
        display("Congratulations! You are assigned to the Green Hornets.", target="congratulationsMessage")
        document.getElementById("teamLogo").innerHTML = "<img src='Green_Hornets.png' alt='Green Hornets Logo'>"
    else:
        display("Error: Invalid section selected.", target="congratulationsMessage")
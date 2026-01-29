from pyscript import display,document

def submit_form(e):
    clinic = str(document.querySelector('input[name="clinic"]:checked').value)  #This code works in dealing <input type="ratio">
    registered = str(document.querySelector('input[name="registered"]:checked').value)
    batch = str(document.getElementById("batch").value) #This was not require since all grades are compiled in one team
    section = str(document.getElementById("section").value)

    if clinic != "yes":
        display("Not eligible: medical clearance is required. Go to the clinic and ask for a medical clearance.", target="congratulationsMessage")
    elif registered != "yes":
        display("Not eligible: online registration is required. Please ask your PE teacher regarding the online registration", target="congratulationsMessage")
    elif section == "Ruby":
        document.getElementById("teamLogo").innerHTML = "<img src='Red_Bulldogs.png' alt='Red Bulldogs Logo'>" #This image may took some time to load.
        display("Congratulations! You are assigned to the Red Bulldogs.", target="congratulationsMessage")
    elif section == "Sapphire":
        document.getElementById("teamLogo").innerHTML = "<img src='Yellow_Tigers.png' alt='Yellow Tigers Logo'>"
        display("Congratulations! You are assigned to the Yellow Tigers.", target="congratulationsMessage")
    elif section == "Emerald":
        document.getElementById("teamLogo").innerHTML = "<img src='Blue_Bears.png' alt='Blue Bears Logo'>"
        display("Congratulations! You are assigned to the Blue Bears.", target="congratulationsMessage")
    elif section == "Topaz":
        document.getElementById("teamLogo").innerHTML = "<img src='Green_Hornets.png' alt='Green Hornets Logo'>" 
        display("Congratulations! You are assigned to the Green Hornets.", target="congratulationsMessage")
    else:  #This won't work since it will only result in AttributeError
        display("Error: Invalid section selected.", target="congratulationsMessage")

// Emailjs script
function sendMail() {
    var params = {
        from_name: document.getElementById("name").value,
        surname: document.getElementById("surname").value,
        subject: document.getElementById("subject").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value,
    };

    const serviceID = "service_onhhlab";
    const templateID = "template_5aqdtop";

    emailjs
        .send(serviceID, templateID, params)
        .then( 
            function (response) {
                document.getElementById(
                    "email-result"
                ).innerHTML = `<p style="color:green;font-weight:bold">Thanks for your email!
            <br> We will contact you as soon as possible!</p>`;
            },
            function (error) {
                 document.getElementById(
                    "email-result"
                ).innerHTML = `<p style="color:green;font-weight:bold">Sorry, something went wrong!
            <br> Try to send an email again.</p>`;
            }
        );
    return false;
}
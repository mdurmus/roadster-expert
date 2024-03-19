// Emailjs script
function sendMail() {
    var params = {
        from_name: document.getElementById("name").value,
        surname: document.getElementById("surname").value,
        subject: document.getElementById("subject").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value,
    };

    const serviceID = "service_9zv91ys";
    const templateID = "template_laidu4t";


    emailjs
        .send(serviceID, templateID, params)
        .then( 
            function (response) {
                document.getElementById(
                    "email_alert"
                ).innerHTML = `<h4 class="email-sent-message alert-success">Thanks for your email!
            <br> We will contact you as soon as possible!</h4>`;
            },
            function (error) {
                document.getElementById(
                    "email_alert"
                ).innerHTML = `<h4 class="email-sent-message alert-danger">Sorry, something went wrong!
            <br> Try to send an email again.</h4>`;
            }
        );
    return false; // To block from loading a new page
}

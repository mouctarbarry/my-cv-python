document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Empêche l'envoi du formulaire par défaut

        const comments = form.querySelectorAll(".comments");
        comments.forEach(comment => comment.textContent = "");

        const formData = new FormData(form);
        const xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Succès : le script Python a été exécuté
                    const response = JSON.parse(xhr.responseText);
                    if (response.success) {
                        Swal.fire({
                            icon: "success",
                            title: "Message envoyé",
                            text: "Merci de m'avoir contacté, je vous répondrai dès que possible",
                        });
                        form.reset(); // Réinitialiser le formulaire
                    } else {
                        const fields = {
                            'firstname': document.getElementById('firstname'),
                            'name': document.getElementById('name'),
                            'email': document.getElementById('email'),
                            'message': document.getElementById('message')
                        };

                        Object.keys(fields).forEach(fieldKey => {
                            const comment = fields[fieldKey].parentNode.querySelector('.comments');

                            if (response.message[fieldKey]) {
                                comment.textContent = response.message[fieldKey];
                            } else {
                                comment.textContent = "";
                            }
                        });
                    }
                } else {
                    // Erreur HTTP lors de l'exécution du script Python
                    Swal.fire({
                        icon: "error",
                        title: "Erreur d'envoi",
                        text: "Une erreur est survenue lors de l'envoi du message.",
                    });
                }
            }
        };

       xhr.open("POST", "/submit_form", true);
       xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
       xhr.send(formData);

    });
});


const aboutPText = "Hello, I'm Mouctar";
const aboutWText = "DevOps Engineer";

function typeTextInLive(elementId, text, typingSpeed) {
    const typingElement = document.getElementById(elementId);

    if (!typingElement) {
        console.error(`Element with ID '${elementId}' not found.`);
        return;
    }

    let charIndex = 0;

    function typeText() {
        if (charIndex < text.length) {
            typingElement.textContent += text.charAt(charIndex);
            charIndex++;
            setTimeout(typeText, typingSpeed);
        }
    }

    return new Promise(resolve => {
        typeText();
        setTimeout(resolve, text.length * typingSpeed);
    });
}

document.addEventListener("DOMContentLoaded", async function() {
    await typeTextInLive("aboutP", aboutPText, 30);
    await typeTextInLive("aboutW", aboutWText, 50);
});

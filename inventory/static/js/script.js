document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("edit-review").addEventListener("click", function() {
        document.getElementById("leave-review-form").style.display = "none";
        document.getElementById("edit-review-button").style.display = "none";
        document.getElementById("edit-review-form").style.display = "block";

        // Populate existing review details in the form
        var userReviewInfo = document.getElementById("user-review-info").innerText;
        var reviewDetails = userReviewInfo.split(" - ");
        document.getElementById("id_comment").value = reviewDetails[0];
        // Assuming your rating input field has the id "id_rating"
        document.getElementById("id_rating").value = parseInt(reviewDetails[1].split(": ")[1]);
    });
});


function toggleBookmark(element, costumeId) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/toggle-bookmark/' + costumeId + '/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Toggle the visual representation of bookmark status
            element.innerHTML = (data.is_bookmarked) ? '★' : '☆';
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const facebookButton = document.querySelector('.facebookButton');
    const shopeeButton = document.querySelector('.shopeeButton');
    
    function toggleTextVisibility(button) {
        const tooltip = button.querySelector('.tooltip');
        if (tooltip) {
            tooltip.style.display = (tooltip.style.display === 'none' || tooltip.style.display === '') ? 'block' : 'none';
        }
    }

    facebookButton.addEventListener('mouseover', function () {
        toggleTextVisibility(facebookButton);
    });

    shopeeButton.addEventListener('mouseover', function () {
        toggleTextVisibility(shopeeButton);
    });
});

let slideIndex = 1;

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  if (n > slides.length) {
    slideIndex = 1;
  }

  if (n < 1) {
    slideIndex = slides.length;
  }

  slides[slideIndex - 1].style.display = "block";
}

showSlides(slideIndex);


    $(document).ready(function () {
        $("#upload-form").submit(function (e) {
            e.preventDefault();  // Prevent the default form submission

            var formData = new FormData(this);

            $.ajax({
                type: "POST",
                url: "{% url 'editprofile' %}",
                data: formData,
                processData: false,
                contentType: false,
                success: function (data) {
                    // Handle the success response if needed
                    console.log("Profile picture updated successfully!");
                },
                error: function (error) {
                    // Handle the error response if needed
                    console.error("Error updating profile picture:", error);
                }
            });
        });
    });







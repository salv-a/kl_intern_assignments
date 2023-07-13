function openModal(userType, userCount) {
    var userDetails = document.getElementById("user-details");
    userDetails.innerHTML = `
      <p><strong>User Type:</strong> ${userType}</p>
      <p><strong>User Count:</strong> ${userCount}</p>
     
    `;


    var modal = document.getElementById("modal");
    modal.style.display = "block";
  }
  
  function closeModal() {
    
    var modal = document.getElementById("modal");
    modal.style.display = "none";
  }
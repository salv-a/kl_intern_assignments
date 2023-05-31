function openModal(userName, userId, userType, createdBy, lastAccessedDate, contactNo, emailId) {
    var userDetails = document.getElementById("user-details");
    userDetails.innerHTML = `
      <p><strong>User Name:</strong> ${userName}</p>
      <p><strong>User ID:</strong> ${userId}</p>
      <p><strong>User Type:</strong> ${userType}</p>
      <p><strong>Created By:</strong> ${createdBy}</p>
      <p><strong>Last Accessed Date:</strong> ${lastAccessedDate}</p>
      <p><strong>Contact No:</strong> ${contactNo}</p>
      <p><strong>Email ID:</strong> ${emailId}</p>
    `;


    var modal = document.getElementById("modal");
    modal.style.display = "block";
  }
  
  function closeModal() {
    
    var modal = document.getElementById("modal");
    modal.style.display = "none";
  }
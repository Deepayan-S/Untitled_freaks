
document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();  // Prevent the default form submission


    const firstName = document.querySelector('.first-name').value;
    const lastName = document.querySelectorAll('.first-name')[1].value;  // Grabs the second 'first-name' input
    const email = document.querySelector('.email').value;
    const password = document.querySelectorAll('.email')[1].value;  // Grabs the second 'email' input for password

    const userData = {
        firstName: firstName,
        lastName: lastName,
        email: email,
        password: password
    };

    try {
      
        const response = await fetch('https://your-backend-url/api/register', { // DUMMY URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)  // Convert the userData object to JSON string
        });

        const data = await response.json();  // Parse the response from the backend

        
        if (response.ok) {
            alert('Account created successfully!');
            window.location.href = '/joblisting';  // Redirect to the job listing page or dashboard
        } else {
            alert('Account creation failed: ' + data.message);  // Show an error message
        }
    } catch (error) {
        console.error('Error during account creation:', error);
        alert('An error occurred. Please try again.');
    }
});

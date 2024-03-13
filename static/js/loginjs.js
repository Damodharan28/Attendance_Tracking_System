$(document).ready(function() {
    // Hide the login form initially
    // $('.login-form').hide();
    
    // Toggle between register and login forms when clicking "Sign In" or "Create an account"
    $('.message a').click(function(){
        // Toggle the visibility of the forms
        $('.register-form').toggle("slow");
        $('.login-form').toggle("slow");
    });
});
# Retreat Right - Testing

**All testing for this project has been done manually**

## Link testing

| Tests ran as a user | Actions | Outcome |
|:---|---:|:---:|
| The logo | Taken back to the home page upon clicking | Successful - Works as expected |
| Navigation Links | Able to view every page upon clicking | Successful - Works as expected |
| Log In Link | Takes the user to the Log In page and form | Successful - Works as expected |
| Log Out Link | Takes the user to the Log Out page and form | Successful - Works as expected |
| Sign Up Link | Takes the user to the Sign Up page and form | Successful - Works as expected |
| Home Link | Takes the user to the home page | Successful - Works as expected |
| About Link | Takes the user to the About Page | Successful - Works as expected |
| Instagram Footer Link | Takes the user to a seperate browser page | Successful - Works as expected |
| LinkedIn Footer Link | Takes the user to a seperate browser page | Successful - Works as expected |
| Post Snippet Links | Takes the user to the full blog post page | Successful - Works as expected |
| Sign In Link - Sign Up Page | Takes to the user to the Sign In page | Successful - Works as expected |
| Next Button (under post snippets) | Displays the next three post snippets to the user | Successful - Works as expected |

### Contact Form

| Tests ran as a user and superuser | Actions | Outcome |
|:---|---:|:---:|
| Contact Form - Name Field | The user is required to fill out this field before submitting | Successful - Works as expected |
| Contact Form - Email Field | The user is required to fill out this field correctly before submitting | Successful - Works as expected |
| Contact Form - Message Field | The user is required to have content in this field before submitting (cannot be left blank) | Successful - Works as expected |
| Contact Form - Submit Button | The form clears after the submit button is clicked | Successful - Works as expected |
| Contact Form - Admin Panel | The contact request is recieved in the admin panel | Successful - Works as expected |

**Contact Form - Name Field**

![Contact Form - Name](documentation/testing/contact-name.png)

**Contact Form - Email Field**

![Contact Form - Email](documentation/testing/contact-email.png)

**Contact Form - Message Field**

![Contact Form - Message](documentation/testing/contact-message.png)

**Contact Form - Admin Panel**

![Contact Form - Admin](documentation/testing/contact-admin.png)

### Log In Form

| Tests ran as a user | Actions | Outcome |
|:---|---:|:---:|
| Log In Form - Username | The user is required to add input to this field (cannot be blank) | Successful - Works as expected |
| Log In Form - Username | The user is required to use a correct username to be able to procceed | Successful - Works as expected |
| Log In Form - Password | The user is required to add input to this field (cannot be blank) | Successful - Works as expected |
| Log In Form - Password | The user is required to use a correct password to be able to procceed | Successful - Works as expected |
| Log In Form - Both | The user is required to fill out all fields correctly to continue | Successful - Works as expected |
| Log In Form - Button | The user is taken to the home page after correct input submission | Successful - Works as expected |


**Log In Form - Username**

![Log In Form - Username](documentation/testing/login-username.png)

**Log In Form - Password**

![Log In Form - Password](documentation/testing/login-password.png)

**Log In Form - Both (Correct Input)**

![Login Form - Both](documentation/testing/login-both.png)

### Log Out Form

| Tests ran as a user | Actions | Outcome |
|:---|---:|:---:|
| Log Out Form - Button | The user is taken back to the homepage as a signed out user upon clicking | Successful - Works as expected |


### Sign Up Form

| Tests ran as a user and superuser | Actions | Outcome |
|:---|---:|:---:|
| Sign Up Form - Username | The user is required to fill out this field | Successful - Works as expected |
| Sign Up Form - Email | The user is not required to fill out this field | Successful - Works as expected |
| Sign Up Form - Password | The user is required to fill out this field in compliance to the instructions given | Successful - Works as expected |
| Sign Up Form - Password (again) | The user is required to fill out this field identical to the prior password field | Successful - Works as expected |
| Sign Up Form - Admin | Once a user is signed up they are added to the users in the admin panel | Successful - Works as expected |

**Sign Up Form - Username**

![Sign Up Form - Username](documentation/testing/signup-username.png)

**Sign Up Form - Password**

![Sign Up Form - Password](documentation/testing/signup-password.png)

**Sign Up Form - Password (again)**

![Sign Up Form - Password (again)](documentation/testing/signup-password-again.png)

### Profile Form

| Tests ran as a user and superuser | Actions | Outcome |
|:---|---:|:---:|
| Profile Form - Name | The user is required to fill in this field before submission | Successful - Works as expected |
| Profile Form - Email | The user is required to fill out this field before submission |Successful - Works as expected |
| Profile Form - About You | This user is not required to fill out this field before submission | Successful - Works as expected |
| Profile Form - Button | The user information is saved and stored into the form upon submission | Successful - Works as expected |
| Profile Form - Admin | The user profile is able to be viewed and edited from the admin panel | Successful - Works as expected |

**Profile Form - Name**

![Profile Form - Name](documentation/testing/profile-name.png)

**Profile Form - Email**

![Profile Form - Email](documentation/testing/profile-email.png)

**Profile Form - Admin**

![Profile Form - Admin](documentation/testing/profile-admin.png)

### Comment Form

| Tests ran as a user and superuser | Actions | Outcome |
|:---|---:|:---:|
| Comment Form - Body | The user is required to fill out this field before submission (cannot be blank) | Successful - Works as expected |
| Comment Form - Submitted Comment | The users comment can be editted or deleted upon submission, both before and after being approved | Successful - Works as expected |
| Comment Form - Admin | Comments are able to be editied, delelted and approved from the admin panel | Successful - Works as expected |

**Comment Form - Body**

![Comment Form - Body](documentation/testing/comments-body.png)

**Comment Form - Update**

![Comment Form - Update](documentation/testing/comments-update.png)

**Comment Form - Delete**

![Comment Form - Delete](documentation/testing/comments-delete.png)

**Comment Form - Admin**

![Comment Form - Admin](documentation/testing/comments-admin.png)

### Like

| Tests ran as a user | Actions | Outcome |
|:---|---:|:---:|
| Likes - Posts | The likes heart icon turns red and the number of likes incremented upon clicking | Successful - Works as expected |
| Likes - Posts Admin | The likes are displayed in the admin panel upon clicking | Successful - Works as expected |

### Notifications and messages 

| Tests ran as a user | Actions | Outcome |
|:---|---:|:---:|
| Messages - Contact | A confirmation message is displayed to the user upon contact form submission | Successful - Works as expected |
| Messages - Profile | A confirmation message is displayed to the user upon profile form submission | Successful - Works as expected |
| Messages - Log In | A confirmation message is displayed to the user upon signing in | Successful - Works as expected |
| Messages - Sign Up | A confimation of log in message is displayed to the user upon signing up | Successful - Works as expected |
| Messages - Log Out | A Sign Out message is displayed to user upon signing out | Successful - Works as expected |
| Messages - Comment Submit | A confirmation message is displayed to the user upon submitting a comment | Successful - Works as expected |
| Messages - Comment Update | A confirmation message is displayed to the user upon updating a comment | Successful - Works as expected |
| Messages - Comment Delete | A confirmation message is displayed to the user upon deleting a comment | Successful - Works as expected |

**Messages - Contact** 

![Messages - Contact](documentation/testing/messages-contact.png)

**Messages - Profile**

![Messages - Profile](documentation/testing/messages-profile.png)

**Messages - Log In**

![Messages - Log In](documentation/testing/messages-login.png)

**Messages - Log Out**

![Messages - Log Out](documentation/testing/messages-logout.png)

**Messages - Comment Submit**

![Messages - Comment Submit](documentation/testing/messages-comment-submit.png)

**Messages - Comment Update**

![Messages - Comment Update](documentation/testing/messages-comment-update.png)

**Messages - Comment Delete**

![Messages - Comment Delete](documentation/testing/messages-comment-delete.png)
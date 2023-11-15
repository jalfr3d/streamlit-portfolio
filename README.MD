# Streamlit Portfolio

This project is a Streamlit-based portfolio website that showcases a Python developer's work and provides a way for visitors to contact the developer. It consists of a main page displaying the developer's information and a list of projects from a CSV file. It also includes a "Contact Us" page with a form for sending email messages to the developer.

## Main Page
The main page of the portfolio website is the entry point for visitors. It displays the developer's profile picture, a title, and a brief introduction. Below the introduction, there is a list of projects with their titles, descriptions, images, and source code links.

### Dependencies
- Streamlit
- Pandas

The main page code is located in `main.py`.

## Contact Us Page
The "Contact Me" page allows visitors to send an email message to the developer. It includes a form with fields for the visitor's email address and message. When the visitor submits the form, the email message is sent using the provided email address and a predefined email template.

The "Contact Me" page code is located in the `contact.py` file.

### Dependencies
- Streamlit

## Sending Email
The email sending functionality is handled in the `send_email.py` file. It uses SMTP to send emails and requires the following information to be provided in the code:
- Sender's email address
- Password (stored as an environment variable for security)
- Receiver's email address
- SMTP server information

Please ensure you replace the placeholders with your actual email addresses and the appropriate SMTP server details.

### Dependencies
- smtplib
- ssl
- os

## Portfolio Data
The portfolio project data is read from a CSV file. The CSV file should be structured with at least the following columns:
- `title`: The title of the project
- `description`: A description of the project
- `image`: The filename of the project's image (located in the "images" directory)
- `url`: The source code URL of the project

The data is loaded and displayed on the main page.

## Running the Portfolio
To run the portfolio website, make sure you have Streamlit and other required dependencies installed. You can run it using the following command:

```
streamlit run main.py
```

## License

This project is licensed under the MIT License. You are free to use and modify the code for your own purposes.


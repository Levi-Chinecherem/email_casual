# O Sender - Company Mail Sender

O Sender is a simple Django web application that allows users to send company-like emails to their friends, pretending to own a company. Users can customize the email recipient, company name, and message content.

## Features

- **Customizable Emails:** Users can enter the email address of the recipient, choose a company name, and compose a personalized message.
- **Pretend to Own a Company:** Have fun sending emails as if you own a company, making the communication more engaging.

## Setup Instructions

### Prerequisites

- Python (3.6 or higher)
- Django

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/email_casual.git
   ```
2. Navigate to the project directory:

   ```bash
   cd email_casual
   ```
3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

### Configuration

1. Open `main_p/settings.py`.
2. Update the `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` with your Gmail account credentials or the desired SMTP server.

### Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## Usage

1. Navigate to the "Send Email" page.
2. Enter the recipient's email, your desired company name, and the message content.
3. Click the "Send Email" button to send the email.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy sending playful company-like emails with O Sender!

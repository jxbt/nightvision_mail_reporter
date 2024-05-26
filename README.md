
# NightVision Mail Reporter

## Description

`NightVision Mail Reporter` is a tool used to automate the process of importing security vulnerability findings from a NightVision scan results file into user-friendly PDF reports and share these reports via email (e.g., Gmail or Outlook).

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/jxbt/nightvision_mail_reporter.git
   cd nightvision_mail_reporter
   ```

2. **Install Dependencies:**
   ```sh
   chmod +x install.sh && sudo ./install.sh
   python3 -m venv .venv
   source .venv/bin/activate
   pip3 install -r requirements.txt
   ```

## Usage

To use the NightVision Mail Reporter, provide the path to your SARIF file along with your Email Settings:

```sh
source .venv/bin/activate
python3 main.py --sarif r.sarif --sender your_email@example.com --password "your_email_password" --receiver receiver_email@example.com --outlook
```

### Flags:

| Flag          | Description                                                                          | 
| ------------- | ------------------------------------------------------------------------------------ |
| -s, --sarif   | Path to the SARIF file containing the security analysis results.                     |                    
| -o, --out     | Path to the output PDF file.                                                         |                    
| --sender      | The sender's email address.                                                          |                    
| --password    | The sender's email password.                                                         |                    
| --receiver    | The receiver's email address.                                                        |                    
| --server      | The SMTP server address.                                                             |                    
| --port        | The SMTP server port.                                                                |                    
| --gmail       | Use Gmail's SMTP server (sets server to `smtp.gmail.com` and port to `587`).         |                    
| --outlook     | Use Outlook's SMTP server (sets server to `smtp-mail.outlook.com` and port to `587`).|     



**Note:** For Gmail, you must create and use a Google App Password. This is because Google does not allow access to your Gmail account using just your Gmail password when accessing via third-party apps apps.

### Examples

1. To run the script and send an email using Gmail's SMTP server:

  ```sh
  source .venv/bin/activate
  python3 main.py --sarif r.sarif --sender your_email@gmail.com --password "your_email_password" --receiver receiver_email@example.com --gmail
  ```
2. To run the script and send an email using Outlook's SMTP server:

  ```sh
  source .venv/bin/activate
  python3 main.py --sarif r.sarif --sender your_email@outlook.com --password "your_email_password" --receiver receiver_email@example.com --outlook
  ```

3. To run the script and send an email using a custom SMTP server:
  ```sh
  source .venv/bin/activate
  python3 main.py --sarif r.sarif --sender your_email@outlook.com --password "your_email_password" --receiver receiver_email@example.com --server smtp.example.com --port 1337
  ```

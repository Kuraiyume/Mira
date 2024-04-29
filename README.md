# Mira Password Manager

Mira is our innovative password management solution designed specifically for the command-line interface (CLI). With a streamlined and efficient approach, Mira provides a robust solution to the vulnerabilities associated with password management in the digital era.

## Objectives

- **Offline Security**: Mira prioritizes offline functionality to ensure password management without dependence on internet connectivity. This approach enhances security by minimizing the attack surface and reducing exposure to online threats.

- **Local Storage**: The password manager facilitates secure storage and retrieval of passwords locally on the user's machine, ensuring data confidentiality and reducing reliance on external servers or cloud services.

- **No Cloud Dependencies**: Mira does not rely on external servers or cloud services for enhanced privacy and control. This approach eliminates the risk of unauthorized access or data breaches associated with online storage.

- **Data Confidentiality**: To ensure the privacy of user data, Mira implements encryption and secure storage procedures, employing Argon2 for hashing the user data. This ensures that even if the device is compromised, the stored passwords remain unreadable without the decryption key.

- **Isolated Environment**: Mira operates within the user's system, minimizing exposure to external threats or vulnerabilities. This isolated environment enhances security by reducing the likelihood of unauthorized access or data breaches.

- **Usability**: Mira provides a user-friendly command-line interface for easy interaction, allowing users to efficiently manage their passwords without the need for complex technical knowledge.

- **Security Best Practices**: The password manager encourages secure practices such as safeguarding master keys, enabling Two-Factor Authentication (2FA), and emphasizing password complexity to enhance overall security.

- **Control**: Mira empowers users with complete control over their password manager, as it operates locally within the system and functions entirely offline. This provides users with a sense of independence and control over their sensitive information.

## Why MIRA is Considered Secure?

- **Limited Attack Surface**: Operating offline reduces the potential attack surface, minimizing vulnerabilities and enhancing overall security.

- **No Cloud Dependency**: Mira does not store user data in the cloud, reducing the risk of unauthorized access or data breaches associated with online storage. Users have direct control over their data, enhancing privacy and security.

- **Lower Exposure to Online Threats**: Due to its offline nature, Mira is less susceptible to phishing attacks or server breaches common with online password managers. Offline managers are not reliant on online authentication, reducing exposure to online threats.

- **Local Encryption**: Mira employs strong encryption algorithms to protect user data. Data is stored locally, and encryption ensures that even if the device is compromised, the stored passwords remain encrypted and unreadable without the decryption key.

- **Zero-Knowledge Architecture**: Mira ensures the privacy of user data by handling passwords without actually knowing what they are. It encrypts and decrypts data locally, ensuring sensitive information stays private, even from the password manager itself.

- **User Independence**: Users have full control over their password manager since it operates within their system. There's no reliance on external services, providing a sense of independence and reducing potential points of failure.

- **No Password Retrieval Over Network**: Password retrieval and storage occur locally, eliminating the need to transmit sensitive information over the network. This reduces the chances of interception or man-in-the-middle attacks.

- **Offline Password Generation**: Mira can generate passwords without requiring an internet connection, offering convenience and security, especially in situations where online access is limited.

- **No Third-Party Involvement**: Mira operates autonomously without any reliance on external service providers, ensuring enhanced security by eliminating potential risks associated with third-party entities. Users can fully trust the locally implemented security measures without involving external platforms.

- **Increased Privacy Control**: Users benefit from enhanced privacy control as their sensitive data remains within their own environment. There is no need to trust external servers with personal information, contributing to a more private and secure user experience.

- **No Connection Latency**: Users experience minimal latency since their password data is instantly accessible locally. This absence of network communication reduces the risk of delays or disruptions that might be exploited by attackers attempting to compromise the system.

*While offline password managers provide significant security benefits, users should remain vigilant about security best practices. It's crucial to store the master key and decryption key in a secure location on their device. Unfortunately, human error often poses the primary challenge in adhering to these practices.*

## MIRA's Credential Storage Capabilities

MIRA supports various types of credentials, including:

- **Account Passwords**: MIRA enables users to securely store and manage passwords for a variety of accounts, such as those used for websites, applications, and services. It employs encryption techniques to safeguard these passwords, preventing unauthorized access and ensuring user privacy and security online.

- **Credit/Debit Card PINs**: MIRA provides a secure repository for storing sensitive financial information, including PINs for credit and debit cards. By encrypting this data and implementing robust security measures, MIRA ensures that users can safely store and access their card PINs, protecting them from unauthorized use and fraudulent activities.

- **API Keys**: MIRA offers a secure environment for storing API keys, which are authentication credentials used to access web services or APIs. By securely managing these keys, MIRA helps prevent unauthorized access to sensitive data and resources, enhancing the overall security of applications and systems that rely on API authentication.

- **SSH(RSA) Keys**: MIRA supports the storage and management of SSH keys, which are cryptographic keys used for secure remote access to servers and systems via the Secure Shell (SSH) protocol. By safeguarding SSH keys within its encrypted storage, MIRA helps users securely authenticate and access remote systems, minimizing the risk of unauthorized access and potential security breaches.

- **Source Codes**: MIRA allows users to store and protect their project source codes securely. By providing encrypted storage for source code files, MIRA helps developers safeguard their intellectual property and sensitive project information, ensuring that their code remains confidential and protected from unauthorized access or tampering.

- **Private Notes**: MIRA enables users to securely store private information, such as personal notes, sensitive documents, or confidential data. By encrypting these notes and providing secure storage, MIRA helps users safeguard their privacy and sensitive information, ensuring that it remains inaccessible to unauthorized individuals or malicious actors.

## Features

- **Comprehensive Credential Storage**: MIRA offers sophisticated storage capabilities, accommodating an extensive range of credentials. These include Platform Accounts, Credit/Debit Card PINs, API Keys, SSH(RSA) Keys, Source Codes, and Private Notes. This breadth of storage options ensures MIRA's flexibility in securely managing diverse types of credentials for users.

- **Multi-Factor Authentication**: Before the user can go to the main menu of MIRA, the user needs to login first. In login prompt, the user needs to enter the master password and the encryption key that has been generated after successful registration and a time-based 6-digit from 2FA if enabled.

- **Secure Storage**: Passwords are encrypted using the Fernet symmetric encryption algorithm, ensuring data confidentiality and integrity. Without the encryption key, it will be almost impossible to retrieve or recover the content.

- **Carrier Lookup**: When you use a phone number for your platform credential instead of email, MIRA will detect its Carrier. This feature can help to validate the phone number that has been entered by the user.

- **Mnemonic Phrase**: Since the encryption key is generated in Base64 format, it's hard to memorize and maintain, that's why MIRA can turn the user's encryption key to a memorable and maintainable mnemonic phrase. 

- **Password Strength Checker**: Ensures that passwords meet recommended strength criteria based on established password policies.

- **Password/PINs Expiry Notifications**: Users receive warnings when passwords are about to expire, prompting them to change passwords regularly for enhanced security.

- **Password Generator**: Mira offers various password generation methods to create strong and unique passwords tailored to user preferences.

- **Password Expiry Lister**: Allows users to view the remaining time until a password expires, facilitating proactive password management.

- **Accessible Instructions**: Prioritized creating intuitive guidance for MIRA, a Terminal-Based Password Manager, ensuring it offers the utmost user-friendliness.

- **Enhanced User Data Encryption**: Worked hard to make your password vault more secure by adding more complex encryptions in your main user in MIRA.

- **Loggings Tracker**: Mira can track login attempts, with the time logged and the status if the logging is successful or not, and the entered username.
  
- **Reset Functionality**: In the Premium Version, MIRA offers a reset option designed to provide users with a comprehensive tool for data management. By selecting this option, users can initiate a process that deletes all saved credentials, including their primary MIRA account. This feature serves as a safeguard, enabling users to reset their MIRA instance in situations such as compromised accounts or a need for a fresh start.

*Please note: Resetting MIRA will permanently delete all stored credentials, and this action cannot be undone. Exercise caution and ensure that you have backed up any essential data before proceeding with the reset. MIRA will not be able to recover any deleted credentials after the reset is complete.*


## OS Compatibility

- [x] Tested on Windows
- [ ] Tested on macOS
- [x] Tested on Linux

## Installation
## Unix-Based Systems
1. **Clone Repository**: Use Git to clone the Mira repository onto your system:
   ```bash
   git clone https://github.com/veilwr4ith/MIRA
   ```

2. **Navigate to Directory**: Move into the Mira directory:
   ```bash
   cd MIRA
   ```

3. **Make the installer executable**:
   ```bash
   chmod +x installer.sh
   ```

4. **Run the installer**:
   ```bash
   sudo ./installer.sh
   ```
   
5. **Verify Installation**: After installation, verify that Mira is successfully installed by running the program:
    ```bash
    sudo MIRA
    ```
    
## Windows 

1. **Clone the repository of MIRA (If Git is Installed)**:
   ```bash
   git clone https://github.com/veilwr4ith/MIRA
   ```

8. **Install Libraries**:
   ```bash
   python3 or py setup.py
   ```

9. **Once the installation has been successfully completed, you can now now use MIRA**:
   ```bash
   python3 or py MIRA.py
   ```

## For Executable Version of MIRA

- Click this link and Download: [here](https://www.mediafire.com/file/7xwlcsm7fher5ph/MIRA.exe/file)



*Make sure that when you're using Windows, run the installation and MIRA as administrator. As well as the executable file, run it as Administrator.*

## Usage

To use Mira effectively:

- Typing `h` or `help` in the Mira prompt provides guidance.
- Before logging in, create a master user to secure the password vault.

## Commands

Once logged in, users can utilize various commands, including:

| **Command**             | **Description**                                                                |
|-------------------------|--------------------------------------------------------------------------------|
| **1. Adding Credentials** |                                                                              |
| `add_platform_passwd`   | Add a new password                                                            |
| `add_api_key`           | Add a new API key                                                              |
| `add_card_pin`          | Add a new PIN                                                                  |
| `add_ssh_key`           | Add a new SSH Key                                                              |
| `add_src_code`          | Add a new Source Code                                                          |
| `add_priv_note`         | Add a new Private Note                                                         |
| **2. Retrieving Credentials** |                                                                          |
| `get_platform_passwd`   | Retrieve the plaintext version of the password for the desired account ID     |
| `get_api_key`           | Retrieve the plaintext version of the key of the desired account ID           |
| `get_card_pin`          | Retrieve the plaintext version of the PIN for the desired card ID             |
| `get_ssh_key`           | Retrieve the plaintext version of the SSH Key for the desired key ID          |
| `get_src_code`          | Retrieve the plaintext version of the Source Code for the desired code ID     |
| `get_priv_note`         | Retrieve the plaintext version of the Private Note for the desired note ID    |
| **3. Deleting Credentials** |                                                                           |
| `del_platform_passwd`   | Delete a saved password according to your desired account ID                  |
| `del_api_key`           | Delete key according to your desired account ID                                |
| `del_card_pin`          | Delete a saved PIN according to your desired card ID                           |
| `del_ssh_key`           | Delete a saved SSH Key according to your desired key ID                        |
| `del_src_code`          | Delete a saved Source Code according to your desired code ID                  |
| `del_priv_note`         | Delete a saved Private Note according to your desired note ID                 |
| **4. Changing Credentials** |                                                                          |
| `ch_platform_pass`      | Change the password for the desired account ID                                 |
| `ch_card_pin`           | Change the password for the desired pin ID                                     |
| `ch_api_key`            | Change the API Key for the desired account ID                                  |
| `ch_ssh_key`            | Change the SSH Key for the desired key ID                                      |
| `ch_src_code`           | Change the Source Code for the desired code ID                                 |
| `upd_priv_note`         | Update the Private Note based on note ID                                       |
| **5. Security and Configuration** |                                                                        |
| `enable2fa`             | Enable Two-Factor Authentication for added security                            |
| `genpasswd`             | Generate a strong password                                                     |
| `changemaster`          | Change the masterkey                                                            |
| **6. Listing and Analysis** |                                                                              |
| `show_passwd_exp`       | List all usernames and their status on a specific platform or all              |
| `show_pin_exp`          | List all card numbers and their status on a specific card type or all          |
| `show_api_key`          | List all available API Key with their Key ID, Platform, Key Name, and Date      |
| `show_ssh_key`          | List all available SSH Key with their Key ID, Username, Key Name, and Date     |
| `show_src_code`         | List all available Source Code with their Code ID, File Name, and Date          |
| `show_priv_note`        | List all available Private Note with their note ID, Title, and Date            |
| `show_passwd_strength`  | List the strength of the password of a username on a specific platform         |
| **7. Securing Encryption Key** |                                                   |
| `mnemonic_enc_key`      | Convert the encryption key to a mnemonic phrase                                 |
| `dec_mnemonic`          | Decode a mnemonic phrase to the original encryption key                         |
| **8. User Actions**     |                                                                               |
| `lout`                  | Logout                                                                          |
| `exit`                  | Terminate MIRA                                                                  |
| `reset`                 | Delete all data, including the user account permanently (Be cautious!)         |

## Security Recommendations

- Regularly check for password expiration using the Listing and Analysis commands above.
- Keep your master password and encryption key secure.
- Enable Two-Factor Authentication for an additional layer of security.
- Mira operates on a Zero-Knowledge basis, which means that the security of your account relies solely on the strength and secrecy of your master password, without any involvement from the service provider. So, it's essential not to compromise your account's security with careless actions. Don't be a bitch!

## Note

- Master Password strength policy requires at least 15 characters with uppercase, numbers, and special characters. (Mandatory).
- Password strength policy for platforms requires at least 10 characters with uppercase, numbers, and special characters also. (Optional, but we recommend you to follow our password policy.)

## License

Mira is licensed under **GNU General Public License v3.0**

## Acknowledgements

- veilwr4ith
- icode3rror

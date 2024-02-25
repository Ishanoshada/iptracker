
# IPTracker


IPTracker is a versatile Python library and service that allows you to track and analyze IP addresses, providing valuable insights into user activity and location.

## Features

- **User Account Management:** Easily create and manage user accounts to track IP addresses.
- **Secure Authentication:** Password-protected accounts ensure secure access to tracking data.
- **Generate Tracking Links:** Generate unique tracking links to monitor user interactions.
- **IP Location Lookup:** Retrieve detailed information about the geographical location of IP addresses.
- **Real-Time Data Processing:** Continuously monitor and process IP tracking data in real-time.
- **Customizable Settings:** Tailor settings to your preferences, including location tracking and data processing intervals.

## Installation

You can install IPTracker via pip:

```bash
pip install iptracker
```

## Usage

```python
from iptracker import IPTracker

# Initialize IPTracker with your credentials
username = "your_username"
password = "your_password"
redirect_url = "/"
tracker = IPTracker(username, password, redirect_url)

# Create an account
# print(tracker.create_account())

# Login
# print(tracker.login())

# Generate a tracking link
tracking_link = tracker.generate_link()
print("Tracking Link:", tracking_link)

# Retrieve data from the tracking link
# Replace the example URL with your generated tracking link
# tracker.link_data("https://xxxxxxxx.com/link/your_tracking_key")
```

## Example

Check out this example to see how IPTracker can be used to monitor user interactions:

```python
from iptracker import IPTracker

# Initialize IPTracker with your credentials
username = "your_username"
password = "your_password"
redirect_url = "https://github.com/Ishanoshada/iptracker/"
tracker = IPTracker(username, password, redirect_url,location=True)

# Create an account
# print(tracker.create_account())

# Login
# print(tracker.login())

# Generate a tracking link
tracking_link = tracker.generate_link()
print("Tracking Link:", tracking_link)

# Retrieve data from the tracking link
# Replace the example URL with your generated tracking link
tracker.link_data(tracking_link)
"""Processing Link Data...


IP: 127, Timestamp: Thu, 22 Feb 2024 12:05:48, User Agent: Mozilla/5.0 (Linux; 37.36

IP Information:
IP Address: 1..237
City: 
Region: 
Country: 
Location: 6.65
Organization: AS180a PLC.
Postal Code: 
Timezone: Asi

"""

```

```python
from iptracker import main

main() #interface
"""
Here's how you can interact with the improved IP Tracker script:

1. Run the script.
2. Enter your credentials when prompted (username, password, redirect URL).
3. Choose options from the menu:

    - **Create Account (1)**: Creates an account with the provided credentials.
    - **Login (2)**: Logs into the account.
    - **Generate Link (3)**: Generates a tracking link.
    - **Track Link Data (4)**: Tracks data for a specific link.
    - **Exit (5)**: Exits the program.

Example interaction:

                                   

Welcome to the IP Tracker!
Please enter your credentials:
Username: my_username
Password: my_password
Redirect URL: https://example.com
Do you want to track IP location? (Y/N): Y

Menu:
1. Create Account
2. Login
3. Generate Link
4. Track Link Data
5. Exit
Enter your choice (1-5): 3
Generated link: https://bbbbbbbb-three.vercel.app/link/123456

Menu:
1. Create Account
2. Login
3. Generate Link
4. Track Link Data
5. Exit
Enter your choice (1-5): 4
Enter the link URL: https://bbbbbbbb-three.vercel.app/link/123456

Processing Link Data...
IP: 123.456.789.0, Timestamp: 2024-02-25 12:34:56, User Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.9000.0 Safari/537.36

IP Information:
IP Address: 123.456.789.0
City: CityName
Region: RegionName
Country: CountryName
Location: Latitude, Longitude
Organization: OrganizationName
Postal Code: PostalCode
Timezone: TimezoneName

Menu:
1. Create Account
2. Login
3. Generate Link
4. Track Link Data
5. Exit
Enter your choice (1-5): 5
Exiting program...

This example demonstrates creating an account, generating a tracking link, and tracking data for that link. You can explore other options similarly.
"""



```

## Contributing

We welcome contributions from the community! Feel free to submit bug reports, feature requests, or pull requests to help improve IPTracker.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact us at Ishan.kodithuwakku.official@gmail.com

**Repository Views** ![Views](https://profile-counter.glitch.me/iplogger/count.svg)




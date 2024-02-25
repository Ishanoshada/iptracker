import requests
import json
import time
import os
import random 
import re



links = ["https://bbbbbbbb-three.vercel.app/", "https://aaaaaaaaaaaaaaa-sigma.vercel.app"]


class IPTracker:
    MIN_USERNAME_LENGTH = 4
    MIN_PASSWORD_LENGTH = 6

    def __init__(self, username, password, redirect_url, location=False):
        self.base_url = os.environ.get("IPTRACKER_BASE_URL", random.choice(links))
        self.username = username
        self.password = password
        self.redirect_url = redirect_url
        self.location = location 

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if len(value) < self.MIN_USERNAME_LENGTH:
            raise ValueError(f"Username must be at least {self.MIN_USERNAME_LENGTH} characters long.")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < self.MIN_PASSWORD_LENGTH:
            raise ValueError(f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters long.")
        self._password = value

    def _send_post_request(self, endpoint, payload):
        headers = {'Content-Type': 'application/json'}
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=payload, headers=headers, verify=True)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
            
    def get_ip_location(self, ip_address):
        url = f"http://ipinfo.io/{ip_address}/json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching IP location: {e}")
            return None
    
    def print_ip_info(self, ip_info):
        print("IP Information:")
        print(f"IP Address: {ip_info['ip']}")
        print(f"City: {ip_info['city']}")
        print(f"Region: {ip_info['region']}")
        print(f"Country: {ip_info['country']}")
        print(f"Location: {ip_info['loc']}")
        print(f"Organization: {ip_info['org']}")
        print(f"Postal Code: {ip_info['postal']}")
        print(f"Timezone: {ip_info['timezone']}")

    def create_account(self):
        endpoint = "create_account"
        payload = {"username": self.username, "password": self.password}
        return self._send_post_request(endpoint, payload)

    def login(self):
        endpoint = "login"
        payload = {"username": self.username, "password": self.password}
        return self._send_post_request(endpoint, payload)

    def generate_link(self):
        endpoint = "generate_link"
        payload = {"username": self.username, "password": self.password, "redirect_url": self.redirect_url}
        try:
            response_data = self._send_post_request(endpoint, payload)
            if response_data:
                return random.choice(links) + str(response_data["link"])
            else:
                print("Failed to generate link.")
                return None
        except:
            print("Error occurred while generating link.")
            return None

    def link_data(self, url):
        match = re.search(r'/link/(\w+)', url)
        if not match:
            print("Invalid URL format. Please provide a valid URL.")
            return
        key = match.group(1)
        endpoint = f"link_data/{key}"
        payload = {"username": self.username, "password": self.password}
        while True:
            try:
                response = requests.post(f"{self.base_url}/{endpoint}", json=payload, verify=True)
                response.raise_for_status()
                data = response.json()
                self.process_link_data(data)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
            time.sleep(5)

    def process_link_data(self, data):
        print("\nProcessing Link Data...")
        data = str(data)
        ips = re.findall(r"'ip': '(.*?)'", data)
        timestamps = re.findall(r"'timestamp': '(.*?) GMT'", data)
        user_agents = re.findall(r"'user_agent': '(.*?)'", data)

        for ip, timestamp, user_agent in zip(ips, timestamps, user_agents):
            print(f"\n\nIP: {ip}, Timestamp: {timestamp}, User Agent: {user_agent}\n")
            if self.location:
                location_info = self.get_ip_location(ip)
                if location_info:
                    self.print_ip_info(location_info)


def main():

    print("Welcome to the IP Tracker!")
    print("Please enter your credentials:")
    username = input("Username: ")
    password = input("Password: ")
    redirect_url = input("Redirect URL: ")
    location = input("Do you want to track IP location? (Y/N): ").lower() == 'y'
    
    tracker = IPTracker(username, password, redirect_url, location)
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Login")
        print("3. Generate Link")
        print("4. Track Link Data")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            if tracker.create_account():
                print("Account created successfully.")
        elif choice == '2':
            if tracker.login():
                print("Login successful.")
        elif choice == '3':
            generated_link = tracker.generate_link()
            if generated_link:
                print("Generated link:", generated_link)
        elif choice == '4':
            url = input("Enter the link URL: ")
            tracker.link_data(url)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


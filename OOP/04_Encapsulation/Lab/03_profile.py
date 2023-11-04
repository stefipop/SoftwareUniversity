class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @username.setter
    def username(self, value: str) -> None:
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @password.setter
    def password(self, value) -> None:
        is_valid_length = len(value) >= 8
        is_upper_case_present = any(char.isupper() for char in value)
        is_digit_present = any(char.isdigit() for char in value)

        if is_digit_present and is_upper_case_present and is_valid_length:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

# profile_with_invalid_password = Profile('My_username', 'My-password')

# profile_with_invalid_username = Profile('Too_long_username', 'Any')

# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)

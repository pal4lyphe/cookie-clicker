import time

class CookieClicker:
    def __init__(self):
        self.cookies = 0
        self.cps = 0  # Cookies per second
        self.upgrades = 0
        self.is_playing = True

    def click(self):
        """Simulate a click event to increase cookies."""
        self.cookies += 1
        print(f"You clicked! Total cookies: {self.cookies}")

    def buy_upgrade(self):
        """Buy an upgrade if cookies are enough."""
        upgrade_cost = 10 * (self.upgrades + 1)
        if self.cookies >= upgrade_cost:
            self.cookies -= upgrade_cost
            self.upgrades += 1
            self.cps += 1
            print(f"Upgrade purchased! Cookies per second increased to {self.cps}")
        else:
            print("Not enough cookies for an upgrade!")

    def run(self):
        """Start the main game loop."""
        while self.is_playing:
            print(f"\nTotal cookies: {self.cookies} | Cookies per second: {self.cps} | Upgrades: {self.upgrades}")
            print("1. Click (Earn 1 cookie)")
            print("2. Buy Upgrade (Increase CPS)")
            print("3. Exit Game")
            choice = input("Choose an action: ")

            if choice == "1":
                self.click()
            elif choice == "2":
                self.buy_upgrade()
            elif choice == "3":
                print("Exiting game...")
                self.is_playing = False
            else:
                print("Invalid choice! Please choose again.")

            # Simulate the passage of time for cookies to accumulate
            time.sleep(1)
            self.cookies += self.cps  # Add cookies based on CPS

if __name__ == "__main__":
    game = CookieClicker()
    game.run()

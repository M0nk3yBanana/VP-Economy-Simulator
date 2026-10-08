import time

class RepublicMember:
    """
    A class to represent a member of The Republic.
    Tracks their Valor Points (VP) and contribution status.
    """
    def __init__(self, username, initial_vp=0):
        self.username = username
        self.vp = initial_vp
        self.last_contribution_time = time.time()
        self.is_active = True

    def earn_vp(self, amount, reason):
        """Earn VP through Quests or Raids."""
        if amount <= 0:
            print("Error: VP amount must be positive.")
            return
        
        self.vp += amount
        self.last_contribution_time = time.time()
        print(f"[+] {self.username} earned {amount} VP for: {reason}. Total VP: {self.vp}")

    def apply_decay(self, decay_rate=0.01):
        """
        Simulate VP decay for inactivity.
        Consistent contribution matters more than raw presence.
        """
        # For simulation purposes, we'll assume 1 decay cycle = 1 call
        decay_amount = self.vp * decay_rate
        self.vp -= decay_amount
        print(f"[-] {self.username} lost {decay_amount:.2f} VP due to inactivity. Remaining VP: {self.vp:.2f}")

    def get_status(self):
        return f"User: {self.username} | Status: {'Active' if self.is_active else 'Inactive'} | VP: {self.vp:.2f}"


def simulate_economy():
    print("=== The Homeland: VP Economy Simulation ===\n")
    
    # 1. Create Members
    member1 = RepublicMember("break_freak", 100)
    member2 = RepublicMember("all37doteth", 50)
    
    print("Initial State:")
    print(member1.get_status())
    print(member2.get_status())
    print("-" * 40)

    # 2. Simulate Earning VP (Quests & Raids)
    print("\nSimulating Contributions (Quests & Raids):")
    member1.earn_vp(75, "Completed 'The Path of Honors' Quest")
    member2.earn_vp(50, "Participated in a Community Raid")
    member1.earn_vp(25, "Helped another squad member")
    print("-" * 40)

    # 3. Simulate Decay (Inactivity)
    print("\nSimulating Periods of Inactivity (Decay):")
    print("Member 2 (all37doteth) goes inactive for a cycle...")
    member2.apply_decay(decay_rate=0.05) # 5% decay for demonstration
    print("Member 1 (break_freak) continues to contribute...")
    member1.earn_vp(10, "Daily engagement")
    print("-" * 40)

    # 4. Final State
    print("\nFinal State:")
    print(member1.get_status())
    print(member2.get_status())
    
    print("\nConclusion: Consistent contribution (break_freak) outpaces raw presence (all37doteth).")

if __name__ == "__main__":
    simulate_economy()

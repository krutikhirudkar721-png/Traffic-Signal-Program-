ch = input("Enter traffic light color: ").strip().capitalize()
        match ch:
            case "Red":
                print("🛑 STOP!!!")
            case "Green":
                print("🟢 GO")
            case "Orange" | "Yellow":  # Handles both common terms for the middle light
                print("🟠 BE READY...")
            case _:
                print("❌ Invalid choice")
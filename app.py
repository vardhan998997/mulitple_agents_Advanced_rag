
from core.coordinator import ResearchCoordinator

if __name__ == "__main__":
    query = input("Enter research query: ")

    coordinator = ResearchCoordinator()
    report = coordinator.run(query)

    print("\n===== FINAL REPORT =====\n")
    print(report)

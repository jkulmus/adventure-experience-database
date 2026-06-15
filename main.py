import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Connect to Firebase using the private service account key.
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Create Firestore database connection.
db = firestore.client()


def add_categories():
    """Add category documents to Firestore."""

    db.collection("categories").document("relaxing").set({
        "name": "Relaxing",
        "description": "Calm, peaceful, and low-stress experiences."
    })

    db.collection("categories").document("adventure").set({
        "name": "Adventure",
        "description": "Active, exciting, and challenge-based experiences."
    })

    db.collection("categories").document("fantasy").set({
        "name": "Fantasy",
        "description": "Story-driven and immersive themed experiences."
    })

    print("Categories added successfully!")


def add_experiences():
    """Add adventure experience documents connected to categories."""

    db.collection("experiences").document("experience1").set({
        "title": "Lakeside Cabin Weekend",
        "mood": "relaxing",
        "group": "family",
        "category_id": "relaxing",
        "description": "A calm family trip with cozy cabins and lake activities."
    })

    db.collection("experiences").document("experience2").set({
        "title": "Mountain Challenge Course",
        "mood": "adventure",
        "group": "solo",
        "category_id": "adventure",
        "description": "A solo adventure with hiking, obstacles, and personal challenges."
    })

    db.collection("experiences").document("experience3").set({
        "title": "Guild Adventure Weekend",
        "mood": "fantasy",
        "group": "friends",
        "category_id": "fantasy",
        "description": "A fantasy group experience with teamwork, quests, and immersive challenges."
    })

    print("Experiences added successfully!")


def view_categories():
    """Retrieve and display all categories from Firestore."""

    categories = db.collection("categories").stream()

    print("\nCurrent Categories:")

    for category in categories:
        print(f"\nID: {category.id}")
        print(category.to_dict())


def view_experiences():
    """Retrieve and display all adventure experiences from Firestore."""

    experiences = db.collection("experiences").stream()

    print("\nCurrent Experiences:")

    for experience in experiences:
        print(f"\nID: {experience.id}")
        print(experience.to_dict())


def update_experience():
    """Update an existing adventure experience document in Firestore."""

    db.collection("experiences").document("experience1").update({
        "title": "Updated Lakeside Cabin Weekend",
        "description": "An updated relaxing family getaway with cabins, trails, and lake activities."
    })

    print("\nExperience updated successfully!")


def delete_experience():
    """Delete an adventure experience document from Firestore."""

    db.collection("experiences").document("experience2").delete()

    print("\nExperience deleted successfully!")


def run_demo():
    """Run a complete cloud database CRUD demonstration."""

    print("=====================================")
    print(" Adventure Experience Database Manager")
    print("=====================================")

    print("\nConnecting to Firestore...")
    print("Connected to Firestore successfully!")

    print("\nCREATE CATEGORY COLLECTION")
    add_categories()

    print("\nCREATE EXPERIENCE COLLECTION")
    add_experiences()

    print("\nREAD CATEGORIES")
    view_categories()

    print("\nREAD EXPERIENCES")
    view_experiences()

    print("\nUPDATE EXPERIENCE")
    update_experience()

    print("\nREAD AFTER UPDATE")
    view_experiences()

    print("\nDELETE OPERATION")
    delete_experience()

    print("\nREAD AFTER DELETE")
    view_experiences()

    print("\n=====================================")
    print(" End of Demo")
    print("=====================================")


run_demo()
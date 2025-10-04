import sys
print("Python is running...")

try:
    print("Importing database...")
    from database import engine
    print("✅ Database imported")
    
    print("Importing models...")
    from models import Base
    print("✅ Models imported")
    
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created!")
    
    # Verify tables exist
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(f"✅ Tables in database: {tables}")
    
except Exception as e:
    print(f"❌ Error occurred: {e}")
    import traceback
    traceback.print_exc()
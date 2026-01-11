

USER = "admin"  

def admin_required(func):

    def inner(*args, **kwargs):
        if USER != "admin":
            raise PermissionError("Admin access required!")
        return func(*args, **kwargs)
    return inner

@admin_required
def database():
    return "Database Found!"



print(database())
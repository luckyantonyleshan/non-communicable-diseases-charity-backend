def user_schema(user):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
    }

def case_schema(case):
    return {
        "id": case.id,
        "title": case.title,
        "description": case.description,
        "status": case.status,
        "user_id": case.user_id
    }

def donation_schema(donation):
    return {
        "id": donation.id,
        "amount": donation.amount,
        "date": donation.date.isoformat(),
        "user_id": donation.user_id
    }

def resource_schema(resource):
    return {
        "id": resource.id,
        "name": resource.name,
        "description": resource.description,
        "quantity": resource.quantity,
        "case_id": resource.case_id
    }

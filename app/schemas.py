def user_schema(user):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }

def case_schema(case):
    return {
        "id": case.id,
        "title": case.title,
        "description": case.description,
        "user_id": case.user_id
    }

def donation_schema(donation):
    return {
        "id": donation.id,
        "amount": donation.amount,
        "donor_name": donation.donor_name,
        "user_id": donation.user_id
    }

def resource_schema(resource):
    return {
        "id": resource.id,
        "title": resource.title,
        "url": resource.url
    }
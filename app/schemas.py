def user_schema(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    }

def case_schema(case):
    return {
        'id': case.id,
        'title': case.title,
        'description': case.description,
        'amount_needed': case.amount_needed,
        'amount_received': case.amount_received,
        'user_id': case.user_id
    }

def donation_schema(donation):
    return {
        'id': donation.id,
        'amount': donation.amount,
        'donor_name': donation.donor_name,
        'user_id': donation.user_id,
        'case_id': donation.case_id,
        'area_id': donation.area_id
    }

def resource_schema(resource):
    return {
        'id': resource.id,
        'title': resource.title,
        'url': resource.url
    }

def disease_schema(disease):
    return {
        'id': disease.id,
        'name': disease.name,
        'description': disease.description,
        'prevalence': disease.prevalence,
        'created_at': disease.created_at.isoformat()
    }

def area_schema(area):
    return {
        'id': area.id,
        'name': area.name,
        'description': area.description,
        'latitude': area.latitude,
        'longitude': area.longitude,
        'created_at': area.created_at.isoformat()
    }

def review_schema(review):
    return {
        'id': review.id,
        'content': review.content,
        'user_id': review.user_id,
        'disease_id': review.disease_id,
        'area_id': review.area_id,
        'created_at': review.created_at.isoformat()
    }
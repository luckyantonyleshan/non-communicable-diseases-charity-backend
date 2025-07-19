import app.extensions

donation_case = app.extensions.db.Table('donation_case',
    app.extensions.db.Column('donation_id', app.extensions.db.Integer, app.extensions.db.ForeignKey('donation.id')),
    app.extensions.db.Column('case_id', app.extensions.db.Integer, app.extensions.db.ForeignKey('case.id'))
)
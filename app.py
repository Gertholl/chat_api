from database.db_config import create_app, db
from routes.routes import *
# from routes.routes import init_api


app = create_app()

if __name__ == '__main__':
   
    db.create_all(app=app)
    init_api(app, db)
    app.run(debug=False, port=9000)

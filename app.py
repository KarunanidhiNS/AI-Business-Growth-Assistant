from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from routes.home_routes import home_bp
from routes.analysis_routes import analysis_bp
from routes.report_routes import report_bp

app.register_blueprint(home_bp)
app.register_blueprint(analysis_bp)
app.register_blueprint(report_bp)

if __name__ == "__main__":
    app.run(debug=True)
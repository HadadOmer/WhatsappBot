if [ -f .env ]; then
    export $(cat .env | xargs)
fi

PYTHONDONTWRITEBYTECODE=1 gunicorn --workers 1 --timeout 180 -b 0.0.0.0:$APP_PORT src.app:app
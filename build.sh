PATH_NAME=$(pwd)
POETRY_ENV_PATH=$(poetry env info -p)

cd $POETRY_ENV_PATH/lib/python3.8/
zip -r9  $PATH_NAME/lambda.zip .
cd $PATH_NAME
zip -g lambda.zip lambda_function.py
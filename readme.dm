proyecto mecanica

INSTALAR entorno virtual
python -m venv venv

1
.\venv\Scripts\activate  

1.1
pip  install requirements.txt

2
cd principal        

3
python manage.py makemigrations

4 
python manage.py migrate

5
python manage.py runserver




-----  EJECUSION DE LA MIGRACION-----

python manage.py makemigrations Login
python manage.py migrate Login


python manage.py makemigrations TiposGarantias
python manage.py migrate TiposGarantias


python manage.py makemigrations Garantias
python manage.py migrate Garantias


python manage.py makemigrations Vehiculo
python manage.py migrate Vehiculo
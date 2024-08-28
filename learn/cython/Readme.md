python3 -m venv cython_env
source cython_env/bin/activate
source cython_env/bin/activate
mkdir my_first_cython
cd my_first_cython/
pip install Cython
python setup.py build_ext --inplace

extraer 7z
```sh
7z x xtest.7z.001
7z x xtrain.7z.001
```
```sh
conda create -n tf_env python=3.10
conda activate tf_env
```
```sh
pip install tensorflow
```
```sh
conda install -c conda-forge tensorflow
```
##### Jupyter Notebook
```sh
pip install notebook
pip install jupyterlab
sudo ufw allow 8888
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser 
```

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
##### Jupyter Notebook WINDOWS
```sh
conda create -n env_iaa4 python=3.8 -y
conda activate env_iaa4
conda install pip -y
conda install tensorflow-gpu -y
pip install -r requirements.txt
pip install notebook
pip install jupyterlab
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser 
```
o pytorch GPU
```sh
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```
entornos conda
```sh
conda env list
conda remove --name env_iaa --all -y
```
.7z
```sh
pip install py7zr -y
```
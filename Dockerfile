# Update pip requirements for python

# Run cmd
#   docker build -t registry.cn-hangzhou.aliyuncs.com/mengjieguo/businessappointment:20.03.06 .
# docker push cmd
#   docker push registry.cn-hangzhou.aliyuncs.com/mengjieguo/businessappointment:20.03.06

FROM  python:3.6

# 设置容器镜像时区
ENV TZ=Asia/Shanghai
# 设置字符编码
ENV LANG=C.UTF-8
# 拷贝依赖文件
COPY requirements.txt /home/
# 设置代理、安装依赖、删除缓存
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/  \
    &&  pip install --upgrade pip  \
#    &&  pip install wheel  \
    &&  pip install -r /home/requirements.txt  #--wheel-dir=/pippacks/wheels \
#    &&  pip wheel gunicorn --wheel-dir=/pippacks/wheels \
#    &&  rm -rf /pippacks/wheels \
#    &&  rm -rf /root/.cache \
#    &&  rm -rf .build-deps

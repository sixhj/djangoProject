
.PHONY: base-image
# 安装依赖
install-dep:
	pip install -r requirements.txt

# 导出依赖文件
export-requirements:
	pip freeze > requirements.txt

# 构建基础镜像
build-base-image:
	docker build -t hello:v0118 .

# 启动
docker-compose-run:
	docker-compose up



 # 生成变更文件
makemigrations:
	python manage.py makemigrations


# 修改数据库
migrate	:
	python manage.py migrate

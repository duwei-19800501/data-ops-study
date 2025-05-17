FROM docker.1ms.run/python:3.8-slim
WORKDIR app
COPY . .
RUN pip install --no-cache-dir \
    -i https://pypi.tuna.tsinghua.edu.cn/simple \
    --trusted-host pypi.tuna.tsinghua.edu.cn \
    pytest pandas
ENV PYTHONPATH=/app
CMD ["python", "-m", "pytest", "tests/", "-v"]
FROM ollama/ollama as stablelm2
RUN ollama serve & sleep 1 && ollama pull stablelm2:1.6b-zephyr-q2_K && chmod -R 777 /root/.ollama
FROM public.ecr.aws/lambda/python:3.11
COPY --from=stablelm2 /usr/bin/ollama /root/.ollama /usr/bin/
COPY requirements.txt app.py ./
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt -t . && rm -rf /root/.cache
ENV HOME=/usr/bin
CMD ["app.lambda_handler"]

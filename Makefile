server:
	docker build -t kenlm-service .
	docker run -it -p 8000:8000 kenlm-service

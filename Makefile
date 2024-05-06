server:
	docker build -t kenlm-service .
	docker run -it -p 8000:8000 kenlm-service
test_req:
	python test_request.py
build_base:
	docker build -t kenlm-service_base -f base.dockerfile .
server:
	docker build -t kenlm-service .
	docker run -it -p 8000:8000 -v "/metadata0:/metadata0" kenlm-service
test_req:
	python test_request.py
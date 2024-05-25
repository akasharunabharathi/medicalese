# Medicalese
Ever felt confused by all the big words on the report from your blood tests? Wished someone would interpret those mysterious numbers and let you know if you're normal ASAP? Here's Medicalese – one tool to simplify it all for you! Upload snapshots of your reports, and receive super easy-to-understand explanations.

## Subsystems:

As of now, there are two primary subsystems to this project, (listed in the order that they process user input):

The OCR-Summarization Subsystem: This is responsible for recognising the text from the reports (contains report text, details of patient's lab work, measurements of blood markers for various functions, etc) that users pass in, and summarizing the report. This is also the first layer where we encounter user input for processing. Uses the Tesseract-OCR engine and Falaconsai's Medical Summarization Model.

The Explainer Subsytem: Takes the input from the OCR-Summarization engine and simplifies it down for users. Yay! Uses Llama-3.

## The UI
<img width="1428" alt="Screen Shot 2024-05-13 at 11 34 38 AM" src="https://github.com/akasharunabharathi/medicalese/assets/90937878/b013f823-83c7-4d25-8d7b-fde6d336b36c">

## Example Report (Generated using ChatGPT)
<img width="546" alt="Sample Report (1)" src="https://github.com/akasharunabharathi/medicalese/assets/90937878/85f685a4-0e24-4617-8974-6d29fadbbfa5">

## Example Interpretation - From V1, V2 coming soon
<img width="1363" alt="Screen Shot 2024-01-04 at 6 07 49 PM" src="https://github.com/akasharunabharathi/medicalese/assets/90937878/f500e225-3453-42b9-9369-2c567fb51831">

# V3

So, for version 3, I decided to implement the UI and host the service myself instead of using Gradio. I built a crude replica of the Gradio frontend with React, TypeScript and NextJS. Admittedly, I didn't leverage all that NextJS had to offer since I didn't really need routing for this project.
<img width="1440" alt="Screen Shot 2024-05-25 at 6 01 34 PM" src="https://github.com/akasharunabharathi/medicalese/assets/90937878/275a7883-c1fa-4779-96c4-c2da3641fcbb">

For the backend, I decided to deploy on Kubernetes with EC2 instances. To avoid prohibitive costs for experimenting and an awful UX because of the load time, I didn't load in Llama-3 for the explainer module. Instead this was more of an exercise in mangaing all the resources required for an ML app demo myself from A-Z. These were the steps I followed:

• Create a private repo in AWS ECR. You can use the CLI, I did it with the console.
• `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <my-aws-repo-url>` – for authenticating your Docker client to push to your AWS ECR repo
• I'm running my Docker Daemon on an M1 MacBook Air, which builds Docker images for an ARM architecture. However, EC2 instances use x86, so my images were initially incompatible with the systems I was trying to deploy my containers on. To resolve this:
  • `docker buildx creeate --name mybuilder --use`
  • `docker buildx inspect --bootstrap`
  • `docker buildx build --platform linux/amd64 -t <my-repo-url>/<my-image-name>:<tag> . --push` – in my case, my image name was `medicalese-backend` and the tag was `0.5.0` (it was the sicth image I'd cretaed, all images `latest`, `0.1.0` - `0.4.0` failed to deploy with `kubectl`, which I'll come to below)
  • `eksctl create cluster` specify parameters as needed. I deployed on `t3.medium` EC2 instances in `us-east-1a` and `us-east-1b` (apparently some availability zones don't have EKS support, and you need to be running in at least two availaibilty zones that do offer support this)
  • `kubectl apply -f deployment.yaml`
  • `kubectl get pods` – check if your pods are alive
  • `kubectl apply -f load_balancer.yaml` – copy the public url of the loadbalancer, this is what we'll `POST` to from the UI when a user clicks `Upload`

Tada!!!

# Bug Fixes and Future Experiments
• Requires error handling for model loading in `bio_summarize.py`.

• Explore using Serverless Inference API for Llama-3 instead of loading it locally using the `Transformers` library.

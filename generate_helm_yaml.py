"""
Generates a basic Helm-compatible Kubernetes Deployment YAML
for a Node.js app and writes it to 'node-app-deploy.yaml'.
"""

def generate_helm_yaml():
    content = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: node-app
  template:
    metadata:
      labels:
        app: node-app
    spec:
      containers:
        - name: node
          image: node:18
          ports:
            - containerPort: 3000
"""
    with open("node-app-deploy.yaml", "w") as f:
        f.write(content)
    print("✅ Generated 'node-app-deploy.yaml' successfully.")

if __name__ == "__main__":
    generate_helm_yaml()

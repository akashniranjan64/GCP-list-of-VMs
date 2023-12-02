FROM alpine:latest
ENV TERRAFORM_VERSION="0.15.5"
ENV CLOUD_SKD_VERSION="415.0.0"


# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add -U tar gzip curl git jsonnet yq jq

# gcloud
RUN mkdir -p /google-cloud-sdk && \
    curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SKD_VERSION}-linux-x86_64.tar.gz | tar xvz -C / && /google-cloud-sdk/install.sh
RUN ln -s /google-cloud-sdk/bin/* /usr/bin/.

# Terraform
RUN wget https://releases.hashicorp.com/terraform/0.15.5/terraform_0.15.5_linux_amd64.zip && \
    unzip terraform_0.15.5_linux_amd64.zip -d /usr/bin && \
    rm terraform_0.15.5_linux_amd64.zip

#TFLINT
RUN curl -k -LO https://github.com/terraform-linters/tflint/releases/download/v0.45.0/tflint_linux_amd64.zip && \
    unzip tflint_linux_amd64.zip -d /usr/bin && \
    rm tflint_linux_amd64.zip


ENTRYPOINT ["/bin/sh", "-l", "-c" ]
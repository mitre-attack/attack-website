FROM ubuntu:19.10
COPY . /home/attackuser/attack-website
LABEL maintainer="Jeff Li"
LABEL description="Dockerfile for the ATT&CK Website Image"

ENV DEBIAN_FRONTEND noninteractive

# *********** Install Prerequisites ***************
# -qq : No output except for errors
RUN apt-get update --fix-missing \
  && apt-get install -qqy --no-install-recommends \
  locales nano sudo git pelican apt-transport-https ca-certificates python3-pip python3-setuptools \
  # ********** Set Locale **********************
  && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
  && locale-gen \
  && update-ca-certificates \
  && python3 -m pip install wheel \
  && cd /home/attackuser \
  && cd /home/attackuser/attack-website \
  && python3 -m pip install -r requirements.txt

  WORKDIR /home/attackuser/attack-website

  RUN python3 update-attack.py -c -b

  WORKDIR /home/attackuser/attack-website/output

  CMD ["python3", "-m", "pelican.server", "80"]
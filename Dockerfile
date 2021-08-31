FROM ubuntu:20.04
COPY . /home/attackuser/attack-website
# label metadata
LABEL name="attack-website"
LABEL description="Dockerfile for the ATT&CK Website"
LABEL usage="https://github.com/mitre-attack/attack-website/blob/master/README.md#install-and-build"
LABEL url="https://attack.mitre.org/"
LABEL vcs-url="https://github.com/mitre-attack/attack-website"
LABEL vendor="MITRE ATT&CK"
LABEL maintainer="attack@mitre.org"

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

  RUN python3 update-attack.py --no-test-exitstatus

  WORKDIR /home/attackuser/attack-website/output

  CMD ["python3", "-m", "pelican.server", "80"]
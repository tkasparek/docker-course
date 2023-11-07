from ubuntu

ENV ORG=""
ENV PAT=""
ENV POOL=""

RUN apt-get update && apt-get install -y curl git && apt-get clean

RUN adduser --home /agent azdo

WORKDIR /agent

USER azdo

RUN  curl -s https://vstsagentpackage.azureedge.net/agent/3.227.2/vsts-agent-linux-x64-3.227.2.tar.gz | tar xz

USER root

RUN /agent/bin/installdependencies.sh

USER azdo

ENTRYPOINT /agent/config.sh --unattended --url https://dev.azure.com/$ORG --auth pat --token $PAT --pool $POOL --agent $HOSTNAME --acceptTeeEula && /agent/run.sh

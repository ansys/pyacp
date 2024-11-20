docker pull ghcr.io/ansys/pydpf-composites:latest
docker pull ghcr.io/ansys/mapdl:latest

if (-not [Environment]::GetEnvironmentVariable('ANSYSLMD_LICENSE_FILE', 'Machine'))
{
    ">> ANSYSLMD_LICENSE_FILE is not set. Use it if the license server is not otherwise defined."
    "   Exampel: $Env:ANSYSLMD_LICENSE_FILE='1055@my_license_server'"
}

$Env:ANSYS_DPF_ACCEPT_LA="Y"
$Env:PYMAPDL_PORT=59991
$Env:PYMAPDL_START_INSTANCE="FALSE"
$Env:PYDPF_COMPOSITES_DOCKER_CONTAINER_PORT=59992
$Env:SPHINXOPT_NITPICKY=0
# whether to skip the gallery (examples)
$Env:PYACP_DOC_SKIP_GALLERY=0
# whether to skip the API documentation
$Env:PYACP_DOC_SKIP_API=0

docker-compose -f ./docker-compose/docker-compose-extras.yaml up -d

cd doc
.\make.bat html
cd ..
docker-compose -f ./docker-compose/docker-compose-extras.yaml down

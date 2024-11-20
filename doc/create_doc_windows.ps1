if ($Env:ANSYSLMD_LICENSE_FILE -ne $null)
{
    "ANSYSLMD_LICENSE_FILE=" + $Env:ANSYSLMD_LICENSE_FILE
}
else
{
    "Env variable 'ANSYSLMD_LICENSE_FILE' is required for the license checks."
    "Example: ANSYSLMD_LICENSE_FILE='1055@my_license_server'"
    exit 1
}

docker pull ghcr.io/ansys/pydpf-composites:latest
docker pull ghcr.io/ansys/mapdl:latest

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

import pytest
from algokit_utils import (
    ApplicationClient,
    ApplicationSpecification,
    get_localnet_default_account,
)
from algosdk.v2client.algod import AlgodClient

from smart_contracts.biogas import contract as biogas_contract


@pytest.fixture(scope="session")
def biogas_app_spec(algod_client: AlgodClient) -> ApplicationSpecification:
    return biogas_contract.app.build(algod_client)


@pytest.fixture(scope="session")
def biogas_client(
    algod_client: AlgodClient, biogas_app_spec: ApplicationSpecification
) -> ApplicationClient:
    client = ApplicationClient(
        algod_client,
        app_spec=biogas_app_spec,
        signer=get_localnet_default_account(algod_client),
        template_values={"UPDATABLE": 1, "DELETABLE": 1},
    )
    client.create()
    return client


def test_says_hello(biogas_client: ApplicationClient) -> None:
    result = biogas_client.call(biogas_contract.hello, name="World")

    assert result.return_value == "Hello, World"

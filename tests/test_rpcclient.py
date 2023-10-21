from mccore import RPCClient


def test_client_initialization():
    client = RPCClient()
    assert client is not None
    assert client.connection is not None
    assert client.channel is not None
    client.close_connection()


def rpc_client_call():
    client = RPCClient()
    response = client.call('test_queue', 'test_message')
    assert response is not None
    assert response == 'test_response'
    client.close_connection()


def test_hello_svc_without_param(hello_svc_client):
    """
    Given: hello svc running on cluster
    And: I have cluster ip address
    And: I have service port
    When: I do a get call
    Then: I should get back 200 Ok
    And: I should get back string Hi there, !"
    """
    status, response = hello_svc_client.get()
    assert status == 200
    assert response == f"Hi there, !"



def test_hello_svc_with_param(hello_svc_client):
    """
    Given: hello svc running on cluster
    And: I have cluster ip address
    And: I have service port
    When: I do a get call with string parameter
    Then: I should get back 200 Ok
    And: I should get back string  Hi there, <param>!"

    """
    name = "pradeep"
    status, response = hello_svc_client.get(name=name)
    assert status == 200
    assert response == f"Hi there, {name}!"
import jsons

from clients.data_classes.reponse_data_classes import SBDBCloseApproachResponse


def test_default_query_params_setup_for_search(sbdb_close_approach_data_client):
    """
    Defaults for query parameters are setup for a typical CNEOS web-site search:
    NEO Earth close-approaches less than 0.05 au in the next 60 days sorted by date.

    Given: I want the NEO Earth close-approaches less than 0.05 au in the next 60 days sorted by date.atus

    And: I call the api.
    Then: I should get back data and 200 Ok Response.

    And: I call the api without any params.
    Then: I should get back data and 200 Ok Response.
    And: Data from both calls should match.

    """

    status, response = sbdb_close_approach_data_client.get()
    assert status == 200

    default_params_resp = jsons.load(response, cls=SBDBCloseApproachResponse)

    sbdb_close_approach_data_client.clear_all_query_param() # with no query params

    status, response = sbdb_close_approach_data_client.get()
    assert status == 200

    no_params_resp = jsons.load(response, cls=SBDBCloseApproachResponse)

    assert default_params_resp.count == no_params_resp.count
    assert default_params_resp.fields == no_params_resp.fields
    assert default_params_resp.data == no_params_resp.data


def test_name_in_field_list_when_body_is_set_to_all(sbdb_close_approach_data_client):
    """
    Given: I have close approach data client.
    And: I add body param with value "All".
    When: I make the call.
    Then: I should get back 200 Ok and body in fields list.
    """

    sbdb_close_approach_data_client.add_query_param(body="All")
    status, response = sbdb_close_approach_data_client.get()
    assert status == 200

    response_class_obj = jsons.load(response, cls=SBDBCloseApproachResponse)

    assert "body" in response_class_obj.fields

    sbdb_close_approach_data_client.add_query_param(body="Earth")
    status, response = sbdb_close_approach_data_client.get()
    assert status == 200

    response_class_obj = jsons.load(response, cls=SBDBCloseApproachResponse)
    assert "body" not in response_class_obj.fields
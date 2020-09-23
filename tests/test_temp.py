

def testfoo(sbdb_close_approach_data_client):
    status, response = sbdb_close_approach_data_client.get_close_approach_data()
    assert status == 200
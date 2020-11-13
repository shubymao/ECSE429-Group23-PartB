import requests
import json
from support.assertions import assert_valid_json_schema, assert_valid_dictionary_schema, \
    get_valid_dictionary_schema, get_valid_json_schema


def test_get_projects_return_code():
    r = requests.get(url="http://localhost:4567/projects")
    assert r.status_code == 200


def test_get_projects_return_payload():
    r = requests.get(url="http://localhost:4567/projects")
    assert assert_valid_json_schema(r.json(), 'projects.get.json')


def test_head_projects_return_code():
    r = requests.get(url="http://localhost:4567/projects")
    assert r.status_code == 200


def test_head_projects_return_payload():
    r = requests.head(url="http://localhost:4567/projects")

    try:
        r.json()
    except json.decoder.JSONDecodeError:
        assert True
        return
    assert False


def test_head_projects_headers():
    r = requests.head(url="http://localhost:4567/projects").headers
    assert r['Server'] == get_valid_dictionary_schema('projects.head.json')['Server'] and \
           r['Content-Type'] == get_valid_dictionary_schema('projects.head.json')['Content-Type'] and \
           r['Transfer-Encoding'] == get_valid_dictionary_schema('projects.head.json')['Transfer-Encoding']


def test_post_projects_return_code_without_id():
    body = get_valid_json_schema('projects.post.withoutid.json')
    r = requests.post(url="http://localhost:4567/projects", json=body)
    assert r.status_code == 201

def test_post_projects_return_code_with_id():
    body = get_valid_json_schema('projects.post.withid.json')
    r = requests.post(url="http://localhost:4567/projects", json=body)
    assert r.status_code == 400

def test_post_projects_return_payload_without_id():
    body = get_valid_json_schema('projects.post.withoutid.json')
    r = requests.post(url="http://localhost:4567/projects", json=body)
    assert r.json() == get_valid_json_schema('projects.post.withoutid.return_payload.json')

def test_post_projects_return_payload_with_id():
    body = get_valid_json_schema('projects.post.withid.json')
    r = requests.post(url="http://localhost:4567/projects", json=body)
    assert r.json() == get_valid_json_schema('projects.post.withid.return_payload.json')

def test_get_projects_id_existing_return_code():
    r = requests.get(url="http://localhost:4567/projects/1")
    assert r.status_code == 200

def test_get_projects_id_existing_return_payload():
    r = requests.get(url="http://localhost:4567/projects/1")
    assert r.json() == get_valid_json_schema('projects.id.get.existing.return_payload.json')

def test_get_projects_id_not_found_return_code():
    r = requests.get(url="http://localhost:4567/projects/55")
    assert r.status_code == 404

def test_get_projects_id_not_found_return_payload():
    r = requests.get(url="http://localhost:4567/projects/55")
    assert r.json() == get_valid_json_schema('projects.id.get.notfound.return_payload.json')

def test_head_projects_id_return_code():
    r = requests.head(url="http://localhost:4567/projects/1")
    assert r.status_code == 200

def test_head_projects_id_return_headers():
    r = requests.head(url="http://localhost:4567/projects/1").headers
    assert r['Server'] == get_valid_dictionary_schema('projects.id.head.json')['Server'] and \
           r['Content-Type'] == get_valid_dictionary_schema('projects.id.head.json')['Content-Type'] and \
           r['Transfer-Encoding'] == get_valid_dictionary_schema('projects.id.head.json')['Transfer-Encoding']

def test_post_projects_id_existing_return_code():
    body = get_valid_json_schema('projects.id.post.existing.json')
    r = requests.post(url="http://localhost:4567/projects/1", json=body)
    assert r.status_code == 200

def test_post_projects_id_existing_return_payload():
    body = get_valid_json_schema('projects.id.post.existing.json')
    r = requests.post(url="http://localhost:4567/projects/1", json=body)
    assert r.json() == get_valid_json_schema('projects.id.post.existing.return_payload.json')

def test_post_projects_id_notfound_return_code():
    body = get_valid_json_schema('projects.id.post.existing.json')
    r = requests.post(url="http://localhost:4567/projects/55", json=body)
    assert r.status_code == 404

def test_post_projects_id_notfound_return_payload():
    body = get_valid_json_schema('projects.id.post.notfound.json')
    r = requests.post(url="http://localhost:4567/projects/55", json=body)
    assert r.json() == get_valid_json_schema('projects.id.post.notfound.return_payload.json')

def test_put_projects_id_existing_return_code():
    body = get_valid_json_schema('projects.id.put.existing.json')
    r = requests.put(url="http://localhost:4567/projects/1", json=body)
    assert r.status_code == 200

def test_put_projects_id_existing_return_payload():
    body = get_valid_json_schema('projects.id.put.existing.json')
    r = requests.put(url="http://localhost:4567/projects/1", json=body)
    assert r.json() == get_valid_json_schema('projects.id.put.existing.return_payload.json')

def test_put_projects_id_notfound_return_code():
    body = get_valid_json_schema('projects.id.put.existing.json')
    r = requests.put(url="http://localhost:4567/projects/55", json=body)
    assert r.status_code == 404

def test_put_projects_id_notfound_return_payload():
    body = get_valid_json_schema('projects.id.put.notfound.json')
    r = requests.put(url="http://localhost:4567/projects/55", json=body)
    assert r.json() == get_valid_json_schema('projects.id.put.notfound.return_payload.json')

def test_delete_projects_id_existing_return_code():
    r = requests.delete(url="http://localhost:4567/projects/1")
    assert r.status_code == 200

def test_delete_projects_id_existing_return_payload():
    r = requests.delete(url="http://localhost:4567/projects/1")
    try:
        r.json()
    except ValueError:
        assert True
        return
    assert False

def test_delete_projects_id_notfound_return_code():
    r = requests.delete(url="http://localhost:4567/projects/55")
    assert r.status_code == 404

def test_delete_projects_id_notfound_return_payload():
    r = requests.delete(url="http://localhost:4567/projects/55")
    assert r.json() == get_valid_json_schema('projects.id.delete.notfound.return_payload.json')

def test_get_projects_id_tasks_return_code():
    r = requests.get(url="http://localhost:4567/projects/1/tasks")
    assert r.status_code == 200

def test_get_projects_id_tasks_return_payload():
    r = requests.get(url="http://localhost:4567/projects/1/tasks")
    assert r.json() == get_valid_json_schema('projects.id.tasks.get.return_payload.json')

def test_head_projects_id_tasks_return_code():
    r = requests.head(url="http://localhost:4567/projects/1/tasks")
    assert r.status_code == 200

def test_head_projects_id_tasks_headers():
    r = requests.head(url="http://localhost:4567/projects/1/tasks").headers
    assert r['Server'] == get_valid_dictionary_schema('projects.id.tasks.head.json')['Server'] and \
           r['Content-Type'] == get_valid_dictionary_schema('projects.id.tasks.head.json')['Content-Type'] and \
           r['Transfer-Encoding'] == get_valid_dictionary_schema('projects.id.tasks.head.json')['Transfer-Encoding']

def test_post_projects_id_tasks_existing_return_code():
    body = get_valid_json_schema('projects.id.tasks.post.existing.json')
    r = requests.post(url="http://localhost:4567/projects/1/tasks", json=body)
    assert r.status_code == 201

def test_post_projects_id_tasks_existing_return_payload():
    body = get_valid_json_schema('projects.id.tasks.post.existing.json')
    r = requests.post(url="http://localhost:4567/projects/1/tasks", json=body)
    try:
        r.json()
    except ValueError:
        assert True
        return
    assert False

def test_post_projects_id_tasks_bodyid_notfound_return_code():
    body = get_valid_json_schema('projects.id.tasks.post.bodyid.notfound.json')
    r = requests.post(url="http://localhost:4567/projects/1/tasks", json=body)
    assert r.status_code == 404

def test_post_projects_id_tasks_bodyid_notfound_return_payload():
    body = get_valid_json_schema('projects.id.tasks.post.bodyid.notfound.json')
    r = requests.post(url="http://localhost:4567/projects/1/tasks", json=body)
    assert r.json() == get_valid_json_schema('projects.id.tasks.post.bodyid.notfound.return_payload.json')

def test_post_projects_id_tasks_id_notfound_return_code():
    body = get_valid_json_schema('projects.id.tasks.post.id.notfound.json')
    r = requests.post(url="http://localhost:4567/projects/55/tasks", json=body)
    assert r.status_code == 404

def test_post_projects_id_tasks_id_notfound_return_payload():
    body = get_valid_json_schema('projects.id.tasks.post.id.notfound.json')
    r = requests.post(url="http://localhost:4567/projects/55/tasks", json=body)
    assert r.json() == get_valid_json_schema('projects.id.tasks.post.id.notfound.return_payload.json')

def test_delete_projects_id_tasks_id_existing_return_code():
    r = requests.delete(url="http://localhost:4567/projects/1/tasks/2")
    assert r.status_code == 200

def test_delete_projects_id_tasks_id_existing_return_payload():
    r = requests.delete(url="http://localhost:4567/projects/1/tasks/2")
    try:
        r.json()
    except ValueError:
        assert True
        return
    assert False

def test_delete_projects_id_tasks_id_notfound_return_code():
    r = requests.delete(url="http://localhost:4567/projects/1/tasks/5")
    assert r.status_code == 404

def test_delete_projects_id_tasks_id_notfound_return_payload():
    r = requests.delete(url="http://localhost:4567/projects/1/tasks/5")
    assert r.json() == get_valid_json_schema('projects.id.tasks.id.notfound.json')

def test_delete_projects_id_tasks_id_wrong_projectid_return_code():
    r = requests.delete(url="http://localhost:4567/projects/6/tasks/2")
    assert r.status_code == 404

def test_delete_projects_id_tasks_id_wrong_projectid_return_payload():
    r = requests.delete(url="http://localhost:4567/projects/6/tasks/2")
    assert r.json() == get_valid_json_schema('projects.id.tasks.id.wrongprojectid.json')

def test_get_shutdown_return_code():
    r = requests.get(url="http://localhost:4567/shutdown")
    assert r.status_code == 200

def test_get_shutdown_notfound_return_code():
    r = requests.get(url="http://localhost:4567/shutdown/dfgiufdshgusfdh")
    assert r.status_code == 404

def test_get_projects_return_code_with_query_match():
    r = requests.get(url="http://localhost:4567/projects?active=false")
    assert r.status_code == 200

def test_get_projects_return_code_with_noquery_match():
    r = requests.get(url="http://localhost:4567/projects?active=true")
    assert r.status_code == 200

def test_get_projects_return_payload_with_query_match():
    r = requests.get(url="http://localhost:4567/projects?active=false")
    print(r.json())
    print(get_valid_json_schema('projects.get.matchingquery.json'))
    assert assert_valid_json_schema(r.json(), 'projects.get.matchingquery.json')

def test_get_projects_id_existing_return_code_with_query_match():
    r = requests.get(url="http://localhost:4567/projects/1?active=false")
    assert r.status_code == 200

def test_get_projects_id_existing_return_code_with_noquery_match():
    r = requests.get(url="http://localhost:4567/projects/1?active=true")
    assert r.status_code == 200

def test_get_projects_id_existing_return_payload_with_query_match():
    r = requests.get(url="http://localhost:4567/projects/1?active=false")
    assert r.json() == get_valid_json_schema('projects.id.get.existing.return_payload_querymatch.json')

def test_get_projects_id_existing_return_payload_with_noquery_match():
    r = requests.get(url="http://localhost:4567/projects/1?active=true")
    assert r.json() == get_valid_json_schema('projects.id.get.existing.return_payload_noquery.json')

def test_get_projects_id_not_found_return_code_with_query_match():
    r = requests.get(url="http://localhost:4567/projects/55?active=false")
    assert r.status_code == 404

def test_get_projects_id_not_found_return_payload_with_noquery_match():
    r = requests.get(url="http://localhost:4567/projects/55?active=true")
    assert r.json() == get_valid_json_schema('projects.id.get.notfound.return_payload_noquery.json')

def test_get_projects_id_tasks_return_code_with_query_match():
    r = requests.get(url="http://localhost:4567/projects/1/tasks?doneStatus=false")
    assert r.status_code == 200

def test_get_projects_id_tasks_query_match_return_payload_query_match():
    r = requests.get(url="http://localhost:4567/projects/1/tasks?doneStatus=false")
    assert r.json() == get_valid_json_schema('projects.id.tasks.get.return_payload_querymatch.json')

def test_get_projects_id_tasks_return_code_with_noquery_match():
    r = requests.get(url="http://localhost:4567/projects/1/tasks?doneStatus=true")
    assert r.status_code == 200

def test_get_projects_id_tasks_query_match_return_payload_noquery_match():
    r = requests.get(url="http://localhost:4567/projects/1/tasks?doneStatus=true")
    assert r.json() == get_valid_json_schema('projects.id.tasks.get.return_payload_noquery.json')
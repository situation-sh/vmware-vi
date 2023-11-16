# NoPeerHostFound

This fault is thrown when no peer host is found to wake up this host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_peer_host_found import NoPeerHostFound

# TODO update the JSON string below
json = "{}"
# create an instance of NoPeerHostFound from a JSON string
no_peer_host_found_instance = NoPeerHostFound.from_json(json)
# print the JSON string representation of the object
print NoPeerHostFound.to_json()

# convert the object into a dict
no_peer_host_found_dict = no_peer_host_found_instance.to_dict()
# create an instance of NoPeerHostFound from a dict
no_peer_host_found_form_dict = no_peer_host_found.from_dict(no_peer_host_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



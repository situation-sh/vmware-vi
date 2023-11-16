# QueryUnmonitoredHostsRequestType

The parameters of *HealthUpdateManager.QueryUnmonitoredHosts*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider id.  | 
**cluster** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_unmonitored_hosts_request_type import QueryUnmonitoredHostsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUnmonitoredHostsRequestType from a JSON string
query_unmonitored_hosts_request_type_instance = QueryUnmonitoredHostsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryUnmonitoredHostsRequestType.to_json()

# convert the object into a dict
query_unmonitored_hosts_request_type_dict = query_unmonitored_hosts_request_type_instance.to_dict()
# create an instance of QueryUnmonitoredHostsRequestType from a dict
query_unmonitored_hosts_request_type_form_dict = query_unmonitored_hosts_request_type.from_dict(query_unmonitored_hosts_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# QueryCompatibleVmnicsFromHostsRequestType

The parameters of *DistributedVirtualSwitchManager.QueryCompatibleVmnicsFromHosts*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The array of hosts on which the query is to be made to fetch valid PhysicalNics on each host.  Refers instances of *HostSystem*.  | [optional] 
**dvs** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_compatible_vmnics_from_hosts_request_type import QueryCompatibleVmnicsFromHostsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCompatibleVmnicsFromHostsRequestType from a JSON string
query_compatible_vmnics_from_hosts_request_type_instance = QueryCompatibleVmnicsFromHostsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryCompatibleVmnicsFromHostsRequestType.to_json()

# convert the object into a dict
query_compatible_vmnics_from_hosts_request_type_dict = query_compatible_vmnics_from_hosts_request_type_instance.to_dict()
# create an instance of QueryCompatibleVmnicsFromHostsRequestType from a dict
query_compatible_vmnics_from_hosts_request_type_form_dict = query_compatible_vmnics_from_hosts_request_type.from_dict(query_compatible_vmnics_from_hosts_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



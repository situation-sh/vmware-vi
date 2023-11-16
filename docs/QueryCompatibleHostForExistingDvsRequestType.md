# QueryCompatibleHostForExistingDvsRequestType

The parameters of *DistributedVirtualSwitchManager.QueryCompatibleHostForExistingDvs*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**recursive** | **bool** | Whether to search for hosts in the subfolders, if applicable. In the case when container is a *Datacenter*, the recursive flag is applied to its HostFolder.  | 
**dvs** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_compatible_host_for_existing_dvs_request_type import QueryCompatibleHostForExistingDvsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCompatibleHostForExistingDvsRequestType from a JSON string
query_compatible_host_for_existing_dvs_request_type_instance = QueryCompatibleHostForExistingDvsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryCompatibleHostForExistingDvsRequestType.to_json()

# convert the object into a dict
query_compatible_host_for_existing_dvs_request_type_dict = query_compatible_host_for_existing_dvs_request_type_instance.to_dict()
# create an instance of QueryCompatibleHostForExistingDvsRequestType from a dict
query_compatible_host_for_existing_dvs_request_type_form_dict = query_compatible_host_for_existing_dvs_request_type.from_dict(query_compatible_host_for_existing_dvs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FindByUuidRequestType

The parameters of *SearchIndex.FindByUuid*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**uuid** | **str** | The UUID to find. If vmSearch is true, the uuid can be either BIOS or instance UUID.  | 
**vm_search** | **bool** | If true, search for virtual machines, otherwise search for hosts.  | 
**instance_uuid** | **bool** | Should only be set when vmSearch is true. If specified, search for virtual machines whose instance UUID matches the given uuid. Otherwise, search for virtual machines whose BIOS UUID matches the given uuid.  | [optional] 

## Example

```python
from vmware_vi.models.find_by_uuid_request_type import FindByUuidRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindByUuidRequestType from a JSON string
find_by_uuid_request_type_instance = FindByUuidRequestType.from_json(json)
# print the JSON string representation of the object
print FindByUuidRequestType.to_json()

# convert the object into a dict
find_by_uuid_request_type_dict = find_by_uuid_request_type_instance.to_dict()
# create an instance of FindByUuidRequestType from a dict
find_by_uuid_request_type_form_dict = find_by_uuid_request_type.from_dict(find_by_uuid_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateReferenceHostRequestType

The parameters of *HostProfile.UpdateReferenceHost*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.update_reference_host_request_type import UpdateReferenceHostRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReferenceHostRequestType from a JSON string
update_reference_host_request_type_instance = UpdateReferenceHostRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateReferenceHostRequestType.to_json()

# convert the object into a dict
update_reference_host_request_type_dict = update_reference_host_request_type_instance.to_dict()
# create an instance of UpdateReferenceHostRequestType from a dict
update_reference_host_request_type_form_dict = update_reference_host_request_type.from_dict(update_reference_host_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



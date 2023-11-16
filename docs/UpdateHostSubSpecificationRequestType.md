# UpdateHostSubSpecificationRequestType

The parameters of *HostSpecificationManager.UpdateHostSubSpecification*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host_sub_spec** | [**HostSubSpecification**](HostSubSpecification.md) |  | 

## Example

```python
from vmware_vi.models.update_host_sub_specification_request_type import UpdateHostSubSpecificationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostSubSpecificationRequestType from a JSON string
update_host_sub_specification_request_type_instance = UpdateHostSubSpecificationRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateHostSubSpecificationRequestType.to_json()

# convert the object into a dict
update_host_sub_specification_request_type_dict = update_host_sub_specification_request_type_instance.to_dict()
# create an instance of UpdateHostSubSpecificationRequestType from a dict
update_host_sub_specification_request_type_form_dict = update_host_sub_specification_request_type.from_dict(update_host_sub_specification_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateHostSpecificationRequestType

The parameters of *HostSpecificationManager.UpdateHostSpecification*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host_spec** | [**HostSpecification**](HostSpecification.md) |  | 

## Example

```python
from vmware_vi.models.update_host_specification_request_type import UpdateHostSpecificationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostSpecificationRequestType from a JSON string
update_host_specification_request_type_instance = UpdateHostSpecificationRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateHostSpecificationRequestType.to_json()

# convert the object into a dict
update_host_specification_request_type_dict = update_host_specification_request_type_instance.to_dict()
# create an instance of UpdateHostSpecificationRequestType from a dict
update_host_specification_request_type_form_dict = update_host_specification_request_type.from_dict(update_host_specification_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeleteHostSpecificationRequestType

The parameters of *HostSpecificationManager.DeleteHostSpecification*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.delete_host_specification_request_type import DeleteHostSpecificationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteHostSpecificationRequestType from a JSON string
delete_host_specification_request_type_instance = DeleteHostSpecificationRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteHostSpecificationRequestType.to_json()

# convert the object into a dict
delete_host_specification_request_type_dict = delete_host_specification_request_type_instance.to_dict()
# create an instance of DeleteHostSpecificationRequestType from a dict
delete_host_specification_request_type_form_dict = delete_host_specification_request_type.from_dict(delete_host_specification_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



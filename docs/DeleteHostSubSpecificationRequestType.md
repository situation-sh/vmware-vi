# DeleteHostSubSpecificationRequestType

The parameters of *HostSpecificationManager.DeleteHostSubSpecification*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**sub_spec_name** | **str** | The name of the host sub specification to be deleted.  | 

## Example

```python
from vmware_vi.models.delete_host_sub_specification_request_type import DeleteHostSubSpecificationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteHostSubSpecificationRequestType from a JSON string
delete_host_sub_specification_request_type_instance = DeleteHostSubSpecificationRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteHostSubSpecificationRequestType.to_json()

# convert the object into a dict
delete_host_sub_specification_request_type_dict = delete_host_sub_specification_request_type_instance.to_dict()
# create an instance of DeleteHostSubSpecificationRequestType from a dict
delete_host_sub_specification_request_type_form_dict = delete_host_sub_specification_request_type.from_dict(delete_host_sub_specification_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



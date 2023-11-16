# CreateDescriptorRequestType

The parameters of *OvfManager.CreateDescriptor*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**cdp** | [**OvfCreateDescriptorParams**](OvfCreateDescriptorParams.md) |  | 

## Example

```python
from vmware_vi.models.create_descriptor_request_type import CreateDescriptorRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDescriptorRequestType from a JSON string
create_descriptor_request_type_instance = CreateDescriptorRequestType.from_json(json)
# print the JSON string representation of the object
print CreateDescriptorRequestType.to_json()

# convert the object into a dict
create_descriptor_request_type_dict = create_descriptor_request_type_instance.to_dict()
# create an instance of CreateDescriptorRequestType from a dict
create_descriptor_request_type_form_dict = create_descriptor_request_type.from_dict(create_descriptor_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



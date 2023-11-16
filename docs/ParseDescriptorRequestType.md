# ParseDescriptorRequestType

The parameters of *OvfManager.ParseDescriptor*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ovf_descriptor** | **str** | The OVF descriptor to examine.  | 
**pdp** | [**OvfParseDescriptorParams**](OvfParseDescriptorParams.md) |  | 

## Example

```python
from vmware_vi.models.parse_descriptor_request_type import ParseDescriptorRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ParseDescriptorRequestType from a JSON string
parse_descriptor_request_type_instance = ParseDescriptorRequestType.from_json(json)
# print the JSON string representation of the object
print ParseDescriptorRequestType.to_json()

# convert the object into a dict
parse_descriptor_request_type_dict = parse_descriptor_request_type_instance.to_dict()
# create an instance of ParseDescriptorRequestType from a dict
parse_descriptor_request_type_form_dict = parse_descriptor_request_type.from_dict(parse_descriptor_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



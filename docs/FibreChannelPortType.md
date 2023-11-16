# FibreChannelPortType

A boxed *FibreChannelPortType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**FibreChannelPortTypeEnum**](FibreChannelPortTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.fibre_channel_port_type import FibreChannelPortType

# TODO update the JSON string below
json = "{}"
# create an instance of FibreChannelPortType from a JSON string
fibre_channel_port_type_instance = FibreChannelPortType.from_json(json)
# print the JSON string representation of the object
print FibreChannelPortType.to_json()

# convert the object into a dict
fibre_channel_port_type_dict = fibre_channel_port_type_instance.to_dict()
# create an instance of FibreChannelPortType from a dict
fibre_channel_port_type_form_dict = fibre_channel_port_type.from_dict(fibre_channel_port_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



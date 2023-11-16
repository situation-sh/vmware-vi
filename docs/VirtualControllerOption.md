# VirtualControllerOption

The VirtualControllerOption data object type contains information about a virtual controller type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**IntOption**](IntOption.md) |  | 
**supported_device** | **List[str]** | Array of supported device options for this controller.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_controller_option import VirtualControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualControllerOption from a JSON string
virtual_controller_option_instance = VirtualControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualControllerOption.to_json()

# convert the object into a dict
virtual_controller_option_dict = virtual_controller_option_instance.to_dict()
# create an instance of VirtualControllerOption from a dict
virtual_controller_option_form_dict = virtual_controller_option.from_dict(virtual_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



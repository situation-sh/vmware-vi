# VirtualVideoCardOption

This data object type contains the options for the *VirtualVideoCard* data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_ram_size_in_kb** | [**LongOption**](LongOption.md) |  | [optional] 
**num_displays** | [**IntOption**](IntOption.md) |  | [optional] 
**use_auto_detect** | [**BoolOption**](BoolOption.md) |  | [optional] 
**support3_d** | [**BoolOption**](BoolOption.md) |  | [optional] 
**use3d_renderer_supported** | [**BoolOption**](BoolOption.md) |  | [optional] 
**graphics_memory_size_in_kb** | [**LongOption**](LongOption.md) |  | [optional] 
**graphics_memory_size_supported** | [**BoolOption**](BoolOption.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_video_card_option import VirtualVideoCardOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVideoCardOption from a JSON string
virtual_video_card_option_instance = VirtualVideoCardOption.from_json(json)
# print the JSON string representation of the object
print VirtualVideoCardOption.to_json()

# convert the object into a dict
virtual_video_card_option_dict = virtual_video_card_option_instance.to_dict()
# create an instance of VirtualVideoCardOption from a dict
virtual_video_card_option_form_dict = virtual_video_card_option.from_dict(virtual_video_card_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



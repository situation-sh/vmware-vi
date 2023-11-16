# VirtualSoundCardDeviceBackingOption

The VirtualSoundCardBackingOption class contains the options for the virtual sound card backing class. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_sound_card_device_backing_option import VirtualSoundCardDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSoundCardDeviceBackingOption from a JSON string
virtual_sound_card_device_backing_option_instance = VirtualSoundCardDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualSoundCardDeviceBackingOption.to_json()

# convert the object into a dict
virtual_sound_card_device_backing_option_dict = virtual_sound_card_device_backing_option_instance.to_dict()
# create an instance of VirtualSoundCardDeviceBackingOption from a dict
virtual_sound_card_device_backing_option_form_dict = virtual_sound_card_device_backing_option.from_dict(virtual_sound_card_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



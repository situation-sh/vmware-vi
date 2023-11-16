# VirtualSoundBlaster16Option

The VirtualSoundBlaster16Option data object type contains the options for a virtual SoundBlaster 16 sound card. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_sound_blaster16_option import VirtualSoundBlaster16Option

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSoundBlaster16Option from a JSON string
virtual_sound_blaster16_option_instance = VirtualSoundBlaster16Option.from_json(json)
# print the JSON string representation of the object
print VirtualSoundBlaster16Option.to_json()

# convert the object into a dict
virtual_sound_blaster16_option_dict = virtual_sound_blaster16_option_instance.to_dict()
# create an instance of VirtualSoundBlaster16Option from a dict
virtual_sound_blaster16_option_form_dict = virtual_sound_blaster16_option.from_dict(virtual_sound_blaster16_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



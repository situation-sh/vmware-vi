# VirtualSoundBlaster16

The VirtualSoundBlaster16 data object type represents a Sound Blaster 16 sound card in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_sound_blaster16 import VirtualSoundBlaster16

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSoundBlaster16 from a JSON string
virtual_sound_blaster16_instance = VirtualSoundBlaster16.from_json(json)
# print the JSON string representation of the object
print VirtualSoundBlaster16.to_json()

# convert the object into a dict
virtual_sound_blaster16_dict = virtual_sound_blaster16_instance.to_dict()
# create an instance of VirtualSoundBlaster16 from a dict
virtual_sound_blaster16_form_dict = virtual_sound_blaster16.from_dict(virtual_sound_blaster16_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



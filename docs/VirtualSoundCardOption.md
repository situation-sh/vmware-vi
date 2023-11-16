# VirtualSoundCardOption

The VirtualSoundCardOption data class contains the options for the virtual sound card class. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_sound_card_option import VirtualSoundCardOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSoundCardOption from a JSON string
virtual_sound_card_option_instance = VirtualSoundCardOption.from_json(json)
# print the JSON string representation of the object
print VirtualSoundCardOption.to_json()

# convert the object into a dict
virtual_sound_card_option_dict = virtual_sound_card_option_instance.to_dict()
# create an instance of VirtualSoundCardOption from a dict
virtual_sound_card_option_form_dict = virtual_sound_card_option.from_dict(virtual_sound_card_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



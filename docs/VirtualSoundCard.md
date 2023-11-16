# VirtualSoundCard

This data object type represents a sound card in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_sound_card import VirtualSoundCard

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSoundCard from a JSON string
virtual_sound_card_instance = VirtualSoundCard.from_json(json)
# print the JSON string representation of the object
print VirtualSoundCard.to_json()

# convert the object into a dict
virtual_sound_card_dict = virtual_sound_card_instance.to_dict()
# create an instance of VirtualSoundCard from a dict
virtual_sound_card_form_dict = virtual_sound_card.from_dict(virtual_sound_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



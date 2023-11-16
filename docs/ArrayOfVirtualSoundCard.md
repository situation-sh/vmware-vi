# ArrayOfVirtualSoundCard

A boxed array of *VirtualSoundCard*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSoundCard]**](VirtualSoundCard.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_sound_card import ArrayOfVirtualSoundCard

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSoundCard from a JSON string
array_of_virtual_sound_card_instance = ArrayOfVirtualSoundCard.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSoundCard.to_json()

# convert the object into a dict
array_of_virtual_sound_card_dict = array_of_virtual_sound_card_instance.to_dict()
# create an instance of ArrayOfVirtualSoundCard from a dict
array_of_virtual_sound_card_form_dict = array_of_virtual_sound_card.from_dict(array_of_virtual_sound_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



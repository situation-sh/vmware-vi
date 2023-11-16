# ArrayOfVirtualHdAudioCard

A boxed array of *VirtualHdAudioCard*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualHdAudioCard]**](VirtualHdAudioCard.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_hd_audio_card import ArrayOfVirtualHdAudioCard

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualHdAudioCard from a JSON string
array_of_virtual_hd_audio_card_instance = ArrayOfVirtualHdAudioCard.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualHdAudioCard.to_json()

# convert the object into a dict
array_of_virtual_hd_audio_card_dict = array_of_virtual_hd_audio_card_instance.to_dict()
# create an instance of ArrayOfVirtualHdAudioCard from a dict
array_of_virtual_hd_audio_card_form_dict = array_of_virtual_hd_audio_card.from_dict(array_of_virtual_hd_audio_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VirtualHdAudioCard

The VirtualHdAudioCard data object type represents a HD Audio sound card in a virtual machine.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_hd_audio_card import VirtualHdAudioCard

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualHdAudioCard from a JSON string
virtual_hd_audio_card_instance = VirtualHdAudioCard.from_json(json)
# print the JSON string representation of the object
print VirtualHdAudioCard.to_json()

# convert the object into a dict
virtual_hd_audio_card_dict = virtual_hd_audio_card_instance.to_dict()
# create an instance of VirtualHdAudioCard from a dict
virtual_hd_audio_card_form_dict = virtual_hd_audio_card.from_dict(virtual_hd_audio_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



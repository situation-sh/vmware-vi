# VirtualHdAudioCardOption

The VirtualHdAudioCardOption data object type contains the options for a virtual HD Audio sound card.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_hd_audio_card_option import VirtualHdAudioCardOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualHdAudioCardOption from a JSON string
virtual_hd_audio_card_option_instance = VirtualHdAudioCardOption.from_json(json)
# print the JSON string representation of the object
print VirtualHdAudioCardOption.to_json()

# convert the object into a dict
virtual_hd_audio_card_option_dict = virtual_hd_audio_card_option_instance.to_dict()
# create an instance of VirtualHdAudioCardOption from a dict
virtual_hd_audio_card_option_form_dict = virtual_hd_audio_card_option.from_dict(virtual_hd_audio_card_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


